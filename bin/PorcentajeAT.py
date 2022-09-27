'''NAME
       Porcentaje AT

VERSION
        2.0

AUTHOR
        Axel Zagal <azagal@lcg.unam.mx>

DESCRIPTION
        Programa para conocer el porcentaje de AT en una secuencia de ADN

CATEGORY
		DNA

USAGE
		Introduzca una secuencia de ADN y el script calculará qué porcentaje de la misma está compuesto por As y Ts
ARGUMENTS
		-seq es la variable donde se almacenará la string correspondiente a la secuencia de ADN
		-nA es el número de veces que aparece el caracter "A"
		-nT es el número de veces que aparece el caracter "T"
		-percent es donde se guardará el resultado de la operación matemática
'''
sequence=input("Introduzca la secuencia de ADN, no importa si son mayúsculas o minúsculas\n").upper()# toda la string se convierte a mayúsculas

cantidadA=seq.count("A")
cantidadT=seq.count("T")
# La función .count cuenta cuántas veces aparece este caracter

percent=(cantidadA+cantidadT)/len(sequence)*100
# len sirve para obtener la longitud de una cadena, vital para obtener el porcentaje
print("El porcentaje de AT en la secuencia introducida es {}%".format(percent))