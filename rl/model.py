import torch
import torch.nn as nn
import torch.nn.functional as F

class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(ActorCritic, self).__init__()
        
        # Shared layers
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        
        # Actor head (policy)
        self.actor = nn.Linear(64, action_dim)
        
        # Critic head (value)
        self.critic = nn.Linear(64, 1)
        
    def forward(self, x):
        # Shared layers
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        
        # Actor: action probabilities
        action_probs = F.softmax(self.actor(x), dim=-1)
        
        # Critic: state value
        state_value = self.critic(x)
        
        return action_probs, state_value