# ============================================================================
# TRABAJO PRÁCTICO: TUPLAS - RESUELTO CON EXPLICACIONES
# ============================================================================

import random
import math

print("="*80)
print("EJERCICIO 1: BARAJA ESPAÑOLA")
print("="*80)

# 1. Crear una variable utilizando tuplas que sea capaz de almacenar los valores de las
# cartas de la baraja española (48 cartas; del 1 al 12 de basto, copa, espada y oro).

# 🎯 CONSEJO: Piensa en la estructura antes de programar
# Una baraja española tiene 4 palos y 12 números por palo
# Podemos usar tuplas anidadas para representar esto

palos = ("basto", "copa", "espada", "oro")
numeros = tuple(range(1, 13))  # Del 1 al 12

# Crear el mazo completo usando comprensión de listas
# Cada carta es una tupla (número, palo)
mazo_espanol = tuple((numero, palo) for palo in palos for numero in numeros)

print(f"Mazo creado con {len(mazo_espanol)} cartas")
print("Primeras 5 cartas:", mazo_espanol[:5])
print("Últimas 5 cartas:", mazo_espanol[-5:])

# a. Crear una función que retorne una lista con una determina cantidad de cartas
# seleccionadas al azar que será recibida como parámetro

def sacar_cartas_aleatorias(mazo, cantidad):
    """
    🎯 CONSEJO: Siempre documenta tus funciones
    Saca una cantidad específica de cartas aleatorias del mazo.
    
    Args:
        mazo (tuple): El mazo de cartas
        cantidad (int): Número de cartas a sacar
    
    Returns:
        list: Lista con las cartas seleccionadas
    """
    # 🎯 CONSEJO: Valida los parámetros de entrada
    if cantidad > len(mazo):
        return "Error: No hay suficientes cartas en el mazo"
    
    if cantidad < 0:
        return "Error: La cantidad no puede ser negativa"
    
    # Convertir tupla a lista para poder usar random.sample
    mazo_lista = list(mazo)
    cartas_seleccionadas = random.sample(mazo_lista, cantidad)
    
    return cartas_seleccionadas

# b. Utilizando la función anterior, obtenga 10 cartas del mazo e indique la
# cantidad de cartas que son de oro.

cartas_sacadas = sacar_cartas_aleatorias(mazo_espanol, 10)
print(f"\n10 cartas aleatorias:")
for i, carta in enumerate(cartas_sacadas, 1):
    print(f"  Carta {i}: {carta[0]} de {carta[1]}")

# Contar cartas de oro
cartas_oro = [carta for carta in cartas_sacadas if carta[1] == "oro"]
print(f"\nCartas de oro encontradas: {len(cartas_oro)}")
for carta in cartas_oro:
    print(f"  {carta[0]} de oro")

# 🎯 CONSEJO: Siempre verifica tu lógica con ejemplos simples

print("\n" + "="*80)
print("EJERCICIO 2: PRODUCTO ESCALAR DE TUPLAS")
print("="*80)

# 2. Escribir un programa que dadas dos tuplas de tres elementos, realice el producto de
# cada elemento existente en la primera tupla con todos los restantes del segundo y
# almacene cada resultado en otra tupla.

def producto_escalar_tuplas(tupla1, tupla2):
    """
    🎯 CONSEJO: Antes de programar, entiende el patrón:
    - Cada elemento de tupla1 se multiplica por TODOS los elementos de tupla2
    - Resultado: tupla de tuplas
    
    Ejemplo: (1,2,3) × (4,5,6) = ((4,5,6), (8,10,12), (12,15,18))
    
    Args:
        tupla1, tupla2: Tuplas de 3 elementos
    
    Returns:
        tuple: Tupla con los productos
    """
    
    # 🎯 CONSEJO: Valida primero los datos de entrada
    if len(tupla1) != 3 or len(tupla2) != 3:
        return "Error: Ambas tuplas deben tener exactamente 3 elementos"
    
    resultado = []
    
    # Para cada elemento de la primera tupla
    for elemento1 in tupla1:
        # Multiplicarlo por todos los elementos de la segunda tupla
        productos_fila = tuple(elemento1 * elemento2 for elemento2 in tupla2)
        resultado.append(productos_fila)
    
    return tuple(resultado)

# Ejemplo del enunciado
tupla_a = (1, 2, 3)
tupla_b = (4, 5, 6)

print(f"Tupla A: {tupla_a}")
print(f"Tupla B: {tupla_b}")

