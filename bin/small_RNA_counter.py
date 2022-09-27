'''
NAME
        small_RNA_counter.py

VERSION
        1.0

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION
        Open a file containing sRNA sequences and know which ones are larger than 300pb,
        print their names and their length.

CATEGORY
        RNA

USAGE
        Open a file that contains genes and create a file with only the genes that are larger than 300 bp.
        The file must be in the same directory as this script

ARGUMENTS

'''
# Open the file, the with function doesn´t need to close files
name = input("Type the name of the desired file\n")
with open("{}".format(name)) as file:
    # Read the file one line at a time
    gene_data = file.readlines()
# Create the output file
new_file= open("sRNA_genes_Ecoli.txt","w+")
# Iterate over each line of the file
numberofgenes=0
for line in gene_data:
    each_line = line.split("\t")
    # Iterate over each element of the the line
    for element in each_line:
        seq_length = len(element)
        # If an element of the line is longer than 300, it gets printed alongside with the name of the gene it belongs
        if seq_length>300 and each_line[5]=="small RNA":
            print(each_line[1],seq_length, each_line[5])
            new_file.write("{}\n{}\n".format(each_line[1],element))
            numberofgenes+=1
print("\nThe number of sRNAs found was {}".format(numberofgenes))
print("The file was created successfully under the name sRNA_genes_Ecoli.txt")