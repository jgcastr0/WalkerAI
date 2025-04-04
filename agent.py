import torch
import torch.nn as nn
import torch.nn.functional as F

class BipedalAgent(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 64)
        self.fc2 = nn.Linear(64, 64)
        self.out = nn.Linear(64, 2)  # controla duas pernas

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return torch.tanh(self.out(x)) * 0.1  # pequena variação angular
