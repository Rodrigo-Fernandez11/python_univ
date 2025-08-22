# ============================================================================
# EXPLICACIÓN COMPLETA DE MATRICES EN PYTHON
# ============================================================================

# ============================================================================
# ¿QUÉ SON LAS MATRICES?
# ============================================================================
# Las matrices son estructuras de datos bidimensionales (filas y columnas)
# En Python, se implementan como LISTAS DE LISTAS
# - Cada lista interna representa una FILA
# - Los elementos de cada fila representan las COLUMNAS
# - Permiten organizar datos en forma de tabla

print("="*60)
print("1. CREACIÓN DE MATRICES")
print("="*60)

# 1. Matriz básica 3x3
matriz_basica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("1. Matriz 3x3:")
for fila in matriz_basica:
    print("  ", fila)

# 2. Matriz de diferentes tipos de datos
matriz_mixta = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 25, "Madrid"],
    ["Ana", 30, "Barcelona"],
    ["Luis", 22, "Valencia"]
]
print("\n2. Matriz mixta (tabla de personas):")
for fila in matriz_mixta:
    print("  ", fila)

# 3. Matriz con todos los elementos iguales
filas, columnas = 3, 4
matriz_ceros = [[0 for j in range(columnas)] for i in range(filas)]
print(f"\n3. Matriz de {filas}x{columnas} llena de ceros:")
for fila in matriz_ceros:
    print("  ", fila)

print("\n" + "="*60)
print("2. ACCESO A ELEMENTOS DE LA MATRIZ")
print("="*60)

# Trabajaremos con esta matriz de ejemplo
numeros = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Matriz de ejemplo:")
for i, fila in enumerate(numeros):
    print(f"  Fila {i}: {fila}")

# Acceso por índices: matriz[fila][columna]
print(f"\nElemento en fila 0, columna 0: {numeros[0][0]}")  # 10
print(f"Elemento en fila 1, columna 2: {numeros[1][2]}")    # 60
print(f"Elemento en fila 2, columna 1: {numeros[2][1]}")    # 80

# Acceso a una fila completa
print(f"Fila completa 1: {numeros[1]}")  # [40, 50, 60]

# Modificar un elemento
print(f"\nAntes de modificar: {numeros[1][1]}")
numeros[1][1] = 999
print(f"Después de modificar: {numeros[1][1]}")
print("Matriz modificada:")
for fila in numeros:
    print("  ", fila)

print("\n" + "="*60)
print("3. DIMENSIONES DE UNA MATRIZ")
print("="*60)

