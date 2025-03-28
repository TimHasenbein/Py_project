##********************##
## Final Project CS50 ##
##********************##
## Project: CS50
## Tim Hasenbein
## Munich
## Last modification 12.2023
## Creation: 12.2023


#####------ set environment ------######
import re
import sys


#####------ main function ------######
def main():
    sequence = check_sequence(input('\nEnter your DNA sequence: ').upper())
    motif = input('\nEnter the motif to search: ').upper()
    if motif != "":
        match_positions = motif_search(sequence, motif)
    length, GC_content, molecular_weight = characterize(sequence)
    comp_sequence = complement(sequence)
    protein_seq = translation(sequence)
    # output
    print(f'\n-------- Characteristics: --------')
    print(f'Length: ' + '\033[0;36m' + f'{length}bp' + '\033[0m')
    print('GC content: ' + '\033[91m' + f'{GC_content * 100:.2f}%' + '\033[0m')
    print(f'Molecular weight: ' + '\033[92m' + f'{molecular_weight} g/mol' + '\033[0m')
    print(f'Reverse complementary sequence:')
    for i in range(0, len(comp_sequence), 50):
        print('\033[93m' + comp_sequence[i:i+50] + '\033[0m')
    print(f'Protein sequence:')
    for i in range(0, len(protein_seq), 50):
        print('\033[94m' + protein_seq[i:i+50] + '\033[0m')
    if motif != "":
        if match_positions:
            print(f'Motif \033[0;95m{motif}\033[0m found at positions:', end = '')
            for position in match_positions:
                print(f' \033[0;95m{position}\033[0m', end = '')
            print()
        else:
            print(f'Motif "\033[0;95m{motif}\033[0m" not found in the sequence.')
    print(f'----------------------------------\n')


#####------ check input sequence for validity ------######
def check_sequence(sequence):
    if re.match("^[ATCG]*$", sequence) and sequence != "":
        return sequence
    else:
        sys.exit('Invalid sequence')


#####------ characterize sequence ------######
def characterize(sequence):
    length = len(sequence)
    GC_content = (sequence.count('G') + sequence.count('C'))/length
    nucleotide_weights = {'A': 135.13, 'T': 126.11, 'C': 111.1, 'G': 151.13}
    molecular_weight = sum(nucleotide_weights[base] for base in sequence)
    return length, GC_content, molecular_weight


#####------ get complementary sequence ------######
def complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp_sequence = ''.join(complement_dict[base] for base in sequence)
    return comp_sequence


#####------ translate sequence ------######
def translation(sequence):
    codon_table = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*STOP*', 'TAG': '*STOP*',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*STOP*', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    protein_sequence = ''
    started_translation = False
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if codon == 'ATG':
            started_translation = True
        if started_translation:
            if codon in codon_table:
                amino_acid = codon_table[codon]
                if amino_acid == '*STOP*':
                    started_translation = False
                else:
                    protein_sequence += amino_acid
    return protein_sequence


#####------ find motif ------######
def motif_search(sequence, motif):
    matches = re.finditer(motif, sequence)
    match_positions = [match.start() for match in matches]
    return match_positions


#####------ run main if main ------######
if __name__ == "__main__":
    main()

