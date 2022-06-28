import sys
from Bio import SeqIO
from numpy import record
from yaml import load

def load_data(path):
    return SeqIO.read(path, 'genbank')

def composition(seq):
    dict = {}
    for amino in sorted(set(seq)): dict[amino] = 0
    for amino in seq: dict[amino] += 1
    return dict


def main():
    path = sys.argv[1]
    record = load_data(path)

    print(record.description)
    print(len(record.seq))
    print(composition(record.seq))

    # METHODS
    #print(record.seq)
    #print(record.id)
    #print(record.name)
    #print(record.description)
    #print(record.letter_annotations)
    #print(record.annotations)
    #print(record.features)
    #print(record.dbxrefs)


if __name__ == '__main__':
    main()