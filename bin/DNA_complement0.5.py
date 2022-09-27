'''NAME
       DNA Complement

VERSION
        2.0

AUTHOR
        Axel Zagal <azagal@lcg.unam.mx>

DESCRIPTION
        Script for obtaining the complementary bases of a DNA sequence

CATEGORY
		DNA

USAGE
		Run it and it will obtain the complementary sequence, the file "file_sequence.txt" must be in the same directory as this script
ARGUMENTS
'''

#Open file
sequence=open("../source/file_sequence.txt","rt")
complement=sequence.read()
complement=complement.replace("T","a").replace("C","g").replace("A","t").replace("G","c")
print(complement.upper())
#Closing the file
sequence.close()