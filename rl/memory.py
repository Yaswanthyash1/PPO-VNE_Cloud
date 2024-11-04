class Memory:
    def __init__(self):
        self.states = []
        self.actions = []
        self.rewards = []
        self.log_probs = []
        self.dones = []
        self.next_states = []
        
    def push(self, state, action, reward, log_prob, done, next_state):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.log_probs.append(log_prob)
        self.dones.append(done)
        self.next_states.append(next_state)
        
    def clear(self):
        self.states.clear()
        self.actions.clear()
        self.rewards.clear()
        self.log_probs.clear()
        self.dones.clear()
        self.next_states.clear()
        
    def get_all(self):
        return (self.states, self.actions, self.rewards, 
                self.log_probs, self.dones, self.next_states)