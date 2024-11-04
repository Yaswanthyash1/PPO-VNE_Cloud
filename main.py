from config import Config
from rl.agent import PPOAgent
from environment.vne_environment import VNEEnvironment 
from visualize import generate_graphs  # Import the visualization function

def run_simulation(num_episodes, config):
    agent = PPOAgent(config)
    env = VNEEnvironment(config)
    
    # Create lists to store metrics over time
    total_vn_requests_list = []
    embedded_vn_counts_list = []
    revenues_list = []
    costs_list = []
    
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
        
        # Store metrics for this episode
        total_vn_requests_list.append(env.total_vn_requests)
        embedded_vn_counts_list.append(env.embedded_vn_counts)
        revenues_list.append(env.revenues)
        costs_list.append(env.costs)
        
        # Print progress
        if (episode + 1) % 10 == 0:  # Print every 10 episodes
            print(f"Episode {episode + 1}/{num_episodes}")
            print(f"Total VN requests: {env.total_vn_requests}")
            print(f"Embedded VN counts: {env.embedded_vn_counts}")
            print(f"Revenues: {env.revenues}")
            print(f"Costs: {env.costs}\n")
    
    return total_vn_requests_list, embedded_vn_counts_list, revenues_list, costs_list

def main():
    config = Config()
    num_episodes = 1000
    
    # Run simulation and get metrics over time
    total_vn_requests, embedded_vn_counts, revenues, costs = run_simulation(num_episodes, config)
    
    # Generate visualization graphs
    generate_graphs([embedded_vn_counts[-1]], [total_vn_requests[-1]], [revenues[-1]], [costs[-1]])
    # Print final results
    print("\nFinal Results:")
    print(f"Total VN requests: {total_vn_requests[-1]}")
    print(f"Embedded VN counts: {embedded_vn_counts[-1]}")
    print(f"Final Revenue: {revenues[-1]}")
    print(f"Final Cost: {costs[-1]}")
    print(f"Revenue/Cost Ratio: {revenues[-1]/costs[-1] if costs[-1] > 0 else 0}")
    print(f"Acceptance Ratio: {embedded_vn_counts[-1]/total_vn_requests[-1] if total_vn_requests[-1] > 0 else 0}")

if __name__ == "__main__":
    main()