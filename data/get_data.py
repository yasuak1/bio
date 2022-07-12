#from functools import cache
from gettext import dpgettext
import sys, os
import io
import matplotlib.pylab as plt
import pickle
import numpy as np
import cv2
import pandas as pd
from PIL import Image
#from regex import F
from rsa import PublicKey
from yaml import load
sys.path.append(os.pardir)
from biopython.part02.tutorial_biopython import load_data, composition
from biopython.prc.plot_non_weighted import calc_dpoints, calc_points

def open_file(path):
    f = open(path)
    return f

def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img

def make_img(line, dpoints, name):
    family, array = line.split()
    family = int(family)
    x_points, y_points = calc_points(array, dpoints)

    fig = plt.figure(figsize=(0.6, 0.6))
    plt.axis("off")
    plt.plot(x_points, y_points, lw=0.5)
    #plt.show()
    fig.savefig(name)
    img = cv2.cvtColor(np.array(fig2img(fig)), cv2.COLOR_BGR2GRAY) / 255
    plt.close()
    return family, img


def main(train_data=True):
    # OPEN FILE
    path = ''
    if train_data: path = '/home/mizuno/data/amino_data/COG-100-2892/dataset0/train.txt'
    else :path = '/home/mizuno/data/amino_data/COG-100-2892/dataset0/test.txt'
    file = open_file(path)

    # PRODUCE IMAGES
    max_cnt = 0
    if train_data: max_cnt = 3
    else: max_cnt = 3
    cnt = 0
    input_size = 60 * 60
    dpoints = calc_dpoints()
    dict = {}
    img_data = np.empty(0)
    label = np.empty(0)
    for line in file.readlines():
        if max_cnt == cnt: break
        if cnt % 100 == 0: print(cnt)
        if train_data: name = "train_img_" + str(cnt)
        else: name = "test_img_" + str(cnt)
        family, img = make_img(line, dpoints, name)
        img_data = np.append(img_data, img)
        label = np.append(label, family)
        cnt += 1
    img_data = img_data.reshape(max_cnt, input_size)
    dict['img_data'] = img_data
    dict['label'] = label
    file.close()

    #if train_data: np.savez_compressed('/home/mizuno/data/neural_data/train', dict)
    #else: np.savez_compressed('/home/mizuno/data/neural_data/test', dict)
    save_path = ''
    if train_data: save_path = '/home/mizuno/data/neural_data/size_train.pkl'
    else: save_path = '/home/mizuno/data/neural_data/size_test.pkl'
    pd.to_pickle(dict, save_path, compression='zip', protocol=4)
    #pd.to_pickle(dict, save_path, protocol=4)

if __name__ == '__main__':
    # OPEN FILE
    main(train_data=True)
    main(train_data=False)
