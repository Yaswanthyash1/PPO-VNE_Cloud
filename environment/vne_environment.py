import numpy as np
from optimizer.energy_optimizer import EnergyOptimizer

class VNEEnvironment:
    def __init__(self, config):
        self.config = config
        self.substrate_network = SubstrateNetwork(config)
        self.virtual_networks = []
        self.total_vn_requests = 0
        self.embedded_vn_counts = 0
        self.revenues = 0
        self.costs = 0
        self.energy_optimizer = EnergyOptimizer(config)
        self.total_energy = 0
        self.energy_consumption = 0
        self.current_virtual_network = None

    def reset(self):
        self.substrate_network.reset()
        self.virtual_networks = []
        self.total_vn_requests = 0
        self.embedded_vn_counts = 0
        self.revenues = 0
        self.costs = 0
        self.total_energy = 0
        self.energy_consumption = 0

        return self._get_state()
    
    def step(self, action):
        # Perform action on substrate network
        self.substrate_network.perform_action(action)
        
        # Generate new virtual network request
        vn_request = self._generate_vn_request()
        self.virtual_networks.append(vn_request)
        self.total_vn_requests += 1
        
        # Check if virtual network can be embedded
        if self.substrate_network.can_embed(vn_request):
            self.substrate_network.embed(vn_request)
            self.embedded_vn_counts += 1
            self.revenues += vn_request.revenue
            self.costs += vn_request.cost
        else:
            self.revenues -= vn_request.penalty
            self.costs += vn_request.penalty
        
        # Calculate reward
        reward = self.revenues - self.costs
        
        self.energy_consumption = self.energy_optimizer.calculate_energy(
            self.substrate_network 
            )
        self.total_energy += self.energy_consumption
        
        # Incorporate energy into reward calculation
        energy_penalty = self.config.energy_weight * self.energy_consumption
        reward -= energy_penalty
        # Check if episode is done
        done = self.total_vn_requests >= self.config.max_vn_requests
        
        return self._get_state(), reward, done, {}
    
    def _get_state(self):
        cpu_util = np.mean(self.substrate_network.get_cpu_utilization())
        bw_util = np.mean(self.substrate_network.get_bandwidth_utilization())
        node_stress = np.mean(self.substrate_network.get_node_stress())
        link_stress = np.mean(self.substrate_network.get_link_stress())
        topo_features = self.substrate_network.get_topology_features()
        
        state = np.concatenate([
            [cpu_util],
            [bw_util],
            [node_stress],
            [link_stress],
            topo_features
        ])
        
        return state
    
    def _generate_vn_request(self):
        # Generate random virtual network request
        num_nodes = np.random.randint(self.config.min_vn_nodes , self.config.max_vn_nodes + 1)
        cpu_demands = np.random.uniform(self.config.cpu_demand_range[0], self.config.cpu_demand_range[1], num_nodes)
        bw_demands = np.random.uniform(self.config.bandwidth_demand_range[0], self.config.bandwidth_demand_range[1], num_nodes)
        revenue = np.random.uniform(10, 50)
        penalty = np.random.uniform(5, 20)
        
        return VirtualNetworkRequest(num_nodes, cpu_demands, bw_demands, revenue, penalty)

class SubstrateNetwork:
    def __init__(self, config):
        self.config = config
        self.nodes = [Node(config) for _ in range(config.num_nodes)]
        self.edges = []
        
        # Initialize edges
        for i in range(config.num_nodes):
            for j in range(i + 1, config.num_nodes):
                if np.random.rand() < config.edge_prob:
                    self.edges.append(Edge(self.nodes[i], self.nodes[j]))
    
    def reset(self):
        for node in self.nodes:
            node.reset()
        for edge in self.edges:
            edge.reset()
    
    def perform_action(self, action):
        # Perform action on substrate network
        node = self.nodes[action]
        node.cpu_utilization += 10  # Simulate CPU utilization increase
    
    def can_embed(self, vn_request):
        # Check if virtual network can be embedded
        for node in self.nodes:
            if node.can_embed(vn_request):
                return True
        return False
    
    def embed(self, vn_request):
        # Embed virtual network
        for node in self.nodes:
            if node.can_embed(vn_request):
                node.embed(vn_request)
                break
    
    def get_cpu_utilization(self):
        return [node.cpu_utilization for node in self.nodes]
    
    def get_bandwidth_utilization(self):
        return [edge.bandwidth_utilization for edge in self.edges]
    
    def get_node_stress(self):
        return [node.stress for node in self.nodes]
    
    def get_link_stress(self):
        return [edge.stress for edge in self.edges]
    
    def get_topology_features(self):
        return [node.feature for node in self.nodes]

class Node:
    def __init__(self, config):
        self.config = config
        self.cpu_utilization = 0
        self.stress = 0
        self.feature = np.random.rand()  # Random feature
    
    def reset(self):
        self.cpu_utilization = 0
        self.stress = 0

    
    def can_embed(self, vn_request):
        # Check if node can embed virtual network
        return self.cpu_utilization + vn_request.cpu_demands[0] <= self.config.max_cpu
    
    def embed(self, vn_request):
        # Embed virtual network
        self.cpu_utilization += vn_request.cpu_demands[0]

class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.bandwidth_utilization = 0
        self.stress = 0
    
    def reset(self):
        self.bandwidth_utilization = 0
        self.stress = 0

class VirtualNetworkRequest:
    def __init__(self, num_nodes, cpu_demands, bw_demands, revenue, penalty):
        self.num_nodes = num_nodes
        self.cpu_demands = cpu_demands
        self.bw_demands = bw_demands
        self.revenue = revenue
        self.penalty = penalty
        self.cost = sum(cpu_demands) + sum(bw_demands)