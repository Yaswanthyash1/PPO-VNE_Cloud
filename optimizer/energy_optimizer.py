class EnergyOptimizer:
    def __init__(self, config):
        self.config = config

    def calculate_energy(self, substrate_network):
        energy = 0
        # Calculate energy consumption based on node utilization
        for node in substrate_network.graph.nodes:
            energy += self.config.P_idle + self.config.P_peak * substrate_network.get_node_utilization(node)
        for edge in substrate_network.graph.edges:
            energy += self.config.P_port + self.config.bandwidth_unit_power * substrate_network.get_link_utilization(edge)
        return energy