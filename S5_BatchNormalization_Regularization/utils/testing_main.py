import torch
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR,OneCycleLR


import dataloader
import model
from helper_funciton import summary
from train import train
from test import test
from plot_inference import plot_matrics

train_transforms, test_transforms = dataloader.image_augmentations()
train_data, test_data = dataloader.download_train_test(train_transforms, test_transforms)


SEED = 1

# CUDA?
cuda = torch.cuda.is_available()
print("CUDA Availalbe?", cuda)

# For reproducibility
torch.manual_seed(SEED)

if cuda:
    torch.cuda.manual_seed(SEED)

# dataloader arguments
dataloader_args = dict(shuffle=True,batch_size=128,num_workers=4,pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)

train_loader, test_loader = dataloader.dataloader(train_data, test_data, dataloader_args)

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
print(device)
model = model.Net().to(device)
summary(model, input_size=(1, 28, 28))


optimizer = optim.SGD(model.parameters(), lr=0.015, momentum=0.9)
# scheduler = StepLR(optimizer, step_size=6, gamma=0.01)
scheduler = OneCycleLR(optimizer, max_lr=0.015,epochs=15,steps_per_epoch=len(train_loader))


# train(model, device, train_loader, optimizer,scheduler, train_losses, train_acc):
# test(model, device, test_loader, test_losses, test_acc):

train_losses = []
test_losses = []
train_acc = []
test_acc = []

EPOCHS = 15

for epoch in range(EPOCHS):
    print("EPOCH:", epoch)
    train(model, device, train_loader, optimizer, scheduler, train_losses, train_acc)
    test(model, device, test_loader, test_losses, test_acc)



plot_matrics(train_losses,
            test_losses,
            train_acc,
            test_acc)