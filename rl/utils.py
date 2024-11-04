import torch

def calculate_advantage(rewards, dones, values, next_values, discount_factor):
    advantages = []
    returns = []
    running_return = 0
    
    for t in reversed(range(len(rewards))):
        if dones[t]:
            running_return = 0
        
        running_return = rewards[t] + discount_factor * running_return * (1 - dones[t])
        returns.insert(0, running_return)
        
        # Calculate advantage
        if t < len(rewards) - 1:
            td_error = rewards[t] + discount_factor * next_values[t+1] * (1 - dones[t]) - values[t]
        else:
            td_error = rewards[t] - values[t]
        advantages.insert(0, td_error)
    
    advantages = torch.tensor(advantages, dtype=torch.float32)
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
    
    return advantages, torch.tensor(returns, dtype=torch.float32)