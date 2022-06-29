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
    dict = {}
    cnt = 0
    img_data = np.empty(0)
    y_train = np.empty(0)
    #path = '/home/yasu/bio/data/'
    #dict = get_data(path)
    dict = get_data('')
    for key in dict:
        if cnt == 10: break
        #print(key + ' ' + dict[key])
        #img_path = path + key + '.png'
        img_path = 'train/' + key + '.png'
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #print(img.shape)
        img_data = np.append(img_data, img)
        y_train = np.append(y_train, dict[key])
        cnt += 1
    img_data = img_data.reshape(cnt, 1, 480, 640)
    print(img_data.shape)
    #np.save('train', img_data)
    data['x_train'] = img_data
    data['y_train'] = y_train
    #np.save('train', data)
    #np.save('test', data)
    with open("train_data.pkl", "wb") as tf:
        pickle.dump(data, tf)

if __name__ == '__main__':
    main()