resultado_producto = producto_escalar_tuplas(tupla_a, tupla_b)
print(f"Resultado: {resultado_producto}")

# 🎯 CONSEJO: Explica paso a paso lo que está pasando
print("\nPaso a paso:")
for i, elemento_a in enumerate(tupla_a):
    productos = tuple(elemento_a * elemento_b for elemento_b in tupla_b)
    print(f"  {elemento_a} × {tupla_b} = {productos}")

# Prueba con otros ejemplos
print("\nOtros ejemplos:")
ejemplo2 = producto_escalar_tuplas((2, 3, 4), (1, 2, 3))
print(f"(2,3,4) × (1,2,3) = {ejemplo2}")

ejemplo3 = producto_escalar_tuplas((5, 10), (2, 4, 6))  # Error esperado
print(f"Prueba con tuplas de diferente tamaño: {ejemplo3}")

print("\n" + "="*80)
print("EJERCICIO 3: HORARIOS AM/PM Y MINUTOS FALTANTES")
print("="*80)

# 3. Desarrolle un programa que procese una tabla con 10 horarios (hora y minutos) 
# en formato tupla; e indique por cada una de ellas: si es AM o PM y cuántos
# minutos falta para la próxima hora.

def procesar_horarios(lista_horarios):
    """
    🎯 CONSEJO: Divide el problema en partes más pequeñas:
    1. Determinar si es AM o PM
    2. Calcular minutos faltantes para la próxima hora
    3. Crear nueva tupla con toda la información
    
    Args:
        lista_horarios: Lista de tuplas (hora, minutos)
    
    Returns:
        list: Lista de tuplas con información completa
    """
    resultados = []
    
    for hora, minutos in lista_horarios:
        # 🎯 CONSEJO: Valida los datos antes de procesarlos
        if not (0 <= hora <= 23) or not (0 <= minutos <= 59):
            resultados.append((hora, minutos, "ERROR", "Hora o minutos inválidos"))
            continue
        
        # Determinar AM o PM
        if hora == 0:
            am_pm = "AM"
            hora_12 = 12
        elif 1 <= hora <= 11:
            am_pm = "AM"
            hora_12 = hora
        elif hora == 12:
            am_pm = "PM"
            hora_12 = 12
        else:  # 13-23
            am_pm = "PM"
            hora_12 = hora - 12
        
        # Calcular minutos faltantes para la próxima hora
        minutos_faltantes = 60 - minutos if minutos > 0 else 0
        
        # Crear tupla resultado: (hora_original, minutos_original, am_pm, minutos_faltantes, hora_12)
        resultado_tupla = (hora, minutos, f"{hora_12}:{minutos:02d} {am_pm}", minutos_faltantes)
        resultados.append(resultado_tupla)
    
    return resultados

# Crear 10 horarios de ejemplo (algunos aleatorios)
horarios_ejemplo = [
    (0, 30),    # 12:30 AM
    (6, 15),    # 6:15 AM
    (12, 0),    # 12:00 PM
    (14, 45),   # 2:45 PM
    (23, 59),   # 11:59 PM
    (9, 0),     # 9:00 AM
    (18, 30),   # 6:30 PM
    (3, 25),    # 3:25 AM
    (21, 10),   # 9:10 PM
    (16, 55)    # 4:55 PM
]

print("Horarios a procesar:")
for i, (hora, minutos) in enumerate(horarios_ejemplo, 1):
    print(f"  {i:2d}. {hora:02d}:{minutos:02d}")

resultados_horarios = procesar_horarios(horarios_ejemplo)

print("\nResultados procesados:")
print("    Original    →    Formato 12h    Minutos faltantes")
print("    " + "-"*50)

for hora, minutos, formato_12h, min_faltantes in resultados_horarios:
    print(f"    {hora:02d}:{minutos:02d}        →    {formato_12h:12s}    {min_faltantes:2d} minutos")

# 🎯 CONSEJO: Siempre prueba casos límite
print("\nPruebas con casos límite:")
casos_limite = [(0, 0), (12, 0), (23, 59), (24, 0), (15, 60)]  # Incluye casos con errores
resultados_limite = procesar_horarios(casos_limite)

for resultado in resultados_limite:
    if len(resultado) == 4:
        hora, minutos, formato, min_falt = resultado
        print(f"  {hora:02d}:{minutos:02d} → {formato} ({min_falt} min faltantes)")
    else:
        print(f"  {resultado}")

