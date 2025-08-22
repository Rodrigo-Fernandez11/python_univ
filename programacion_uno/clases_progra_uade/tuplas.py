# ============================================================================
# EXPLICACIÓN COMPLETA DE TUPLAS EN PYTHON
# ============================================================================

# ============================================================================
# ¿QUÉ SON LAS TUPLAS?
# ============================================================================
# Las tuplas son secuencias ordenadas e INMUTABLES de elementos
# - Ordenadas: Los elementos tienen un orden específico que no cambia
# - Inmutables: No se pueden modificar después de ser creadas
# - Permiten elementos duplicados
# - Pueden contener diferentes tipos de datos

print("="*60)
print("1. CREACIÓN DE TUPLAS")
print("="*60)

# 1. Tupla vacía
tupla_vacia = ()
print("1. Tupla vacía:", tupla_vacia)

# 2. Tupla con elementos del mismo tipo
tupla_numeros = (1, 2, 3, 4, 5)
tupla_textos = ("manzana", "banana", "cereza")
print("2. Tupla de números:", tupla_numeros)
print("   Tupla de textos:", tupla_textos)

# 3. Tupla con elementos de diferentes tipos (mixta)
tupla_mixta = (1, "hola", 3.14, True, [1, 2, 3])
print("3. Tupla mixta:", tupla_mixta)

# 4. Tupla sin paréntesis (empaquetado automático)
tupla_sin_parentesis = 1, 2, 3, 4
print("4. Tupla sin paréntesis:", tupla_sin_parentesis)

# 5. Tupla con UN SOLO elemento (¡CUIDADO CON LA COMA!)
tupla_un_elemento = (5,)  # LA COMA ES OBLIGATORIA
no_es_tupla = (5)         # Esto NO es una tupla, es solo el número 5
print("5. Tupla de un elemento:", tupla_un_elemento, type(tupla_un_elemento))
print("   No es tupla:", no_es_tupla, type(no_es_tupla))

# 6. Convertir otros tipos a tupla
lista = [1, 2, 3, 4]
tupla_desde_lista = tuple(lista)
tupla_desde_string = tuple("Python")
print("6. Tupla desde lista:", tupla_desde_lista)
print("   Tupla desde string:", tupla_desde_string)

print("\n" + "="*60)
print("2. ACCESO A ELEMENTOS (INDEXACIÓN)")
print("="*60)

colores = ("rojo", "verde", "azul", "amarillo", "negro")
print("Tupla de colores:", colores)

# Índices positivos (de izquierda a derecha: 0, 1, 2, 3, 4)
print("Primer elemento (índice 0):", colores[0])
print("Segundo elemento (índice 1):", colores[1])
print("Último elemento (índice 4):", colores[4])

# Índices negativos (de derecha a izquierda: -1, -2, -3, -4, -5)
print("Último elemento (índice -1):", colores[-1])
print("Penúltimo elemento (índice -2):", colores[-2])

print("\n" + "="*60)
print("3. SLICING (REBANADO)")
print("="*60)

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tupla original:", numeros)

# Sintaxis: tupla[inicio:fin:paso]
print("numeros[1:5]:", numeros[1:5])      # Del índice 1 al 4
print("numeros[:3]:", numeros[:3])        # Desde el inicio hasta el índice 2
print("numeros[3:]:", numeros[3:])        # Desde el índice 3 hasta el final
print("numeros[-3:]:", numeros[-3:])      # Los últimos 3 elementos
print("numeros[::2]:", numeros[::2])      # Todos los elementos con paso 2
print("numeros[::-1]:", numeros[::-1])    # Tupla invertida

print("\n" + "="*60)
print("4. INMUTABILIDAD DE LAS TUPLAS")
print("="*60)

frutas = ("manzana", "banana", "cereza")
print("Tupla original:", frutas)

# Esto NO funciona (genera error):
# frutas[0] = "pera"  # TypeError: 'tuple' object does not support item assignment
# frutas.append("pera")  # AttributeError: 'tuple' object has no attribute 'append'

print("Las tuplas NO se pueden modificar después de ser creadas")

# Sin embargo, si una tupla contiene objetos mutables, esos SÍ se pueden modificar
tupla_con_lista = (1, 2, [3, 4, 5])
print("Tupla con lista:", tupla_con_lista)
tupla_con_lista[2][0] = 99  # Modificamos el primer elemento de la lista
print("Después de modificar la lista interna:", tupla_con_lista)

print("\n" + "="*60)
print("5. MÉTODOS DE TUPLAS")
print("="*60)

animales = ("gato", "perro", "gato", "pájaro", "gato", "pez")
print("Tupla de animales:", animales)

# count() - Cuenta las apariciones de un elemento
print("Número de 'gato':", animales.count("gato"))
print("Número de 'perro':", animales.count("perro"))

# index() - Encuentra el índice de la primera aparición
print("Índice del primer 'gato':", animales.index("gato"))
print("Índice de 'pájaro':", animales.index("pájaro"))

