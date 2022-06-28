#from functools import cache
from gettext import dpgettext
import sys, os
import matplotlib.pylab as plt
import pickle
from numpy import flip
#from regex import F
from rsa import PublicKey
from yaml import load
sys.path.append(os.pardir)
from biopython.part02.tutorial_biopython import load_data, composition
from biopython.prc.plot_non_weighted import calc_dpoints, calc_points

def main():
    dict = {}
    dpoints = calc_dpoints()
    #path = '/home/yasu/data/COG-100-2892/dataset0/'
    path = '/home/mizuno/data/COG-100-2892/dataset0/'
    #file = open(path + 'train.txt')
    file = open(path + 'test.txt')
    cnt = 0
    for line in file.readlines():
        fig = plt.figure()
        ax = fig.add_subplot(111, xlabel='x', ylabel='y')
        if cnt == 1000: break
        family, arry = line.split()
        #print(arry)
        x_point, y_points = calc_points(arry, dpoints)
        plt.plot(x_point, y_points)
        filename = str(cnt) + "-" + family
        plt.savefig(filename)
        plt.close()
        dict[filename] = family
        cnt += 1
    #with open("train.pkl", "wb") as tf:
    with open("test.pkl", "wb") as tf:
        pickle.dump(dict, tf)
    #print(dict)


if __name__ == '__main__':
    main()