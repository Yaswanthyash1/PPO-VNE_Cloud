class Config:
    def __init__(self):
        # Network parameters
        self.num_nodes = 20  # Number of substrate network nodes
        self.edge_prob = 0.1  # Probability of edge creation
        self.max_cpu = 100
        self.max_bandwidth = 100
        
        # Virtual network parameters
        self.min_vn_nodes = 2
        self.max_vn_nodes = 5
        self.cpu_demand_range = (10, 30)
        self.max_vn_requests = 120
        self.bandwidth_demand_range = (10, 30)
        
        # Energy parameters
        self.P_idle = 150  # Idle power consumption
        self.P_peak = 250  # Peak power consumption
        self.P_port = 10   # Port power consumption
        self.bandwidth_unit_power = 0.1
        
        # Learning parameters
        self.learning_rate = 0.001
        self.discount_factor = 0.99
        self.batch_size = 32
        self.epochs = 4
        self.clip_epsilon = 0.2
        self.value_coefficient = 0.5
        self.entropy_coefficient = 0.01
        
        # Reward weights
        self.revenue_weight = 1.0
        self.energy_weight = 0.5
        
        # Calculate state and action dimensions
        self.calculate_dimensions()
        
    def calculate_dimensions(self):
        # State space dimensions
        base_features = 4  # CPU util, BW util, node stress, link stress
        topology_features = self.num_nodes  # One feature per node
        self.state_dim = base_features + topology_features
        
        # Action space dimensions (one action per substrate node)
        self.action_dim = self.num_nodes