print("\n" + "="*80)
print("EJERCICIO 4: MANO DE PÓKER")
print("="*80)

# 4. Juego de cartas: crea una función que genere aleatoriamente una mano de cinco cartas
# de una baraja de póker. Cada carta debe ser representada por una tupla que contenga
# un número y un palo.

def generar_mano_poker():
    """
    🎯 CONSEJO: Define claramente las reglas del póker:
    - 52 cartas: 13 valores × 4 palos
    - Valores: A, 2-10, J, Q, K
    - Palos: ♠, ♥, ♦, ♣
    
    Returns:
        list: Lista de 5 tuplas (valor, palo)
    """
    
    # Definir los elementos de una baraja de póker
    valores = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    palos = ('♠', '♥', '♦', '♣')  # Espadas, Corazones, Diamantes, Tréboles
    
    # Crear baraja completa
    baraja_poker = [(valor, palo) for valor in valores for palo in palos]
    
    # 🎯 CONSEJO: En póker no se pueden repetir cartas
    mano = random.sample(baraja_poker, 5)
    
    return mano

def evaluar_mano_poker(mano):
    """
    🎯 CONSEJO: Función extra para hacer más interesante el ejercicio
    Evalúa básicamente qué tipo de mano es (par, escalera, etc.)
    """
    valores = [carta[0] for carta in mano]
    palos = [carta[1] for carta in mano]
    
    # Contar valores repetidos
    conteo_valores = {}
    for valor in valores:
        conteo_valores[valor] = conteo_valores.get(valor, 0) + 1
    
    # Verificar si todos los palos son iguales (color)
    es_color = len(set(palos)) == 1
    
    # Análisis básico
    repeticiones = sorted(conteo_valores.values(), reverse=True)
    
    if repeticiones == [4, 1]:
        return "Póker"
    elif repeticiones == [3, 2]:
        return "Full House"
    elif es_color:
        return "Color"
    elif repeticiones == [3, 1, 1]:
        return "Trío"
    elif repeticiones == [2, 2, 1]:
        return "Doble Par"
    elif repeticiones == [2, 1, 1, 1]:
        return "Par"
    else:
        return "Carta Alta"

# Generar y mostrar varias manos
print("Generando manos de póker:")
for i in range(3):
    mano = generar_mano_poker()
    evaluacion = evaluar_mano_poker(mano)
    
    print(f"\nMano {i+1}:")
    for j, (valor, palo) in enumerate(mano, 1):
        print(f"  Carta {j}: {valor}{palo}")
    print(f"  Evaluación: {evaluacion}")

# 🎯 CONSEJO: Muestra las tuplas tal como las pide el ejercicio
print(f"\nÚltima mano como tuplas: {mano}")

print("\n" + "="*80)
print("EJERCICIO 5: SUMA DE NÚMEROS EN TUPLAS")
print("="*80)

# 5. Suma de números: crea un programa que lea una lista de tuplas, donde cada tupla
# contiene dos números enteros, y calcule la suma de los números en cada tupla.

def sumar_numeros_tuplas(lista_tuplas):
    """
    🎯 CONSEJO: Este ejercicio es más simple de lo que parece
    Solo necesitas sumar los elementos de cada tupla y luego sumar todo
    
    Args:
        lista_tuplas: Lista de tuplas con dos números cada una
    
    Returns:
        int: Suma total de todos los números
    """
    
    suma_total = 0
    
    print("Procesando tuplas:")
    for i, tupla in enumerate(lista_tuplas, 1):
        if len(tupla) != 2:
            print(f"  Tupla {i}: {tupla} - ERROR: Debe tener exactamente 2 elementos")
            continue
        
        suma_tupla = tupla[0] + tupla[1]
        suma_total += suma_tupla
        
        print(f"  Tupla {i}: {tupla} → {tupla[0]} + {tupla[1]} = {suma_tupla}")
    
    return suma_total

# Ejemplo del enunciado
ejemplo_tuplas = [(1, 2), (3, 4), (5, 6)]
print(f"Lista de tuplas: {ejemplo_tuplas}")

resultado_suma = sumar_numeros_tuplas(ejemplo_tuplas)
print(f"\n🎯 Suma total: {resultado_suma}")

# 🎯 CONSEJO: Verifica manualmente: (1+2) + (3+4) + (5+6) = 3 + 7 + 11 = 21 ✓

