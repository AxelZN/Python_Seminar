"""
NAME
        Gene_Class_creating.py

VERSION
        1.0

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Creates a class that can be instanced in gene objects and gets the at content and transcription product
        of that gene.

CATEGORY
        DNA

USAGE
        Run the program with the argument --file_path and the relative path to a file containing a gene sequence.

ARGUMENTS
        --file_path: Type the relative path to a gene sequence
"""
import argparse


class Gene:
    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location

    def __str__(self):
        return f"Introduced object= name: {self.name}, type: {self.type}, location: {self.location}"

    @staticmethod
    def get_atcontent(file_sequence):
        at_content = ((file_sequence.count("A") + file_sequence.count("T")) / len(file_sequence)) * 100
        return at_content

    @staticmethod
    def transcribe(file_sequence):
        rna_sequence = file_sequence.replace("T", "U")
        return rna_sequence


# argument parser
parser = argparse.ArgumentParser(description="")
parser.add_argument("--file_path", dest="input", type=str, metavar="text",
                    help="Relative path to the file you want to open")

args = parser.parse_args()

gene = Gene("CFTR", "exon", "7q31.2")

with open(f"{args.input}") as file_name:
    file_sequence = file_name.read()
    setattr(gene, "sequence", file_sequence)

print(gene, (gene.get_atcontent(file_sequence)), (gene.transcribe(file_sequence)))
