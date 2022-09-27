"""
NAME
        amino_acid_residues_counter.py

VERSION
        3.0

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Obtain the number of appearances of a desired amino acid inside a file containing a protein sequence in
        FASTA or RAW format using dictionaries.

CATEGORY
        Proteins

USAGE
        Type the path to the file containing the protein sequence, then tell the program which amino acids you want to
        search for in said sequence

ARGUMENTS


"""

all_amino_acids = {
    "A": 0,
    "R": 0,
    "N": 0,
    "C": 0,
    "E": 0,
    "Q": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "L": 0,
    "K": 0,
    "M": 0,
    "F": 0,
    "P": 0,
    "S": 0,
    "T": 0,
    "W": 0,
    "Y": 0,
    "V": 0,
    "X": 0,
}
# Ask for the file name
file_name = input("Type the relative path to the file containing the protein sequence.\n")
# Ask for amino acids to look for
wanted_amino_acids = input("Type the single letter code of the amino acids you want to search for.\n"
                           "Examples:\n ARNT\nw,v,p\n")
# Amino acids can be introduced in upper or lowercase
wanted_amino_acids = wanted_amino_acids.upper()
#  a list containing all the typed amino acids
amino_acids = list(wanted_amino_acids)

with open(f"../source/{file_name}") as file:
    # Create a list where each line of the file is an element
    sequence_lines = file.readlines()
    # Create a string containing all the lines of the file but the heading
    sequence = "".join(sequence_lines[1:])
    for amino_acid in amino_acids:
        if amino_acid in all_amino_acids:
            all_amino_acids[amino_acid] = sequence.count(amino_acid)

# Iterate through the dictionary to see which keys have a value other than zero and print them
for key, value in all_amino_acids.items():
    if value > 0:
        print(key, "was found", value, "times")