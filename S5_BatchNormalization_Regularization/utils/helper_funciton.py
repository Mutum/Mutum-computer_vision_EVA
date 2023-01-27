# import torch
# import torch.optim as optim
# import matplotlib.pyplot as plt
# from torch.optim.lr_scheduler import StepLR,OneCycleLR
import model
# from utils import train as trn
# from utils import test as tst

from torchsummary import summary

def model_summary(model, input_size):
    result = summary(model, input_size=input_size)
    print(result)