def obtener_dimensiones(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return filas, columnas

def mostrar_info_matriz(matriz, nombre):
    filas, columnas = obtener_dimensiones(matriz)
    print(f"{nombre}:")
    print(f"  Filas: {filas}")
    print(f"  Columnas: {columnas}")
    print(f"  Dimensión: {filas}x{columnas}")
    print(f"  Total de elementos: {filas * columnas}")

# Diferentes tipos de matrices
matriz_2x3 = [[1, 2, 3], [4, 5, 6]]
matriz_4x2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
matriz_1x5 = [[1, 2, 3, 4, 5]]

mostrar_info_matriz(matriz_2x3, "Matriz 2x3")
mostrar_info_matriz(matriz_4x2, "Matriz 4x2")
mostrar_info_matriz(matriz_1x5, "Matriz 1x5")

print("\n" + "="*60)
print("4. RECORRIDO DE MATRICES")
print("="*60)

colores = [
    ["rojo", "verde", "azul"],
    ["amarillo", "naranja", "morado"],
    ["negro", "blanco", "gris"]
]

# Método 1: Recorrido simple por filas
print("Método 1 - Recorrido por filas:")
for fila in colores:
    for elemento in fila:
        print(f"  {elemento}", end=" ")
    print()  # Salto de línea después de cada fila

# Método 2: Recorrido con índices
print("\nMétodo 2 - Recorrido con índices:")
for i in range(len(colores)):
    for j in range(len(colores[i])):
        print(f"  [{i}][{j}]: {colores[i][j]}")

# Método 3: Recorrido con enumerate
print("\nMétodo 3 - Recorrido con enumerate:")
for i, fila in enumerate(colores):
    for j, elemento in enumerate(fila):
        print(f"  Posición ({i},{j}): {elemento}")

print("\n" + "="*60)
print("5. OPERACIONES BÁSICAS CON MATRICES")
print("="*60)

# Suma de todos los elementos
def sumar_elementos(matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    return suma

# Encontrar el valor máximo
def encontrar_maximo(matriz):
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

# Encontrar el valor mínimo
def encontrar_minimo(matriz):
    minimo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento < minimo:
                minimo = elemento
    return minimo

# Buscar un elemento específico
def buscar_elemento(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición
    return None  # No encontrado

# Ejemplo con matriz numérica
nums = [
    [5, 12, 8],
    [3, 15, 7],
    [9, 2, 11]
]

print("Matriz de números:")
for fila in nums:
    print("  ", fila)

print(f"\nSuma total: {sumar_elementos(nums)}")
print(f"Valor máximo: {encontrar_maximo(nums)}")
print(f"Valor mínimo: {encontrar_minimo(nums)}")

posicion_15 = buscar_elemento(nums, 15)
if posicion_15:
    print(f"El valor 15 está en la posición: {posicion_15}")
else:
    print("El valor 15 no se encontró")

print("\n" + "="*60)
print("6. CREACIÓN DINÁMICA DE MATRICES")
print("="*60)

# Crear matriz con input del usuario
def crear_matriz_usuario():
    filas = int(input("¿Cuántas filas quieres? "))
    columnas = int(input("¿Cuántas columnas quieres? "))
    
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingresa el valor para [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    return matriz

# Crear matriz con valores aleatorios
import random

def crear_matriz_aleatoria(filas, columnas, min_val=1, max_val=100):
    return [[random.randint(min_val, max_val) for j in range(columnas)] for i in range(filas)]

# Crear matriz con patrón específico
def crear_matriz_patron(filas, columnas):
    return [[i*columnas + j + 1 for j in range(columnas)] for i in range(filas)]

print("Ejemplos de creación dinámica:")
matriz_aleatoria = crear_matriz_aleatoria(3, 3)
print("Matriz aleatoria 3x3:")
for fila in matriz_aleatoria:
    print("  ", fila)

matriz_patron = crear_matriz_patron(4, 3)
print("\nMatriz con patrón secuencial 4x3:")
for fila in matriz_patron:
    print("  ", fila)

print("\n" + "="*60)
print("7. OPERACIONES AVANZADAS")
print("="*60)

# Transponer una matriz (intercambiar filas por columnas)
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
    return transpuesta

# Multiplicar matriz por un escalar
def multiplicar_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]

# Sumar dos matrices (deben tener las mismas dimensiones)
def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Error: Las matrices deben tener las mismas dimensiones"
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

# Ejemplos
original = [[1, 2, 3], [4, 5, 6]]
print("Matriz original:")
for fila in original:
    print("  ", fila)

transpuesta = transponer_matriz(original)
print("\nMatriz transpuesta:")
for fila in transpuesta:
    print("  ", fila)

multiplicada = multiplicar_escalar(original, 3)
print("\nMatriz multiplicada por 3:")
for fila in multiplicada:
    print("  ", fila)

matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]
suma = sumar_matrices(matriz_a, matriz_b)
print("\nSuma de matrices:")
print("Matriz A:", matriz_a)
print("Matriz B:", matriz_b)
print("A + B:", suma)

print("\n" + "="*60)
print("8. MATRICES ESPECIALES")
print("="*60)

# Matriz identidad (1s en la diagonal, 0s en el resto)
def crear_matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Matriz diagonal
def crear_matriz_diagonal(valores):
    n = len(valores)
    return [[valores[i] if i == j else 0 for j in range(n)] for i in range(n)]

# Verificar si una matriz es cuadrada
def es_cuadrada(matriz):
    return len(matriz) == len(matriz[0])

# Verificar si una matriz es simétrica
def es_simetrica(matriz):
    if not es_cuadrada(matriz):
        return False
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

print("Matriz identidad 4x4:")
identidad = crear_matriz_identidad(4)
for fila in identidad:
    print("  ", fila)

print("\nMatriz diagonal:")
diagonal = crear_matriz_diagonal([2, 5, 8, 3])
for fila in diagonal:
    print("  ", fila)

test_simetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
print(f"\n¿La matriz {test_simetrica} es simétrica? {es_simetrica(test_simetrica)}")

print("\n" + "="*60)
print("9. CASOS DE USO PRÁCTICOS")
print("="*60)

# 1. Tablero de juego (como tres en raya)
def crear_tablero_vacio(tamaño):
    return [["." for j in range(tamaño)] for i in range(tamaño)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("  " + " ".join(fila))

# 2. Tabla de calificaciones
calificaciones = [
    ["Estudiante", "Matemáticas", "Ciencias", "Historia"],
    ["Ana", 95, 87, 92],
    ["Luis", 78, 93, 85],
    ["María", 88, 91, 94]
]

def calcular_promedio_estudiante(calificaciones, fila_estudiante):
    notas = calificaciones[fila_estudiante][1:]  # Excluir el nombre
    return sum(notas) / len(notas)

print("1. Tablero de tres en raya:")
tablero = crear_tablero_vacio(3)
tablero[1][1] = "X"  # Jugada en el centro
tablero[0][0] = "O"  # Jugada en esquina
mostrar_tablero(tablero)

print("\n2. Tabla de calificaciones:")
for fila in calificaciones:
    print("  ", fila)

print("\nPromedios:")
for i in range(1, len(calificaciones)):
    nombre = calificaciones[i][0]
    promedio = calcular_promedio_estudiante(calificaciones, i)
    print(f"  {nombre}: {promedio:.1f}")

print("\n" + "="*60)
print("10. EJEMPLO COMPLETO: SISTEMA DE VENTAS")
print("="*60)

# Matriz de ventas: [mes, producto1, producto2, producto3]
ventas_mensuales = [
    ["Mes", "Producto A", "Producto B", "Producto C"],
    ["Enero", 100, 150, 80],
    ["Febrero", 120, 140, 90],
    ["Marzo", 110, 160, 85],
    ["Abril", 130, 155, 95]
]

def mostrar_tabla_ventas(ventas):
    for fila in ventas:
        print(f"  {fila[0]:10} {fila[1]:12} {fila[2]:12} {fila[3]:12}")

def calcular_total_producto(ventas, columna_producto):
    total = 0
    for i in range(1, len(ventas)):  # Saltar encabezado
        total += ventas[i][columna_producto]
    return total

def calcular_total_mes(ventas, fila_mes):
    return sum(ventas[fila_mes][1:])  # Sumar todas las columnas excepto el mes

print("Tabla de ventas mensuales:")
mostrar_tabla_ventas(ventas_mensuales)

print("\nTotales por producto:")
for i in range(1, 4):  # Productos A, B, C
    producto = ventas_mensuales[0][i]
    total = calcular_total_producto(ventas_mensuales, i)
    print(f"  {producto}: {total} unidades")

print("\nTotales por mes:")
for i in range(1, len(ventas_mensuales)):
    mes = ventas_mensuales[i][0]
    total = calcular_total_mes(ventas_mensuales, i)
    print(f"  {mes}: {total} unidades")


# EJERCICIO ORIGINAL DEL ARCHIVO:

print("\n" + "="*60)
print("11. EJERCICIO ORIGINAL: DÍAS DEL MES")
print("="*60)

# 1. Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
# y diga cuántos días tiene (por ejemplo, 30). Debes usar una matriz para su
# parametrización y una función para la recuperación del dato

# proposito es verificar si un numero representa un mes valido
# parametro que vamos a recibir del usuario es mes
def validarMes(mes):
    return mes >= 1 and mes <=12

# funcion que usamos una matriz meses, cada sublista contiene el mes y la cantidad de días
def cantidadDiasMes(mes):
    meses = [
                [6,30],   # Junio
                [7,31],   # Julio
                [8,31],   # Agosto
                [9,30],   # Septiembre
                [10,31],  # Octubre
                [11,30],  # Noviembre
                [12,31],  # Diciembre
                [1,31],   # Enero
                [2,28],   # Febrero (sin años bisiestos)
                [3,31],   # Marzo
                [4,30],   # Abril
                [5,31]    # Mayo
            ]
# condición : si el mes buscado es igual al mes en la matriz (primer elemento de la sublista)
    for i in range(0, len(meses)):
        if mes == meses[i][0]:
            return meses[i][1] # devuelve meses[i][1] (segundo elemento == cantidad de días)

print("Probando todos los meses (válidos e inválidos):")
for mes in range(-2, 16):
    if validarMes(mes):
        print(f"Mes {mes}: {cantidadDiasMes(mes)} días")
    else:
        print(f"Mes {mes}: es inválido")

# Versión interactiva del programa
print("\n" + "="*60)
print("PROGRAMA INTERACTIVO - DÍAS DEL MES")
print("="*60)

def programa_dias_mes():
    nombres_meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    try:
        mes_usuario = int(input("Ingresa un número de mes (1-12): "))
        
        if validarMes(mes_usuario):
            dias = cantidadDiasMes(mes_usuario)
            nombre_mes = nombres_meses[mes_usuario]
            print(f"✓ {nombre_mes} (mes {mes_usuario}) tiene {dias} días")
        else:
            print(f"✗ El número {mes_usuario} no corresponde a un mes válido")
            print("  Los meses válidos son del 1 al 12")
    
    except ValueError:
        print("✗ Error: Debes ingresar un número entero")

# Descomenta la siguiente línea para ejecutar el programa interactivo
# programa_dias_mes()

print("\n" + "="*60)
print("¡RESUMEN FINAL DE MATRICES!")
print("="*60)
print("Las matrices en Python son útiles para:")
print("1. Representar datos en forma de tabla (filas y columnas)")
print("2. Trabajar con datos bidimensionales")
print("3. Operaciones matemáticas y científicas")
print("4. Tableros de juegos")
print("5. Almacenar y procesar datos estructurados")
print("")
print("Conceptos clave:")
print("- Se crean como listas de listas: [[fila1], [fila2], [fila3]]")
print("- Acceso por índices: matriz[fila][columna]")
print("- Se pueden recorrer con bucles anidados")
print("- Son mutables (se pueden modificar)")
print("- Permiten operaciones como suma, multiplicación, transposición")
print("="*60)