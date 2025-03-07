from cifar10_label_mapper import cifar10_labels
import numpy as np
import matplotlib.pyplot as plt
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

def load_cifar_data():
    # Load CIFAR10 data
    transform = transforms.Compose([transforms.ToTensor()])
    train_data = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    test_data = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

    # Create dataloaders
    #trainloader = DataLoader(train_data, batch_size=64, shuffle=True)
    #testloader = DataLoader(test_data, batch_size=64, shuffle=False)

    return train_data, test_data

if __name__ == "__main__":
    trainset, testset = load_cifar_data()
    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    testloader = DataLoader(testset, batch_size=64, shuffle=False)
    image, label = trainset[0]
    print(f"image shape: {image.size()}")
    labels = cifar10_labels()
    plt.title(labels[label])
    plt.imshow(image.permute(1, 2, 0))
    plt.show()
