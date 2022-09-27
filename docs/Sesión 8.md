**Sesión 8 **

``````python
dna= "AATGATCGATCGTAATCGCCTAATATCGCATAGC"

trinucleotide_count = {}

for base1 in ["A", "T", "C", "G"]:
	for base2 in ["A", "T", "C", "G"]:
    	for base3 in ["A", "T", "C", "G"]:
            trinucleotide = base1 + base2 + base3
            trinucleotide_count[trinucleotide] = 
dna.count(trinucleotide)

for key in trinucleotide_count:
	if trinucelotide_count(trinucleotide) == 0:
        continue
    print(trinucleotide_count(key))
            


``````

**Diccionarios**
Nos permiten relacionar una llave con un valor

``````python
         key     value
gene = {"name" : "acaC"}
``````

sólo puede haber una llave de cada una

Puedes contar elementos repetidos, aumentando el valor de la llave
Si un elemento no se encuentra, puedes usar dict.setdefault(key, value)

**Métodos en diccionarios**
obteniendo el valor de una llave 

```` python
print dict(key)
````

obtener todas las llaves del diccinario

```` python 
keys = dict.keys()
````

agregando una llave

```` python
dict[key] = value
print (keys) #no se tiene que volver a hacer el método keys
````

eliminando una llave

```` python
dict = {key1, key2, key3}
del dict[key2]
````

recorriendo un diccionario

````python 
dict = {key1, key2 key3, key4}

for key in dict:
print (key)

for key in dict:
print (key, ->, dict[key])

for item in dict.items():
print (item)

for key, value in dict.items():
print (key, value)
````



**Listas dentro de diccionarios**

```` python
key = [key1, key2, key3]
value = [value1, valu2, value3]

dict = {}
dict ["key"] = key
dict ["key2"] = key2
#####
dict = {
    "key1" : key,
    "key2"  : key2
}

print (dict)

````

**Diccionarios dentro diccionarios**

```` python 
genes = {
    "araC" : "TACAGAT",
    "araD" : "CGATACGRA"
}
products = {
	
  "AraC": "MAEAQNDPLL",
	
  "CRP": "PGYSFNAHLV"
	
}
	
 	
ecoli = {}
	
ecoli["genes"] = genes
	
ecoli["products"] = products

print(ecoli)
````

