import numpy as np

class VirtualNetwork:
    def __init__(self, num_nodes, config):
        self.num_nodes = num_nodes
        self.config = config
        self.nodes = self._create_nodes()
        self.edges = self._create_edges()
    
    def _create_nodes(self):
        nodes = {}
        for i in range(self.num_nodes):
            cpu_demand = np.random.uniform(self.config.cpu_demand_range[0], self.config.cpu_demand_range[1])
            nodes[i] = {'cpu': cpu_demand}
        return nodes
    
    def _create_edges(self):
        edges = {}
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                bandwidth_demand = np.random.uniform(self.config.bandwidth_demand_range[0], self.config.bandwidth_demand_range[1])
                edges[(i, j)] = {'bandwidth': bandwidth_demand}
        return edges