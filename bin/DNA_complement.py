'''NAME
       DNA Complement

VERSION
        0.5

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
sequence=open("file_sequence.txt","rt")
complement=sequence.read()
print("The entered sequence is: ")
print(complement)
print("The complement of the sequence is: ")
for char in complement:
	if char=="A":
		print("T",end="")
	elif char=="T":
		print("A",end="")
	elif char=="G":
		print("C",end="")
	elif char=="C":
		print("G",end="")
print("\n\nThe reverse complement of the sequence is: ")
for char in reversed(complement):
	if char=="A":
		print("T",end="")
	elif char=="T":
		print("A",end="")
	elif char=="G":
		print("C",end="")
	elif char=="C":
		print("G",end="")
		
#Closing the file
sequence.close()