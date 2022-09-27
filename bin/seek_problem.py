"""NAME
    seek_problem.py

VERSION
    0.1

AUTHOR
        Axel Zagal Norman <azagal@lcg.unam.mx>

DESCRIPTION


CATEGORY
    DNA

USAGE


ARGUMENTS

"""
# Abrir archivo
open_file= open()
file= open_file.read()
# Recorrer archivo línea por línea
while True:
    line= file.readline()
# Ignorar líneas que son encabezado
    if line.startswith("#"):
        continue
# Generar una lista con los elementos de cada línea
gene_data=
# Obtener el tipo de gen
# Ignorar genes que no sean del tipo gene
    if gene_sequence != "gene":
    continue
# Determinar si la secuencia existe
gene_sequence= gene_data[1]
    if gene_sequence is None or gene_sequence== "":
    continue
# Determinar si la secuencia está en dirección forward o reverse
gene_strand= gene_data[5]
# Si es reverse calcular su reverso complementario
    if gene_strand.lower() == "reverse":
    gene_sequence=gene_sequence[::-1]
    gene_sequence=gene_sequence.replace("A","t").replace("T","a").replace("C","g").replace("G","C")
# Calcular contenido de AT
# Guardar el resultado en un nuevo archivo
# Cerrar ambos archivos