# Más ejemplos
print("\nOtros ejemplos:")
ejemplo2 = [(10, 20), (30, 40), (50, 60)]
resultado2 = sumar_numeros_tuplas(ejemplo2)
print(f"Suma total: {resultado2}")

ejemplo3 = [(0, 0), (-5, 5), (100, -50)]
resultado3 = sumar_numeros_tuplas(ejemplo3)
print(f"Suma total: {resultado3}")

print("\n" + "="*80)
print("EJERCICIO 6: CÁLCULO DE PROMEDIO DE ESTUDIANTES")
print("="*80)

# 6. Cálculo de promedio: crea un programa que lea una lista de tuplas, donde cada tupla
# contiene el nombre de un estudiante y una lista de calificaciones, y calcule el promedio
# de calificaciones de cada estudiante.

def calcular_promedios_estudiantes(lista_estudiantes):
    """
    🎯 CONSEJO: Aquí trabajamos con tuplas que contienen strings y listas
    - Primer elemento: nombre (string)
    - Segundo elemento: lista de calificaciones (list)
    
    Args:
        lista_estudiantes: Lista de tuplas (nombre, [calificaciones])
    
    Returns:
        list: Lista de tuplas (nombre, promedio)
    """
    
    resultados = []
    
    print("Calculando promedios:")
    print("Estudiante       Calificaciones                    Promedio")
    print("-" * 60)
    
    for nombre, calificaciones in lista_estudiantes:
        # 🎯 CONSEJO: Siempre verifica que la lista no esté vacía
        if not calificaciones:
            promedio = 0.0
            print(f"{nombre:15s} Sin calificaciones                0.00")
        else:
            promedio = sum(calificaciones) / len(calificaciones)
            califs_str = str(calificaciones)
            print(f"{nombre:15s} {califs_str:25s}         {promedio:.2f}")
        
        # Crear tupla resultado
        resultado_tupla = (nombre, round(promedio, 2))
        resultados.append(resultado_tupla)
    
    return resultados

# Ejemplo del enunciado
estudiantes_ejemplo = [
    ('Juan', [9, 8, 7]),
    ('Maria', [10, 9, 10]),
    ('Pedro', [8, 7, 9])
]

print(f"Lista original: {estudiantes_ejemplo}")
print()

resultados_promedios = calcular_promedios_estudiantes(estudiantes_ejemplo)

print(f"\n🎯 Resultado final: {resultados_promedios}")

# 🎯 CONSEJO: Verificación manual:
# Juan: (9+8+7)/3 = 24/3 = 8.0 ✓
# Maria: (10+9+10)/3 = 29/3 = 9.67 ✓
# Pedro: (8+7+9)/3 = 24/3 = 8.0 ✓

# Más ejemplos con casos especiales
print("\nEjemplos adicionales:")
estudiantes_extra = [
    ('Ana', [10, 10, 10, 10]),
    ('Luis', [5, 6, 7, 8, 9]),
    ('Sofia', []),  # Sin calificaciones
    ('Carlos', [8.5, 9.2, 7.8])  # Con decimales
]

resultados_extra = calcular_promedios_estudiantes(estudiantes_extra)
print(f"Resultados extra: {resultados_extra}")

print("\n" + "="*80)
print("EJERCICIO 7: CÁLCULO DE ÁREAS")
print("="*80)

# 7. Cálculo de áreas: crea un programa que lea una lista de tuplas, donde cada tupla
# contiene el nombre de una figura geométrica (cuadrado, rectángulo, triángulo y
# círculo) y sus dimensiones, y calcule el área de cada figura.

