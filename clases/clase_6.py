# Arreglos : listas

# los arreglos son una estructura de datos que permite almacenar varios valores en una sola variable
# los arreglos son mutables, es decir, se pueden modificar sus elementos
# los arreglos son indexados, es decir, se pueden acceder a sus elementos por su posicion en el arreglo
# los arreglos pueden contener diferentes tipos de datos, es decir, se pueden mezclar enteros, flotantes, cadenas, booleanos, etc.
# los arreglos pueden ser multidimensionales, es decir, se pueden crear arreglos de arreglos, o matrices

# crecen y decrecen dinamicamente, es decir, se pueden agregar o eliminar elementos en cualquier momento


# Crear un arreglo (lista)
numeros = [10, 20, 30, 40, 50]

# Acceder a elementos usando índices
print(numeros[0])  # Primer elemento: 10
print(numeros[-1]) # Último elemento: 50

# recorrer un arreglo con un bucle for
for numero in numeros:
    print(numero)  # Imprime cada elemento del arreglo

#Modificar un elemento del arreglo
numeros[2] = 99  # Cambia el tercer elemento
print(numeros)   # [10, 20, 99, 40, 50]

# Agregar y eliminar elemnentos
numeros.append(60)  # Agrega un elemento al final
numeros.insert(1, 15)  # Inserta en la posición 1
numeros.remove(40)  # Elimina un elemento por su valor
print(numeros)

# Arreglos multidimensionales (matrices)
# La definicion de una matriz es una lista de listas, donde cada lista interna representa una fila de la matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][1])  # Accede al elemento en la primera fila y segunda columna: 2
print(matriz[1][2])  # Accede al elemento en la segunda fila y tercera columna: 6

# con () el contenido del casillero
# con [] la posicion del casillero

# recorrer la lista de adelante hacia atras con while
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

# recorrer la lista de atras hacia adelante con while
i = len(numeros) - 1
while i >= 0:
    print(numeros[i])
    i -= 1

# para que sirve el end=""
# end="" es un argumento de la funcion print() que permite cambiar el comportamiento del salto de linea al imprimir
# por defecto, print() agrega un salto de linea al final de la salida, pero con end="" se puede especificar un string diferente para que se imprima al final
# por ejemplo, si se quiere imprimir una lista de numeros en la misma linea, se puede usar end=" " para agregar un espacio en lugar de un salto de linea

# ejemplo de uso de end="" con while, permite imprimir a continuacion con listas

numeros = [1, 2, 3, 4, 5]
i = 0

# Imprimir elementos en la misma línea con espacio entre ellos
while i < len(numeros):
    print(numeros[i], end=" ")
    i += 1

# Salida: 1 2 3 4 5

# cambio de valores
vect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 5
vect[a]= vect[a] + 1 # tomando el contenido del casillero 5 y sumandole 1, contenido es cuando sumo fuera de los corchetes
print(vect) # [1, 2, 3, 4, 6, 6, 7, 8, 9, 10]

b = 7
vect[b] = vect[a + 1] # dentro de los corchetes es la posicion del casillero, fuera de los corchetes es el contenido del casillero
print(vect) # [1, 2, 3, 4, 6, 6, 7, 8, 9, 10]


# len() devuelve la longitud de un arreglo, es decir, la cantidad de elementos que contiene
# el primer elemento de un arreglo tiene indice 0, el segundo elemento tiene indice 1, y asi sucesivamente

# ejemplo de uso de len() con while, permite imprimir la longitud de un arreglo
numeros = [1, 2, 3, 4, 5]
i = 0
print("Longitud del arreglo:", len(numeros))  # Imprime la longitud del arreglo: 5

# for in range(len(numeros)): es una forma de recorrer un arreglo usando un bucle for, donde range(len(numeros)) genera una secuencia de numeros desde 0 hasta la longitud del arreglo - 1
# es una forma de recorrer un arreglo usando un bucle for, donde range(len(numeros)) genera una secuencia de numeros desde 0 hasta la longitud del arreglo - 1

# range() genera una lista en memoria de numeros enteros, y len() devuelve la longitud de un arreglo, es decir, la cantidad de elementos que contiene

# los parametros de range() son:
# 1- start: el valor inicial de la secuencia (opcional, por defecto es 0)
# 2- stop: el valor final de la secuencia, hasta que posicon (obligatorio)
# 3- step: el incremento de la secuencia, el intervalo con  lo que voy a recorrer las posiciones  (opcional, por defecto es 1)

for i in range(len(numeros)):
    print(numeros[i])  # Imprime cada elemento del arreglo

#otro ejemplo mas completo y explicativo de el cilco for in range(len(numeros)):
numeros = [1, 2, 3, 4, 5]
i = 0

print("Longitud del arreglo:", len(numeros))  # Imprime la longitud del arreglo: 5
print("Elementos del arreglo:")
for i in range(len(numeros)):
    print("Elemento en la posición", i, ":", numeros[i])  # Imprime cada elemento del arreglo con su posición
# Salida:
# Longitud del arreglo: 5
# Elementos del arreglo:
# Elemento en la posición 0 : 1
# Elemento en la posición 1 : 2

# instruccion del en python es una palabra reservada que permite verificar si un elemento pertenece a un arreglo o lista
# la instruccion del se utiliza para eliminar un elemento de un arreglo o lista
# la instruccion del se utiliza para eliminar un elemento de un arreglo o lista, y se puede usar con el operador in para verificar si un elemento pertenece a un arreglo o lista

# ejemplo de uso de del 

numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)  # Imprime la lista original: [1, 2, 3, 4, 5]

del numeros[2]  # Elimina el elemento en la posición 2 (tercer elemento)
print("Lista después de eliminar el elemento en la posición 2:", numeros)  # Imprime la lista después de eliminar el elemento en la posición 2: [1, 2, 4, 5]    

