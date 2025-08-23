# ============================================================================
# SEGMENTACIÓN DE LISTAS (SLICING) - EXPLICACIÓN COMPLETA
# ============================================================================

# ============================================================================
# ¿QUÉ ES LA SEGMENTACIÓN DE LISTAS?
# ============================================================================
# La segmentación (slicing) es una técnica para extraer partes específicas de una lista
# - Te permite obtener sublistas sin modificar la lista original
# - Usa la sintaxis: lista[inicio:fin:paso]
# - Es una herramienta MUY poderosa en Python

print("="*80)
print("1. CONCEPTOS BÁSICOS DE SEGMENTACIÓN")
print("="*80)

# Lista de ejemplo para todos los ejercicios
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("Lista de números:", numeros)
print("Lista de letras:", letras)

# 🎯 CONSEJO: Los índices en Python empiezan en 0
print("\nÍndices de la lista:")
print("Posición:  0  1  2  3  4  5  6  7  8  9")
print("Valor:    ", numeros)
print("Neg:     -10 -9 -8 -7 -6 -5 -4 -3 -2 -1")

print("\n" + "="*80)
print("2. SINTAXIS BÁSICA: lista[inicio:fin]")
print("="*80)

# 🎯 CONSEJO: El índice 'fin' NO se incluye en el resultado
print("numeros[2:5]:", numeros[2:5])  # Elementos 2, 3, 4 (5 NO se incluye)
print("letras[1:4]:", letras[1:4])    # Elementos b, c, d

# Explicación paso a paso
print("\n🎯 EXPLICACIÓN:")
print("numeros[2:5] significa:")
print("  - Empieza en el índice 2 (valor 2)")
print("  - Termina ANTES del índice 5 (valor 5)")
print("  - Resultado: [2, 3, 4]")

print("\n" + "="*80)
print("3. OMITIR EL INICIO O EL FIN")
print("="*80)

# Omitir el inicio (desde el principio)
print("numeros[:4]:", numeros[:4])    # Desde el inicio hasta el índice 3
print("letras[:3]:", letras[:3])      # Desde el inicio hasta el índice 2

# Omitir el fin (hasta el final)
print("numeros[6:]:", numeros[6:])    # Desde el índice 6 hasta el final
print("letras[7:]:", letras[7:])      # Desde el índice 7 hasta el final

# 🎯 CONSEJO: Esto es muy útil para dividir listas
print("\n🎯 DIVIDIR UNA LISTA EN DOS PARTES:")
mitad = len(numeros) // 2
primera_mitad = numeros[:mitad]
segunda_mitad = numeros[mitad:]
print(f"Primera mitad: {primera_mitad}")
print(f"Segunda mitad: {segunda_mitad}")

print("\n" + "="*80)
print("4. ÍNDICES NEGATIVOS")
print("="*80)

# Los índices negativos cuentan desde el final
print("numeros[-3:]:", numeros[-3:])   # Últimos 3 elementos
print("numeros[:-2]:", numeros[:-2])   # Todos excepto los últimos 2
print("letras[-5:-1]:", letras[-5:-1]) # Desde -5 hasta -2

print("\n🎯 EJEMPLOS PRÁCTICOS CON ÍNDICES NEGATIVOS:")
print("Último elemento:", numeros[-1])
print("Últimos 3:", numeros[-3:])
print("Todo excepto el último:", numeros[:-1])
print("Penúltimo elemento:", numeros[-2])

print("\n" + "="*80)
print("5. EL TERCER PARÁMETRO: PASO (STEP)")
print("="*80)

# El paso determina de cuánto en cuánto avanzas
print("numeros[::2]:", numeros[::2])     # Todos con paso 2 (de 2 en 2)
print("numeros[1::2]:", numeros[1::2])   # Desde índice 1, de 2 en 2
print("letras[::3]:", letras[::3])       # De 3 en 3

print("\n🎯 PASOS ÚTILES:")
print("Números pares (posiciones pares):", numeros[::2])
print("Números impares (posiciones impares):", numeros[1::2])
print("Cada tercer elemento:", numeros[::3])

print("\n" + "="*80)
print("6. INVERTIR LISTAS CON PASO NEGATIVO")
print("="*80)

# Paso negativo = recorrer hacia atrás
print("numeros[::-1]:", numeros[::-1])   # Lista completa invertida
print("letras[::-1]:", letras[::-1])     # Lista completa invertida

print("numeros[8:2:-1]:", numeros[8:2:-1])  # Desde 8 hasta 3, hacia atrás
print("letras[-1:-6:-1]:", letras[-1:-6:-1]) # Últimos 5, hacia atrás

print("\n🎯 FORMAS DE INVERTIR:")
original = [1, 2, 3, 4, 5]
print("Original:", original)
print("Con slicing:", original[::-1])
print("Con reversed():", list(reversed(original)))

print("\n" + "="*80)
print("7. EJEMPLOS PRÁCTICOS Y CASOS DE USO")
print("="*80)

# Ejemplo: Lista de calificaciones
calificaciones = [85, 92, 78, 96, 87, 91, 83, 94, 88, 90]
print("Calificaciones:", calificaciones)

