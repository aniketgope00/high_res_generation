def cifar10_labels():
    labels = { 0: 'airplane',
               1: 'automobile',
               2: 'bird',
               3: 'cat',
               4: 'deer',
               5: 'dog',
               6: 'frog',
               7: 'horse',
               8: 'ship',
               9: 'truck'}
    return labels

if __name__ == "__main__":
    labels = cifar10_labels()
    for key in labels.keys():
        print(f"{key}: {labels[key]}")