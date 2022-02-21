import torch
import torch.nn as nn
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        
        self.linear_one = nn.Linear(input_size, hidden_size)
        self.linear_two = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = F.relu(self.linear_one(x))
        x = self.linear_two(x)

        return x
    
    def save(self, file_name='model.pth'):
        model_folder_path = './model'

        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)