# Obtener las mejores y peores calificaciones
calificaciones_ordenadas = sorted(calificaciones, reverse=True)
print("Ordenadas (mayor a menor):", calificaciones_ordenadas)

mejores_3 = calificaciones_ordenadas[:3]
peores_3 = calificaciones_ordenadas[-3:]
print(f"Mejores 3: {mejores_3}")
print(f"Peores 3: {peores_3}")

# Obtener calificaciones del primer y segundo semestre
primer_semestre = calificaciones[:5]
segundo_semestre = calificaciones[5:]
print(f"Primer semestre: {primer_semestre}")
print(f"Segundo semestre: {segundo_semestre}")

print("\n" + "="*80)
print("8. SEGMENTACIÓN CON STRINGS")
print("="*80)

# 🎯 CONSEJO: Los strings también se pueden segmentar
texto = "Python es genial"
print("Texto:", texto)

print("texto[0:6]:", texto[0:6])      # "Python"
print("texto[7:9]:", texto[7:9])      # "es"
print("texto[10:]:", texto[10:])      # "genial"
print("texto[::-1]:", texto[::-1])    # Texto invertido

# Casos prácticos con strings
email = "usuario@gmail.com"
print(f"\nEmail: {email}")
usuario = email[:email.index('@')]
dominio = email[email.index('@')+1:]
print(f"Usuario: {usuario}")
print(f"Dominio: {dominio}")

print("\n" + "="*80)
print("9. EJERCICIOS PRÁCTICOS RESUELTOS")
print("="*80)

def ejercicios_segmentacion():
    """
    🎯 CONSEJO: Practiquemos con ejercicios reales
    """
    
    # Ejercicio 1: Extraer información de una lista de productos
    productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora", "Scanner", "Tablet", "Smartphone"]
    print("🎯 EJERCICIO 1: Lista de productos")
    print("Productos:", productos)
    
    print("Primeros 3 productos:", productos[:3])
    print("Últimos 2 productos:", productos[-2:])
    print("Productos del 2 al 5:", productos[1:5])
    print("Productos en posiciones pares:", productos[::2])
    
    # Ejercicio 2: Procesar datos de ventas mensuales
    ventas_mensuales = [1200, 1350, 1100, 1500, 1800, 1650, 1900, 1750, 1600, 1400, 1550, 1700]
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    
    print(f"\n🎯 EJERCICIO 2: Ventas mensuales")
    print("Ventas:", ventas_mensuales)
    
    # Trimestres
    q1 = ventas_mensuales[:3]    # Primer trimestre
    q2 = ventas_mensuales[3:6]   # Segundo trimestre
    q3 = ventas_mensuales[6:9]   # Tercer trimestre
    q4 = ventas_mensuales[9:]    # Cuarto trimestre
    
    print(f"Q1 (Ene-Mar): {q1} → Total: {sum(q1)}")
    print(f"Q2 (Abr-Jun): {q2} → Total: {sum(q2)}")
    print(f"Q3 (Jul-Sep): {q3} → Total: {sum(q3)}")
    print(f"Q4 (Oct-Dic): {q4} → Total: {sum(q4)}")
    
    # Semestres
    primer_semestre = ventas_mensuales[:6]
    segundo_semestre = ventas_mensuales[6:]
    print(f"Primer semestre: {sum(primer_semestre)}")
    print(f"Segundo semestre: {sum(segundo_semestre)}")
    
    # Ejercicio 3: Análisis de temperaturas
    temperaturas = [22, 25, 28, 30, 32, 29, 26, 24, 27, 31, 33, 28, 25, 23]
    print(f"\n🎯 EJERCICIO 3: Análisis de temperaturas")
    print("Temperaturas (°C):", temperaturas)
    
    # Análisis por semanas (asumiendo 7 días por semana)
    semana1 = temperaturas[:7]
    semana2 = temperaturas[7:]
    
    print(f"Semana 1: {semana1}")
    print(f"Promedio semana 1: {sum(semana1)/len(semana1):.1f}°C")
    print(f"Semana 2: {semana2}")
    print(f"Promedio semana 2: {sum(semana2)/len(semana2):.1f}°C")
    
    # Temperaturas más altas y más bajas
    temp_ordenadas = sorted(temperaturas)
    print(f"3 temperaturas más bajas: {temp_ordenadas[:3]}")
    print(f"3 temperaturas más altas: {temp_ordenadas[-3:]}")

ejercicios_segmentacion()

print("\n" + "="*80)
print("10. FUNCIONES ÚTILES PARA SEGMENTACIÓN")
print("="*80)

