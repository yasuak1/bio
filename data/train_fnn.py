import numpy as np

if __name__ == '__main__':
    data = np.load('test.npy', allow_pickle=True)
    print(data['x_test'])