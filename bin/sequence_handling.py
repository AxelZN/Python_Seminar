"""
NAME
        Sequence_handling.py

VERSION
        1.4

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Script for doing various things with DNA, RNA, and Protein sequences.
        Only plain text and FASTA files are supported
        Functions included:
            AT content calculator
            Reverse complement of DNA sequence
            Transcription of DNA sequence
            Translation of DNA/RNA sequence
            Aminoacid counter for protein sequences

CATEGORY
        DNA

USAGE
        Execute in terminal, a file, the sequence type, and at least one function are required.
        Example: python sequence_handling.py --file_path ../source/sequence.txt --seq_type DNA --at_content yes
        at_content: calculates the percentage of the sequence made up of Adenine and Thymine.
        rev_complement: determines the lagging strand sequence based on your sequence.
        transcribe: turns a DNA sequence into a RNA sequence.
        translate: Turns a RNA sequence into an amin oacid sequence.
        amino_acid_counter: Counts how many times each amino acid appears in the sequence.

ARGUMENTS
        --file path: Used for the relative path of the file containing the DNA sequence.
        --seq_type: determines the type of sequence that will be used.
        The next arguments will call said function if value is "yes"
        --at_content: used to call at_content function.
        --rev_comp: used to call reverse_complement function.
        --transcribe: used to call the transcribe function.
        --translate: used to call the translate function.
        --aa_counter: used to call the amino_acid_counter function.
"""

import argparse

# argument parser
parser = argparse.ArgumentParser(description="")
parser.add_argument("--file_path", dest="input", type=str, metavar="text",
                    help="Relative path to the file you want to open")
parser.add_argument("--seq_type", dest="seq_type", type=str, metavar="DNA/RNA/PROTEIN",
                    help="Type what kind of sequence you are going to use")
parser.add_argument("--at_content", dest="function_1", type=str, metavar="yes",
                    help="Type yes if you want this function to be included in this run, exclusive to DNA")
parser.add_argument("--rev_comp", dest="function_2", type=str, metavar="yes",
                    help="Type yes if you want this function to be included in this run, exclusive to DNA")
parser.add_argument("--transcribe", dest="function_3", type=str, metavar="yes",
                    help="Type yes if you want this function to be included in this run, exclusive to DNA")
parser.add_argument("--translate", dest="function_4", type=str, metavar="yes",
                    help="Type yes if you want this function to be included in this run, not compatible with PROTEIN")
parser.add_argument("--aa_counter", dest="function_5", type=str, metavar="yes",
                    help="Type yes if you want this function to be included in this run")

args = parser.parse_args()


def at_content(sequence):
    """
    :param sequence: sequence being used
    :return: at percentage
    """
    global functions_called
    a_content = sequence.count("A")
    t_content = sequence.count("T")
    at_content = (a_content + t_content) / (len(sequence)) * 100
    functions_called += 1
    print("AT and CG content are:")
    return at_content.__round__(4), 100 - at_content.__round__(4)


def reverse_complement(sequence):
    """
    :param sequence: sequence being used
    :return: reverse sequence complementary to the entered one
    """
    global functions_called
    functions_called += 1
    # The sequence gets stored from end to start
    reverse = sequence[::-1]
    # Each letter is replaced by their watson-crick counterpart
    lower_case = reverse.replace("T", "a").replace("C", "g").replace("A", "t").replace("G", "c")
    rev_complement = (lower_case.upper())
    new_file = open(f"reverse_complement.txt", "w+")
    new_file.write(rev_complement)
    return rev_complement


def transcribe(sequence):
    """
    :param sequence: sequence being used
    :return: DNA sequence turned into RNA
    """
    global functions_called
    functions_called += 1
    # thymine gets turned into uracil
    rna = sequence.replace("T", "U")
    new_file = open(f"sequence_transcription.txt", "w+")
    new_file.write(rna)
    return rna


def translate(sequence, protein_sequence):
    """
    :param sequence: sequence being used
    :param protein_sequence: stores the amino acid sequence being generated
    :return: amino acid sequence based on the RNA transcript
    """
    global functions_called
    functions_called += 1
    # determines if sequence needs to be transcribed based on it´s type
    if seq_type == "DNA":
        rna = transcribe(sequence)
    else:
        rna = sequence
    n = 3
    # The sequence gets saved into a list with each element being three letters long
    codons = [(rna[i:i + n]) for i in range(0, len(rna), n)]
    for elements in codons:
        if elements in genetic_code:
            protein_sequence += genetic_code[elements]
    new_file = open(f"sequence_translation.txt", "w+")
    new_file.write(protein_sequence)
    return protein_sequence


def amino_acid_counter(sequence):
    """
    :param sequence: sequence being used
    :return: prints the complete amino acid dictionary
    """
    global functions_called
    functions_called += 1
    # Determines if sequence needs to be translated based on it's type
    if seq_type != "PROTEINS":
        aminoacids = sequence
    else:
        aminoacids = translate(sequence, protein_sequence)
    # each appearance of the codons gets counted and added to the dictionary
    for elements in aminoacids:
        all_amino_acids[elements] = aminoacids.count(elements)
    for key, value in all_amino_acids.items():
        if value > 0:
            print(key, "was found", value, "times")
    return


genetic_code = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
                "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

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

with open(f"{args.input}") as file_name:
    # seq_type gets turned into uppercase, so the user can write it however they want
    seq_type = args.seq_type.upper()
    file = file_name.readlines()
    untrimmed_seq = ""
    protein_sequence = ""
    # skips headline
    for lines in file[1:]:
        untrimmed_seq += lines.rstrip()
    sequence = untrimmed_seq
    # if sequence type is protein, translation is skipped
    if seq_type == "PROTEIN":
        protein_sequence = untrimmed_seq
    functions_called = 0

if args.function_1 == "yes":
    if seq_type != "DNA":
        print("This function is incompatible with your sequence type")
    else:
        print("\n\n")
        print(at_content(sequence))

if args.function_2 == "yes":
    if seq_type != "DNA":
        print("This function is incompatible with your sequence type")
    else:
        reverse_complement(sequence)

if args.function_3 == "yes":
    if seq_type == "DNA":
        print("This function is incompatible with your sequence type")
    else:
        transcribe(sequence)

if args.function_4 == "yes":
    if seq_type != "PROTEIN":
        print("This function is incompatible with your sequence type")
    else:
        translate(sequence, protein_sequence)

if args.function_5 == "yes":
    print("\n")
    amino_acid_counter(sequence)

try:
    if functions_called > 0:
        print(f"Successfully used {functions_called} functions")
except:
    if functions_called == 0:
        print("Function arguments missing")
