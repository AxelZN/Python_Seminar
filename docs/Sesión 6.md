# **Sesión 6**

# Funciones



Don't repeat yourself

*print()*
*input()*
*len()*

````python
def hello world():`
	`print("Hello World")`

hello world()
````

<u>Parámetros vs Argumentos</u>

````python
`def hello_message(name):`
	`print(f"hello {name}!")`

`hello_message ("Emilio")
````

<u>Default parameters vs keyword parameters</u>
keyword parameters:
`def hello_message (name, last_name):`
	print (f"hello {name} {last_name}!")

`hello_message (name="Emilio, last_name= Peña")`

Default parameters:
`def hello_message (name= "Alumno" , last_name= "UNAM")`:
	`print(f"hello {name} {last_name}")`

`hello_message("Emilio")`
`#> hello Emilio UNAM`

**Return**
`def suma (number_1, number_2):`
	`number_1 + number_2`

`print (suma(2,5)) 

no hace nada, por otro lado:

````python
def suma (number1, number2):`
	`resultado = number1 + number2` 
	`return resultado`

`print(suma(2,5))
````

imprime 7

**Docstrings**

```python
def hello_world():`
	`'''`
	`prints hello world`
	`'''`
	`print("hello world")`

`print(hello_world-__doc__)
```

**Assert**: revisa si  algo es verdadero, de lo contrario arroja un mensaje de error personalizado, esto puede ser útil para comprobar si una función sirve correctamente 