import numpy as np
import networkx as nx

class SubstrateNetwork:
    def __init__(self, config):
        self.config = config
        self.graph = self._create_network()
        
    def _create_network(self):
        """Create a random graph for the substrate network."""
        G = nx. erdos_renyi_graph(self.config.num_nodes, self.config.edge_prob)
        for node in G.nodes:
            G.nodes[node]['cpu'] = np.random.uniform(0, self.config.max_cpu)
            G.nodes[node]['bandwidth'] = np.random.uniform(0, self.config.max_bandwidth)
        for edge in G.edges:
            G.edges[edge]['bandwidth'] = np.random.uniform(0, self.config.max_bandwidth)
        return G
    
    def reset(self):
        for node in self.graph.nodes:
            self.graph.nodes[node]['cpu_util'] = 0
            self.graph.nodes[node]['bandwidth_util'] = 0
        for edge in self.graph.edges:
            self.graph.edges[edge]['bandwidth_util'] = 0
    
    def get_cpu_utilization(self):
        return [node['cpu_util'] for node in self.graph.nodes.values()]
    
    def get_bandwidth_utilization(self):
        return [node['bandwidth_util'] for node in self.graph.nodes.values()]
    
    def get_node_stress(self):
        return [node['cpu_util'] / node['cpu'] for node in self.graph.nodes.values()]
    
    def get_link_stress(self):
        return [edge['bandwidth_util'] / edge['bandwidth'] for edge in self.graph.edges.values()]
    
    def get_topology_features(self):
        # Calculate topology features (e.g., degree distribution, clustering coefficient)
        # For simplicity, we'll just use the average degree
        avg_degree = np.mean([degree for node, degree in self.graph.degree()])
        return [avg_degree]
    
    def can_embed_node(self, substrate_node, cpu_demand):
        return self.graph.nodes[substrate_node]['cpu'] >= cpu_demand
    
    def embed_node(self, substrate_node, cpu_demand):
        self.graph.nodes[substrate_node]['cpu_util'] += cpu_demand