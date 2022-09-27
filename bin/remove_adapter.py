"""NAME
        remove_adapter.py
VERSION
        2.0

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Remove a specific adapter from DNA sequences contained in a .txt file

CATEGORY
        DNA

USAGE
        Use it to open a txt file containing DNA sequences and remove the adapters from them.
        The resulting sequences will be saved as a new file

ARGUMENTS

"""
# Open the desired file
file_name= input("Type the directory path to the desired file\n Example: ../source/file_sequence.txt \n")
open_file= open("{}".format(file_name),"rt")
file = open_file.read()
# Separate each element divided by a "\n", so they don't appear in the list
seq = file.split("\n")
print("The lengths of the entered sequences are:")
# Creates the output file
new_file= open("DNA_sequence_no_adapters.txt","w+")
# A for loop to iterate "line" number of times
for line in seq:
    # Erase the specified adapter from each DNA sequence, all of them must have the same adapter length
    sequences = line[14:]
    # Counting the number of nucleotides remaining after the cut
    length = len(sequences)
    # Print the end result
    print(length)
    # Writes each sequence in the new file
    new_file.write("\n{}".format(sequences))
print("The new file was created successfully in the same directory as this script as: "
      "DNA_sequence_no_adapters.txt ")