print("\n" + "="*60)
print("6. OPERACIONES CON TUPLAS")
print("="*60)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print("Tupla 1:", tupla1)
print("Tupla 2:", tupla2)

# Concatenación
tupla_concatenada = tupla1 + tupla2
print("Concatenación (+):", tupla_concatenada)

# Repetición
tupla_repetida = tupla1 * 3
print("Repetición (* 3):", tupla_repetida)

# Membresía (verificar si un elemento está en la tupla)
print("¿2 está en tupla1?", 2 in tupla1)
print("¿7 está en tupla1?", 7 in tupla1)

# Longitud
print("Longitud de tupla1:", len(tupla1))

print("\n" + "="*60)
print("7. DESEMPAQUETADO DE TUPLAS")
print("="*60)

# Asignación múltiple (desempaquetado)
coordenadas = (10, 20)
x, y = coordenadas
print("Coordenadas:", coordenadas)
print("x =", x, ", y =", y)

# Desempaquetado con más elementos
persona = ("Juan", "Pérez", 25, "Programador")
nombre, apellido, edad, profesion = persona
print("Persona:", persona)
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}, Profesión: {profesion}")

# Desempaquetado parcial con asterisco (*)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
primero, segundo, *resto, ultimo = numeros
print("Números:", numeros)
print("Primero:", primero)
print("Segundo:", segundo)
print("Resto:", resto)
print("Último:", ultimo)

print("\n" + "="*60)
print("8. TUPLAS ANIDADAS")
print("="*60)

# Tuplas dentro de tuplas
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matriz (tupla de tuplas):", matriz)
print("Primera fila:", matriz[0])
print("Elemento [1][2]:", matriz[1][2])  # Fila 1, Columna 2

# Recorrer tupla anidada
print("Recorriendo la matriz:")
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        print(f"Posición [{i}][{j}]: {elemento}")

print("\n" + "="*60)
print("9. RECORRIDO DE TUPLAS")
print("="*60)

estaciones = ("primavera", "verano", "otoño", "invierno")

# Recorrido simple
print("Recorrido simple:")
for estacion in estaciones:
    print(f"- {estacion}")

# Recorrido con índice
print("\nRecorrido con índice:")
for i in range(len(estaciones)):
    print(f"{i}: {estaciones[i]}")

# Recorrido con enumerate
print("\nRecorrido con enumerate:")
for indice, estacion in enumerate(estaciones):
    print(f"{indice}: {estacion}")

print("\n" + "="*60)
print("10. COMPARACIÓN: TUPLAS vs LISTAS")
print("="*60)

print("TUPLAS:")
print("- Inmutables (no se pueden modificar)")
print("- Más rápidas para acceder a elementos")
print("- Menos memoria")
print("- Se pueden usar como claves en diccionarios")
print("- Ideales para datos que no cambian")

print("\nLISTAS:")
print("- Mutables (se pueden modificar)")
print("- Más lentas para acceder a elementos")
print("- Más memoria")
print("- NO se pueden usar como claves en diccionarios")
print("- Ideales para datos que cambian")

print("\n" + "="*60)
print("11. CASOS DE USO COMUNES")
print("="*60)

# 1. Coordenadas
punto = (3, 7)
print("1. Coordenadas:", punto)

# 2. Datos de una persona
estudiante = ("María", "García", 20, "Ingeniería")
print("2. Datos de estudiante:", estudiante)

# 3. Configuración que no debe cambiar
configuracion = ("localhost", 8080, True)
print("3. Configuración:", configuracion)

# 4. Retorno múltiple de funciones
def obtener_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

lista_numeros = [1, 2, 3, 4, 5]
minimo, maximo, promedio = obtener_estadisticas(lista_numeros)
print("4. Estadísticas:", f"Min: {minimo}, Max: {maximo}, Promedio: {promedio}")

# 5. Como claves en diccionarios
diccionario_coordenadas = {
    (0, 0): "origen",
    (1, 0): "derecha",
    (0, 1): "arriba"
}
print("5. Diccionario con tuplas como claves:", diccionario_coordenadas)

print("\n" + "="*60)
print("12. FUNCIONES ÚTILES CON TUPLAS")
print("="*60)

datos = (3, 1, 4, 1, 5, 9, 2, 6)
print("Datos:", datos)

# Funciones integradas
print("Longitud:", len(datos))
print("Mínimo:", min(datos))
print("Máximo:", max(datos))
print("Suma:", sum(datos))
print("Ordenada:", tuple(sorted(datos)))
print("Invertida:", tuple(reversed(datos)))

print("\n" + "="*60)
print("¡RESUMEN FINAL!")
print("="*60)
print("Las tuplas son perfectas cuando necesitas:")
print("1. Almacenar datos que NO van a cambiar")
print("2. Trabajar con coordenadas o puntos")
print("3. Retornar múltiples valores desde una función")
print("4. Usar como claves en diccionarios")
print("5. Proteger datos de modificaciones accidentales")
print("="*60)
