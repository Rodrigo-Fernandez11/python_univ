# Modulo random en Python es 
# una libreria que permite generar numeros aleatorios y de realizar operaciones aleatorias como mezclar listas, elegir elementos al azar, etc.

# que es un modulo en python
# Un modulo en Python es un archivo que contiene definiciones y declaraciones de Python.
# Un modulo puede definir funciones, clases y variables, y puede incluir codigo ejecutable.
# Los modulos permiten organizar el codigo en partes mas pequeñas y reutilizables.

# ejemplo de modulo

# randint es una funcion del modulo random que genera un numero entero aleatorio entre dos limites especificos.
# Por ejemplo, si queremos generar un numero aleatorio entre 1 y 10, podemos usar la funcion randint de la siguiente manera:

import random
# Generar un numero aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Numero aleatorio entre 1 y 10: {numero_aleatorio}")
# Generar un numero aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print(f"Numero aleatorio entre 1 y 100: {numero_aleatorio}")
# Generar un numero aleatorio entre 1 y 1000
numero_aleatorio = random.randint(1, 1000)
print(f"Numero aleatorio entre 1 y 1000: {numero_aleatorio}")

def lanzar_dado(x, y):
    # Generar un numero aleatorio entre 1 y 6
    dado = random.randint(x, y)
    return dado


# Busqueda secuencial
# es un algoritmo de busqueda que consiste en recorrer una lista o un arreglo elemento por elemento hasta encontrar el elemento buscado o llegar al final de la lista.

# odenamiento de vectores
# es un algoritmo que consiste en organizar los elementos de un vector o lista en un orden especifico, ya sea ascendente o descendente.
# Existen diferentes algoritmos de ordenamiento, como el metodo de burbuja, el metodo de seleccion, el metodo de insercion, entre otros.

# El metodo de selaccion
# consiste en recorrer una lista o un arreglo y seleccionar el elemento mas pequeño (o mas grande) y colocarlo en la primera posicion de la lista. Luego se repite el proceso con el resto de la lista.

def busqueda_secuencial(lista, elemento):
    # Recorrer la lista
    for i in range(len(lista)):
        # Si el elemento es igual al elemento buscado, devolver la posicion
        if lista[i] == elemento:
            return i
    # Si no se encuentra el elemento, devolver -1
    return -1

# metodo de busqueda binaria
# es un algoritmo de busqueda que consiste en dividir una lista o un arreglo en dos partes y buscar el elemento en la parte correspondiente. Este algoritmo es mas eficiente que la busqueda secuencial, ya que reduce el tiempo de busqueda a la mitad en cada iteracion.
def busqueda_binaria(lista, elemento):
    # Definir los limites inferior y superior
    limite_inferior = 0
    limite_superior = len(lista) - 1

    # Mientras el limite inferior sea menor o igual al limite superior
    while limite_inferior <= limite_superior:
        # Calcular el punto medio
        punto_medio = (limite_inferior + limite_superior) // 2

        # Si el elemento es igual al elemento en el punto medio, devolver la posicion
        if lista[punto_medio] == elemento:
            return punto_medio
        # Si el elemento es menor que el elemento en el punto medio, buscar en la mitad inferior
        elif lista[punto_medio] > elemento:
            limite_superior = punto_medio - 1
        # Si el elemento es mayor que el elemento en el punto medio, buscar en la mitad superior
        else:
            limite_inferior = punto_medio + 1

    # Si no se encuentra el elemento, devolver -1
    return -1
