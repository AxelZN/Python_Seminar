# **Sesión 7**

Manejo de errores, importando módulos 

Excepciones: Errores no tan feos, sintaxis

Error handling; para el manejo de errores necesitamos: 

```` python
try: 
	#bloque de código
except: 
    #bloque de código que se ejecuta cuando ocurre un error
````

ejemplo: 

````python
numer1 = input
number2 = input

try: suma = int (number1) + int (number2)
    print(suma)
except: 
    print ("no se pudo hacer la suma")
````

else: se ejecuta algo cuando sí sirvió el try

finally: se ejecuta si ocurre o no ocurre un error

```` python
try:
    #código
except:
    #Código que se ejecuta cuando no se pudo el try
else:
    # código que se ejecuta cuando sí ocurre el primer código
finally:
    # código que se ejecuta si ocurre o no un error
````

Easier to ask for forgiveness than permission: intentar algo en el código, si se pudo, bien, de lo contrario, arreglarlo
vs
Look before you leap: checar si se puede hacer algo en el código, hacer que se pueda, luego hacerlo

Mejorando nuestras funciones con manejo de errores

# **Importando módulos** 

Puedes importar módulos para tener funcionalidades adicionales en tus códigos, usualmente se escriben hasta arriba del código

Se recomienda escribirlas de la siguiente manera:
-módulos estándar
-módulos de terceros
-módulos locales

se recomienda: 

```` python
import random
random.randint()

#no se recomienda:
from random import randint
randint()
````

**Formas de importar nuestros módulos**

