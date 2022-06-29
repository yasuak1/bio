import numpy as np

if __name__ == '__main__':
    data = np.load('train_data.pkl', allow_pickle=True)
    for key in data:
        print(data[key].shape)