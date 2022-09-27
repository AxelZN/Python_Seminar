import sys


def at_content(line):
        # Counting the AT content
        a_content = line.count("a")
        t_content = line.count("t")
        at_content = a_content + t_content
        # Obtaining the length of the sequence
        sequencelength = len(line)
        result = (at_content / sequencelength) * 100
        return round(result)

def get_sequence(file_path):
    secuencia = ""
    with open(file_path) as file_handler:
        for line in file_handler:
            secuencia = line
            print(at_content(secuencia))

arguments = sys.argv
file_path = arguments[1]
