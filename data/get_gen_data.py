from functools import cache
from gettext import dpgettext
import sys, os
import matplotlib.pylab as plt

from numpy import flip
from yaml import load
sys.path.append(os.pardir)
from biopython.part02.tutorial_biopython import load_data, composition
from biopython.prc.plot_non_weighted import calc_dpoints, calc_points

def main():
    dpoints = calc_dpoints()
    file = open('/home/yasu/data/COG-100-2892/dataset0/train.txt')
    cnt = 0
    for line in file.readlines():
        fig = plt.figure()
        ax = fig.add_subplot(111, xlabel='x', ylabel='y')
        if cnt == 10: break
        family, arry = line.split()
        #print(arry)
        x_point, y_points = calc_points(arry, dpoints)
        plt.plot(x_point, y_points)
        plt.savefig(family + "-" + str(cnt))
        cnt += 1

if __name__ == '__main__':
    main()