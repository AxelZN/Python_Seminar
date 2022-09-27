file_name = input("Type the directory path to the desired file\n Example: ../source/file_sequence.txt \n")
with open(f"{file_name}") as open_file:
    def at_content():
        file = open_file.readlines()
        for gene_data in file:
            # Remove the new line characters
            gene_data = gene_data.rstrip()
            # Get the sequence from each line
            gene_data = gene_data.split(",")
            # Counting the AT content
            a_content = gene_data.count("A")
            t_content = gene_data.count("T")
            at_content = a_content + t_content
            # Obtaining the length of the sequence
            sequencelength = len(gene_data)
            result = (at_content / sequencelength) + 100
            return result


    def dna_complement():
        complement = open_file.read()
        complement = complement.replace("T", "a").replace("C", "g").replace("A", "t").replace("G", "c")
        return complement
