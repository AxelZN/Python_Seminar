'''NAME
       lectura_archivo

VERSION
        2.0

AUTHOR
        Axel Zagal <azagal@lcg.unam.mx>

DESCRIPTION
        Script for creating a file containing a DNA sequence

CATEGORY
		DNA

USAGE
		Run it and it will create said file
ARGUMENTS
'''

#Create file
file=open("archivo_secuencia.txt", "w+")
#Inseting the sequence in the file
file.write("ACTGATCGGCATGCATCATCGTGCGCATCGATGC")
#Closing the file
file.close()