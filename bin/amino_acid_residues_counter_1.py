"""
NAME
        amino_acid_residues_counter

VERSION
        1.0

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Obtain the number of appearances of a desired amino acid inside a file containing a protein sequence in
        FASTA or RAW format

CATEGORY
        Proteins

USAGE
        Enter the name of a file and the desired amino acid and the program will print the number of times it appears,
        its length and the percentage of the sequence made up of that amino acid. The protein sequence must be in the
        same directory as this script

ARGUMENTS

"""
file_name = input("Type the name of the file containing the protein sequence\n")
amino_acid = input("Type the code for the desired amino acid. Example: M, P, L\n")
# Turns the amino acid code into uppercase regardless of what the user typed
amino_acid = amino_acid.upper()
# Checks if the amino acid is a valid string
assert isinstance(amino_acid, str), "Amino acid not in valid type"

def amino_acid_counter(file_name, amino_acid):
    """
    :param file_name:
    :param amino_acid:
    :return: percentage
    """
    # Opens file using with
    with open(f"{file_name}") as file:
        sequence = file.read()
        # Divides the file into a list using new lines as a division
        sequence = sequence.split("\n")
        # Ignores the first line of FASTA and RAW formats
        sequence = ', '.join(sequence[1:])
        # Checks if the sequence is empty
        assert len(sequence) != 0, "sequence is empty"
        appearances = sequence.count(f"{amino_acid}")
        # Calculates the percentage of the protein composed by the amino acid
        percentage = round(((appearances / len(sequence)) * 100), 2)
        print(f"{amino_acid} has appeared {appearances} times among {len(sequence)} amino acids")
    return percentage

print(f"The protein is made up of {amino_acid} by {amino_acid_counter(file_name, amino_acid)}% ")