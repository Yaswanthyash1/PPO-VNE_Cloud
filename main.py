from config import Config
from rl.agent import PPOAgent
from environment.vne_environment import VNEEnvironment 
from visualize import generate_graphs  # Import the visualization function

def run_simulation(num_episodes, config, total_vn_requests_list, embedded_vn_counts_list, revenues_list, costs_list,energy_list):
    for max_requests in [20, 40, 60, 80, 100, 120]:  # Loop through the desired request counts
        config.max_vn_requests = max_requests  # Update the config for the current run
        print(f"\nRunning simulation with max VN requests: {max_requests}")
        
        agent = PPOAgent(config)
        env = VNEEnvironment(config)
        
        # Reset metrics for this run
        total_vn_requests = 0
        embedded_vn_counts = 0
        revenues = 0
        costs = 0
        total_energy = 0

        for episode in range(num_episodes):
            state = env.reset()
            done = False
            
            while not done:
                action, log_prob = agent.select_action(state)
                next_state, reward, done, _ = env.step(action)
                
                # Store experience in memory
                agent.memory.push(state, action, reward, log_prob, done, next_state)
                
                state = next_state
            
            # Update agent
            agent.update()
            
            # Accumulate metrics for this episode
            total_vn_requests += env.total_vn_requests
            embedded_vn_counts += env.embedded_vn_counts
            revenues += env.revenues
            costs += env.costs
            total_energy = env.total_energy

            # Print progress
            if (episode + 1) % 10 == 0:  # Print every 10 episodes
                print(f"Episode {episode + 1}/{num_episodes}")
                print(f"Total VN requests: {env.total_vn_requests}")
                print(f"Embedded VN counts: {env.embedded_vn_counts}")
                print(f"Revenues: {env.revenues}")
                print(f"Costs: {env.costs}\n")
        
        # Store the average metrics for this run
        total_vn_requests_list.append(total_vn_requests / num_episodes)
        embedded_vn_counts_list.append(embedded_vn_counts / num_episodes)
        revenues_list.append(revenues / num_episodes)
        costs_list.append(costs / num_episodes)
        energy_list.append(total_energy/100)

    # Generate visualization graphs
    generate_graphs(embedded_vn_counts_list, total_vn_requests_list, revenues_list, costs_list, energy_list)

def main():
    config = Config()
    num_episodes = 100
    
    # Create lists to store metrics over different max request counts
    total_vn_requests_list = []
    embedded_vn_counts_list = []
    revenues_list = []
    costs_list = []
    energy_list = [] 
    
    # Run simulation and get metrics over time
    run_simulation(num_episodes, config, total_vn_requests_list, embedded_vn_counts_list, revenues_list, costs_list,energy_list)

    # Print final results (optional)
    print("\nFinal Results:")
    print(f"Max VN Requests: {config.max_vn_requests}")
    print(f"Average Total VN Requests: {sum(total_vn_requests_list) / len(total_vn_requests_list)}")
    print(f"Average Embedded VN Counts: {sum(embedded_vn_counts_list) / len(embedded_vn_counts_list)}")
    print(f"Average Revenue: {sum(revenues_list) / len(revenues_list)}")
    print(f"Average Cost: {sum(costs_list) / len(costs_list)}")
    print(f"Average Energy Consumption: {sum(energy_list) / len(energy_list)}")

if __name__ == "__main__":
    main()