import torch
import torch.optim as optim
from .model import ActorCritic
from .memory import Memory
from .utils import calculate_advantage
import numpy as np
class PPOAgent:
    def __init__(self, config):
        self.config = config
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Initialize actor-critic network
        self.actor_critic = ActorCritic(
            config.state_dim,
            config.action_dim
        ).to(self.device)
        
        # Initialize optimizer
        self.optimizer = optim.Adam(
            self.actor_critic.parameters(),
            lr=config.learning_rate
        )
        
        # Initialize memory
        self.memory = Memory()
    
    def select_action(self, state):
        state = torch.FloatTensor(state).unsqueeze(0).to(self.device)
        with torch.no_grad():
            action_probs, _ = self.actor_critic(state)
        
        # Sample action from the probability distribution
        dist = torch.distributions.Categorical(action_probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        
        return action.item(), log_prob.item()
    
    def update(self):
        # Get all data from memory
        states, actions, rewards, old_log_probs, dones, next_states = self.memory.get_all()
        
        states = np.array(states)
        actions = np.array(actions)
        rewards = np.array(rewards)
        old_log_probs = np.array(old_log_probs)
        dones = np.array(dones)
        next_states = np.array(next_states)
        
        # Convert to tensors
        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        old_log_probs = torch.FloatTensor(old_log_probs).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        
        # Get current values and action probabilities
        action_probs, values = self.actor_critic(states)
        _, next_values = self.actor_critic(next_states)
        
        # Calculate advantages
        advantages, returns = calculate_advantage(
            rewards, dones, values.detach(), 
            next_values.detach(), self.config.discount_factor
        )
        
        # PPO update
        for _ in range(self.config.epochs):
            # Get current action probabilities and values
            current_action_probs, current_values = self.actor_critic(states)
            dist = torch.distributions.Categorical(current_action_probs)
            current_log_probs = dist.log_prob(actions)
            
            # Calculate ratios and surrogate objectives
            ratios = torch .exp(current_log_probs - old_log_probs)
            clipped_ratios = torch.clamp(ratios, 1 - self.config.clip_epsilon, 1 + self.config.clip_epsilon)
            surrogate = torch.min(ratios * advantages, clipped_ratios * advantages)
            
            # Calculate value loss
            value_loss = (current_values - returns) ** 2
            
            # Calculate entropy bonus
            entropy_bonus = -self.config.entropy_coefficient * dist.entropy()
            
            # Calculate total loss
            loss = -surrogate.mean() + self.config.value_coefficient * value_loss.mean() + entropy_bonus.mean()
            
            # Backpropagate and update
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        
        # Clear memory
        self.memory.clear()