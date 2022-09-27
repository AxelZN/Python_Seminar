'''NAME
       Open_file

VERSION
        1.0

AUTHOR
        Axel Zagal <azagal@lcg.unam.mx>

DESCRIPTION
        Script for reading a file in terminal

CATEGORY
		MISC

USAGE
		Run it and it will open a requested file
ARGUMENTS
'''

file=input("¿Que archivo quieres abrir?\n")
file=open("../source/{}".format(file),"r")
leyendo_archivo=file.read()
print(leyendo_archivo)