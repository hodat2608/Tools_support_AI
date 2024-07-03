import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1("C:/Users/CCSX009/Documents/ultralytics-main/2024-03-05_00-01-31-398585-C1.jpg")
print(hidden1.size())