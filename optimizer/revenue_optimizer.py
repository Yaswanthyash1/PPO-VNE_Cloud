class RevenueOptimizer:
    def __init__(self, config):
        self.config = config

    def calculate_revenue(self, substrate_network, virtual_network):
        revenue = 0
        # Calculate revenue based on CPU and bandwidth
        for node in virtual_network.nodes:
            revenue += virtual_network.nodes[node]['cpu'] * self.config.revenue_weight
        for edge in virtual_network.edges:
            revenue += virtual_network.edges[edge]['bandwidth'] * self.config.revenue_weight
        return revenue