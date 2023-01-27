import torch
from torchvision import datasets, transforms

def image_augmentations():

    train_transforms = transforms.Compose([
                                        transforms.ToTensor(),
                                        transforms.RandomAffine(degrees=7, shear=10, translate=(0.1, 0.1), scale=(0.8, 1.2)),
                                        transforms.RandomRotation((-7.0, 7.0), fill=(1,)),
                                        transforms.Normalize((0.1307,), (0.3081,)) # The mean and std have to be sequences (e.g., tuples), therefore you should add a comma after the values. 
                                        # Note the difference between (0.1307) and (0.1307,)
                                        ])

    # Test Phase transformations
    test_transforms = transforms.Compose([
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.1307,), (0.3081,))
                                        ])

    return train_transforms, test_transforms

def download_train_test(train_transforms, test_transforms):

    train = datasets.MNIST('./data', train=True, download = True, transform=train_transforms)
    test = datasets.MNIST('./data', train=False, download=True, transform=test_transforms)

    return train, test

def dataloader(train, test, dataloader_args):
    # train dataloader
    train_loader = torch.utils.data.DataLoader(train, **dataloader_args)

    # test dataloader
    test_loader = torch.utils.data.DataLoader(test, **dataloader_args)

    return train_loader, test_loader
