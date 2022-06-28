import sys, os
from jsonschema import draft201909_format_checker
from matplotlib.cbook import delete_masked_points
from sympy import re

from yaml import load
sys.path.append(os.pardir)
from Bio import SeqIO
import math
import copy
from part02.tutorial_biopython import load_data, composition

def calc_dpoints(seq):
    dpoints = {}
    arg = 0
    darg = 360 / len(set(seq))
    for amino in sorted(set(seq)):
        x = math.cos(math.radians(arg))
        y = math.sin(math.radians(arg))
        dpoints[amino] = [x, y]
        arg += darg
    return dpoints

def calc_points(seq, dpoint):
    points = []
    points.append([0, 0])
    latest_point = [0, 0]
    for amino in seq:
        latest_point[0] += dpoint[amino][0]
        latest_point[1] += dpoint[amino][1]
        points.append(copy.copy(latest_point))
    return points


def main():
    path = sys.argv[1]
    record = load_data(path)
    amino_weight = {}
    dpoints = calc_dpoints(record.seq)
    points = calc_points(record.seq, dpoints)
    for point in points:
        print(str(point[0]) + " " + str(point[1]))


if __name__ == '__main__':
    main()