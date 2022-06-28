import sys, os
from matplotlib.cbook import delete_masked_points

from yaml import load
sys.path.append(os.pardir)
import math
import copy
from part02.tutorial_biopython import load_data
from prc.plot_non_weighted import calc_dpoints

def calc_weight():
    lseq = 0
    cnt_amino = {}
    amino_weight = {}
    with open('../data/composition.dat') as f:
        for l in f.readlines():
            key, val = l.split()
            val = float(val)
            cnt_amino[key] = val
            lseq += val
    for key in cnt_amino:
        amino_weight[key] = - math.log(cnt_amino[key] / lseq, 10)
    return amino_weight

def calc_weighted_points(seq, dpoints, amino_weight):
    points = []
    points.append([0, 0])
    latest_point = [0, 0]
    for amino in seq:
        latest_point[0] += amino_weight[amino] * dpoints[amino][0]
        latest_point[1] += amino_weight[amino] * dpoints[amino][1]
        points.append(copy.copy(latest_point))
    return points

def main():
    path = sys.argv[1]
    record = load_data(path)
    dpoints = calc_dpoints(record.seq)
    amino_weight = calc_weight()
    points = calc_weighted_points(record.seq, dpoints, amino_weight)
    for point in points:
        print(str(point[0]) + " " + str(point[1]))


if __name__ == '__main__':
    main()