def calcular_areas_figuras(lista_figuras):
    """
    🎯 CONSEJO: Define claramente qué dimensiones necesita cada figura:
    - Cuadrado: (lado)
    - Rectángulo: (base, altura)
    - Triángulo: (base, altura)
    - Círculo: (radio)
    
    Args:
        lista_figuras: Lista de tuplas (nombre_figura, dimensiones)
    
    Returns:
        list: Lista de tuplas (nombre_figura, dimensiones, area)
    """
    
    resultados = []
    
    print("Calculando áreas de figuras geométricas:")
    print("Figura          Dimensiones              Área")
    print("-" * 55)
    
    for figura_info in lista_figuras:
        nombre_figura = figura_info[0].lower()
        dimensiones = figura_info[1:]  # Resto de elementos son dimensiones
        
        # 🎯 CONSEJO: Usa un diccionario o if-elif para diferentes casos
        if nombre_figura == "cuadrado":
            if len(dimensiones) != 1:
                area = "Error: Cuadrado necesita 1 dimensión (lado)"
            else:
                lado = dimensiones[0]
                area = lado ** 2
                
        elif nombre_figura == "rectangulo" or nombre_figura == "rectángulo":
            if len(dimensiones) != 2:
                area = "Error: Rectángulo necesita 2 dimensiones (base, altura)"
            else:
                base, altura = dimensiones
                area = base * altura
                
        elif nombre_figura == "triangulo" or nombre_figura == "triángulo":
            if len(dimensiones) != 2:
                area = "Error: Triángulo necesita 2 dimensiones (base, altura)"
            else:
                base, altura = dimensiones
                area = (base * altura) / 2
                
        elif nombre_figura == "circulo" or nombre_figura == "círculo":
            if len(dimensiones) != 1:
                area = "Error: Círculo necesita 1 dimensión (radio)"
            else:
                radio = dimensiones[0]
                area = math.pi * (radio ** 2)
                
        else:
            area = f"Error: Figura '{nombre_figura}' no reconocida"
        
        # Mostrar resultado
        dim_str = str(dimensiones)
        if isinstance(area, (int, float)):
            area_str = f"{area:.2f}"
            print(f"{figura_info[0]:15s} {dim_str:20s}     {area_str}")
        else:
            print(f"{figura_info[0]:15s} {dim_str:20s}     {area}")
        
        # Crear tupla resultado
        resultado_tupla = (*figura_info, area)
        resultados.append(resultado_tupla)
    
    return resultados

# Ejemplos de figuras
figuras_ejemplo = [
    ("cuadrado", 5),
    ("rectángulo", 4, 6),
    ("triángulo", 8, 3),
    ("círculo", 3),
    ("cuadrado", 2.5),
    ("rectángulo", 10, 2),
    ("triángulo", 12, 5),
    ("círculo", 1.5)
]

print(f"Lista de figuras: {figuras_ejemplo[:4]}...")  # Mostrar solo las primeras
print()

resultados_areas = calcular_areas_figuras(figuras_ejemplo)

print(f"\n🎯 Resultados completos:")
for resultado in resultados_areas:
    print(f"  {resultado}")

# 🎯 CONSEJO: Verificación manual de algunos cálculos:
# Cuadrado lado 5: 5² = 25 ✓
# Rectángulo 4×6: 4×6 = 24 ✓
# Triángulo base 8, altura 3: (8×3)/2 = 12 ✓
# Círculo radio 3: π×3² ≈ 28.27 ✓

print("\nCasos con errores (para probar validaciones):")
figuras_error = [
    ("cuadrado", 5, 10),  # Demasiadas dimensiones
    ("círculo",),         # Sin dimensiones
    ("hexágono", 6),      # Figura no reconocida
]

resultados_error = calcular_areas_figuras(figuras_error)

print("\n" + "="*80)
print("🎯 RESUMEN DE CONSEJOS APRENDIDOS")
print("="*80)
print("""
1. 📋 PLANIFICACIÓN:
   - Antes de programar, entiende completamente el problema
   - Divide problemas grandes en partes más pequeñas
   - Define claramente qué datos de entrada esperas

2. 🔍 VALIDACIÓN:
   - Siempre valida los parámetros de entrada
   - Considera casos límite y errores posibles
   - Prueba con datos que sabes que pueden fallar

3. 📝 DOCUMENTACIÓN:
   - Documenta tus funciones con docstrings
   - Explica qué hace cada parte compleja del código
   - Incluye ejemplos de uso

4. 🧪 VERIFICACIÓN:
   - Verifica manualmente algunos resultados
   - Usa ejemplos simples para probar tu lógica
   - Prueba con diferentes tipos de datos

5. 🏗️ ESTRUCTURA:
   - Usa nombres de variables descriptivos
   - Mantén funciones pequeñas y enfocadas
   - Usa comentarios para explicar la lógica compleja

6. 🎯 TUPLAS ESPECÍFICAMENTE:
   - Son inmutables: no se pueden modificar
   - Perfectas para datos que no cambian
   - Se pueden usar como claves en diccionarios
   - Ideales para retornar múltiples valores de funciones
   - Se pueden desempaquetar fácilmente

¡Sigue practicando y siempre pregunta cuando tengas dudas!
""")
print("="*80)
