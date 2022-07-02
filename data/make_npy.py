from operator import ge
import pickle
import numpy as np
import cv2

def get_data(path):
    dict = {}
    with open(path + 'train.pkl', 'rb') as tf:
    #with open(path + 'test.pkl', 'rb') as tf:
        dict = pickle.load(tf)
    return dict

def main():
    data = {}
    cnt = 0
    img_data = np.empty(0)
    y_train = np.empty(0)
    dict = get_data('')
    for key in dict:
        if cnt == 100: break
        img_path = '/home/mizuno/data/neural_data/train_png/' + key + '.png'
        #img_path = '/home/mizuno/data/neural_data/test_png/' + key + '.png'
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255
        img_data = np.append(img_data, img)
        y_train = np.append(y_train, dict[key])
        cnt += 1

    input_size = 480 * 640
    img_data = img_data.reshape(cnt, 1, 480, 640)
    data['img_data'] = img_data
    data['label'] = y_train
    np.save('train', data)
    #np.save('test', data)

if __name__ == '__main__':
    main()