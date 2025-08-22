# las matrices son estructuras de datos bidimensionales eso significa que tienen filas y columnas
# se pueden representar como una lista de listas en python

# siempre va primero la fila y luego la columna

# ejemplo de una matriz 4x4 en formato de tabla
# | 1 2 3 4 |
# | 5 6 7 8 |
# | 9 10 11 12 |
# | 13 14 15 16 |

# array = listas = arreglos

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

# para python una matriz es una lista de listas, conceptualmente es lo mismo que los vectores, arrays o listas de otros lenguajes de programacion
# cada fila es una lista y cada columna es un elemento de esa lista

filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
matriz = []
for f in range(filas):
    matriz.append([])  # agregamos una fila vacia
    for c in range(columnas):
        matriz[f].append(0)  # inicializamos cada columna en 0
# ahora tenemos una matriz de filas x columnas con todos los elementos en 0
print("Matriz inicializada:")

# carga de datos por teclado
for f in range(filas):
    for c in range(columnas):
        n = int(input("ingresa un numero: "))
        matriz[f][c] = n

# carga de datoa random
import random
for f in range(filas):
    for c in range(columnas):
        n = random.randint(1, 100)  # genera un numero aleatorio entre 1 y 100
        matriz[f][c] = n
# como imprimir una matriz de manera correcta

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], end="\t")  # end="\t" para que se imprima en una sola linea
    print()  # salto de linea al final de cada fila
    
