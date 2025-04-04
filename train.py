import torch
import torch.optim as optim
from environment import Environment
from agent import BipedalAgent
import numpy as np

env = Environment()
agent = BipedalAgent()
optimizer = optim.Adam(agent.parameters(), lr=0.001)

for episode in range(1000):
    state = torch.tensor(env.reset(), dtype=torch.float32)
    total_reward = 0

    for t in range(200):
        action = agent(state)
        next_state, reward, done = env.step(action.detach().numpy())
        next_state = torch.tensor(next_state, dtype=torch.float32)

        # Loss = -reward (tentando maximizar recompensa)
        loss = -torch.tensor(reward, dtype=torch.float32)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        state = next_state
        total_reward += reward

        if done:
            break

    print(f"Episode {episode} | Total reward: {total_reward:.2f}")
