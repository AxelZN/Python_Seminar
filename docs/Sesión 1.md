# Sesión de Unix

## Ejercicios de clase

**Comandos básicos**

Las opciones de comando son: 

- -h help
- -v version 



```python

```

| clear           | limpiar pantalla                                             |
| --------------- | :----------------------------------------------------------- |
| man             | manual                                                       |
| pwd             | donde estás                                                  |
| cd              | mover entre carpetas                                         |
| -F              | te muestra los archivos del directorio actual                |
| ls              | enlista los directorios dentro del directorio actual         |
| -a              | muestra todos los directorios, incluso los ocultos           |
| eedgt/gdg/ ljnj | para ir a un directorio específico debes teclear todo el path |
| cd ../..        | Sirve para ir hacia atrás más de un directorio               |
| -t              | ordena por fecha de modificación                             |
| *               | caracter comodín al momento de filtrar resultados            |
| ?               | sirve para sustituir un caracter que no conozcas cuando haces una búsqueda |
| cat             | permite ver el contenido de un archivo                       |
| less            | permite ver el contenido de un archivo en paginación         |
| history         | muestra un historial de los comandos utilizados en la sesión actual |
| head            | muestra las primeras líneas de un archivo                    |
| tail            | muestra las últimas líneas de un archivo                     |

Unix es un sistema operativo multiprocesos y multiusuarios desarrollado en la década de los 60, es muy importante para la bioinformática porque permite hacer muchas cosas útiles para la misma, como automatizar procesos repetitivos, haciendo que sea menos susceptible a errores, ya que la computadora puede repetir un proceso muchas veces sin equivocarse. También está la opción de cómputo en la nube, cuando una sola computadora no es suficiente para la tarea. Incluso hay herramientas bioinformáticas exclusivas de unix. 

Los directorios son las "carpetas" donde se almacenan los archivos, y cada directorio puede tener varios directorios dentro, permitiéndonos mover libremente entre estas "ramas", por eso, el comando tree muestra todas las ramas que hay en los directorios. 

La ruta absoluta es el camino que sigues hacia un directorio desde la root, mientras que la ruta negativa es la que sigues desde cualquier dispositivo conectado al mismo servidor. 