def mostrar_funciones_utiles():
    """
    🎯 CONSEJO: Estas funciones complementan muy bien la segmentación
    """
    
    datos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Datos:", datos)
    
    # Combinar con len()
    mitad = len(datos) // 2
    print(f"Mitad: {mitad}")
    print(f"Primera mitad: {datos[:mitad]}")
    print(f"Segunda mitad: {datos[mitad:]}")
    
    # Combinar con min() y max()
    print(f"Valor mínimo: {min(datos)}")
    print(f"Valor máximo: {max(datos)}")
    print(f"Suma total: {sum(datos)}")
    
    # Combinar con sorted()
    desordenados = [45, 12, 78, 23, 67, 34, 89, 56]
    print(f"\nDesordenados: {desordenados}")
    ordenados = sorted(desordenados)
    print(f"Ordenados: {ordenados}")
    print(f"Primeros 3 (menores): {ordenados[:3]}")
    print(f"Últimos 3 (mayores): {ordenados[-3:]}")
    
    # Combinar con enumerate()
    print(f"\nCon enumerate():")
    for i, valor in enumerate(datos[:5]):  # Solo los primeros 5
        print(f"  Posición {i}: {valor}")

mostrar_funciones_utiles()

print("\n" + "="*80)
print("11. ERRORES COMUNES Y CÓMO EVITARLOS")
print("="*80)

def errores_comunes():
    """
    🎯 CONSEJO: Aprende de estos errores típicos para evitarlos
    """
    
    lista = [1, 2, 3, 4, 5]
    print("Lista de ejemplo:", lista)
    
    print("\n❌ ERRORES COMUNES:")
    
    # Error 1: Confundir que el índice final NO se incluye
    print("1. lista[1:3] NO incluye el índice 3:")
    print(f"   lista[1:3] = {lista[1:3]} (elementos en posiciones 1 y 2)")
    
    # Error 2: Índices fuera de rango (en slicing NO da error, pero puede ser inesperado)
    print("2. Índices fuera de rango en slicing:")
    print(f"   lista[10:20] = {lista[10:20]} (lista vacía, no error)")
    print(f"   lista[-10:2] = {lista[-10:2]} (toma desde el inicio)")
    
    # Error 3: Confundir paso positivo con negativo
    print("3. Diferencia entre pasos positivos y negativos:")
    print(f"   lista[1:4:1] = {lista[1:4:1]} (hacia adelante)")
    print(f"   lista[4:1:-1] = {lista[4:1:-1]} (hacia atrás)")
    
    print("\n✅ CONSEJOS PARA EVITAR ERRORES:")
    print("   • Recuerda: [inicio:fin) - el fin NO se incluye")
    print("   • Para invertir usa [::-1]")
    print("   • Para obtener elementos desde el final usa índices negativos")
    print("   • Siempre verifica la longitud de tu lista primero")

errores_comunes()

print("\n" + "="*80)
print("12. EJERCICIOS PARA PRACTICAR")
print("="*80)

def ejercicios_practica():
    """
    🎯 CONSEJO: Practica con estos ejercicios
    """
    
    print("🎯 EJERCICIOS PARA QUE PRACTIQUES:")
    print()
    
    # Datos para practicar
    numeros = list(range(1, 21))  # [1, 2, 3, ..., 20]
    print("Lista para practicar:", numeros)
    
    print("\n📝 EJERCICIOS (intenta resolverlos antes de ver las respuestas):")
    print("1. Obtén los primeros 5 números")
    print("2. Obtén los últimos 3 números")
    print("3. Obtén los números del 5 al 10 (inclusive)")
    print("4. Obtén los números en posiciones pares")
    print("5. Obtén los números en posiciones impares")
    print("6. Invierte toda la lista")
    print("7. Obtén los números del 15 al 8 (hacia atrás)")
    print("8. Obtén cada 3er número empezando desde el 2")
    
    print("\n🔍 RESPUESTAS:")
    print("1.", numeros[:5])
    print("2.", numeros[-3:])
    print("3.", numeros[4:10])  # Posiciones 4-9 = valores 5-10
    print("4.", numeros[::2])
    print("5.", numeros[1::2])
    print("6.", numeros[::-1])
    print("7.", numeros[14:7:-1])  # Desde posición 14 (valor 15) hasta posición 8
    print("8.", numeros[1::3])  # Desde posición 1, cada 3

ejercicios_practica()

print("\n" + "="*80)
print("🎯 RESUMEN DE SEGMENTACIÓN DE LISTAS")
print("="*80)
print("""
📋 SINTAXIS GENERAL: lista[inicio:fin:paso]

🔑 CONCEPTOS CLAVE:
   • inicio: Desde dónde empezar (incluido)
   • fin: Hasta dónde llegar (NO incluido)
   • paso: De cuánto en cuánto avanzar

💡 CASOS ESPECIALES:
   • [:n] → Primeros n elementos
   • [n:] → Desde n hasta el final
   • [::-1] → Lista completa invertida
   • [::2] → Elementos en posiciones pares
   • [-n:] → Últimos n elementos

⚠️ PUNTOS IMPORTANTES:
   • Los índices negativos cuentan desde el final
   • El índice 'fin' NUNCA se incluye
   • Si los índices están fuera de rango, no da error
   • El paso puede ser negativo (para ir hacia atrás)

🎯 CASOS DE USO COMUNES:
   • Dividir listas en partes
   • Obtener primeros/últimos elementos
   • Invertir listas
   • Filtrar por posición
   • Procesar datos por chunks/grupos

¡La segmentación es una herramienta MUY poderosa en Python!
¡Sigue practicando y úsala en tus proyectos reales!
""")
print("="*80)
