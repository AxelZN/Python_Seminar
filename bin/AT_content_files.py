'''NAME
       AT_content_files

VERSION
        

AUTHOR
        Axel zagal Norman

DESCRIPTION
        Script for obtaining the AT content of several DNA sequences inside a file

CATEGORY
		DNA

USAGE
		

ARGUMENTS
		
'''
open_file=open("../source/myoglobin.txt")
file=open_file.readlines()
#3 Iterate trough the file one line at a time
for gene_data in file:
# Remove the new line characters
	gene_data=gene_data.rstrip()
# Get the sequence from each line
	gene_data=gene_data.split(",")
#Counting the AT content
	A_content=gene_data.count("A")
	T_content=gene_data.count("T")
	AT_content=A_content+T_content
#Obtaining the length of the sequence
	sequencelength=len(gene_data)
	result=(AT_content/sequencelength)+100
	print(result)
