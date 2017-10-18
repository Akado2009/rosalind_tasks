def translate(seq):
    RNA_CODON_TABLE = {
        'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
        'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
        'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
        'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
        'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
        'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
        'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
        'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
        'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
        'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
        'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
        'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
        'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
        'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
        'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
        'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }
    return ''.join([RNA_CODON_TABLE[seq[i : i + 3]] for i in range(0, len(seq), 3)])

import re

def get_max_orf(sequence):
    starts = [m.start() for m in re.finditer('ATG', sequence)]
    stops = [m.start() for m in re.finditer('TAG|TAA|TGA', sequence)]
    pairs = [(start, stop) for start in starts for stop in stops if (stop - start) % 3 == 0 and stop > start]
    max_pair = (1, 1)
    seen_starts = []
    for pair in pairs:
        if pair[0] not in seen_starts:
            if pair[1] - pair[0] > max_pair[1] - max_pair[0]: 
                max_pair = pair
                seen_starts.append(pair[0])
                
    return max_pair


def main(sequence):
    q = get_max_orf(sequence)
    print(translate(sequence[q[0] : q[1]].replace('T', 'U')))

if __name__ == '__main__':
    main('AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
