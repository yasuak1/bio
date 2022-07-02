#from functools import cache
from gettext import dpgettext
import sys, os
import io
import matplotlib.pylab as plt
import pickle
import numpy as np
import cv2
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

def make_img(cnt, line, dpoints):
    family, array = line.split()
    family = int(family)
    x_points, y_points = calc_points(array, dpoints)
    fig = plt.figure()
    plt.axis("off")
    plt.plot(x_points, y_points)
    #plt.show()
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
    cnt = 0
    dpoints = calc_dpoints()
    dict = {}
    img_data = np.empty(0)
    label = np.empty(0)
    for line in file.readlines():
        if cnt == 1: break
        family, img = make_img(cnt, line, dpoints)
        img_data = np.append(img_data, img)
        label = np.append(label, family)
        cnt += 1
    dict['img_data'] = img_data
    dict['label'] = label
    file.close()

    if train_data: np.save('/home/mizuno/data/neural_data/train', dict)
    else: np.save('/home/mizuno/data/neural_data/test', dict)

if __name__ == '__main__':
    # OPEN FILE
    main(train_data=True)
    main(train_data=False)
