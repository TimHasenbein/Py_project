# DNA SEQUENCE CHARACTERISATION
#### Video Demo:  https://youtu.be/7ak2niLc0RQ
#### Description:
The project 'DNA sequence characterisation' contain s two files, project.py and the test_project.py file for unit testing.
The program takes a string as input that is composed of the four bases A, T, C, G in a case insenitive manner.
If desired, the user can also input a motif of interest for a look-up in the sequence.
The output is a characterisation of the input sequence and includes:
    1. Then length of the input sequence.
    2. The percentage of GC-content.
    3. The molecular weight in g/mol.
    4. The reverse complementary sequence.
    5. If the sequence includes a protein-coding sequence with a start codon it will output the corresponding aminoacid sequence after translation.
    6. If entered the position at which the input motif was found.

## FUNCTIONS
### check_sequence(sequence):
Checks if there is input snd if so, if the sequence is consisting of the four bases A,T,C,G only.
If not the program will exit and return 'Invalid sequence'.

### characterize(sequence):
Characterises the input sequence. Calculates the length of the sequence, as well as the GC content and the molecular weight.

### complement(sequence):
Returns the complementary sequence to the input sequence.

### translation(sequence):
Looks for a start codong in the input sequence and if so gets the corresponding aminoacids for each triplet.
Stops if a stop codon is reached in the sequence.
If there is no stop codon, the program will assume a non-coding sequence and not return the protein sequence.

### motif_search(sequence, motif):
If entered the program will look for the motif of interest in the sequence and returns the position(s) as list.

