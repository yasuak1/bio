import sys, os
sys.path.append(os.pardir)
from Bio import SeqIO
from part02.tutorial_biopython import load_data, composition

def main():
    path = sys.argv[1]
    record = load_data(path)
    lseq = len(record.seq)
    dict = composition(record.seq)

    # DISP
    print("amino acid\tcnt\tratio")
    for amino in dict:
        print(amino + "\t\t" + str(dict[amino]) + "\t" + str(dict[amino]/lseq))

if __name__ == '__main__':
    main()