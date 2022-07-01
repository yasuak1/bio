import numpy as np

if __name__ == '__main__':
    data = np.load('train.npy', allow_pickle=True)
    print(type(data))
    print(type(data.item()))
    for key in data.item():
        print(key)
        print(data.item()[key])