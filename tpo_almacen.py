# ==============================================================================
# UNIVERSIDAD ARGENTINA DE LA EMPRESA (UADE)
# Departamento de Tecnología Informática
# Introducción Algoritmia
#
# Trabajo Práctico Python
# Ejemplo 1: Tema Análisis de Ventas Online
#
# RESTRICCIÓN CLAVE: Solo conceptos básicos de Python,
#                     sin imports ni funcionalidades avanzadas.
# ==============================================================================

# --- CONSTANTES ---
ID_PRODUCTO = 0
CATEGORIA = 1
PRECIO = 2
CANTIDAD_VENDIDA = 3
FECHA_VENTA = 4


# --- FUNCIONES DE UTILIDAD PARA LA UI (SIN IMPORTS) ---

def simular_limpiar_consola():
    """Simula una limpieza de consola imprimiendo muchas líneas vacías."""
    print('\n' * 50) 

def imprimir_linea_horizontal(caracter, longitud):
    """Imprime una linea horizontal de caracteres."""
    print(caracter * longitud)

def imprimir_titulo_centrado(texto, longitud_total, caracter_borde=' '):
    """Imprime un texto centrado con relleno a los lados."""
    espacios_laterales = (longitud_total - len(texto)) // 2
    texto_centrado = caracter_borde * espacios_laterales + texto + caracter_borde * (longitud_total - len(texto) - espacios_laterales)
    print(texto_centrado)

def imprimir_banner_inicio():
    """Imprime un banner de bienvenida más elaborado."""
    simular_limpiar_consola()
    ancho = 80
    
    imprimir_linea_horizontal("═", ancho)
    imprimir_titulo_centrado(" ", ancho, "║")
    imprimir_titulo_centrado("  📊 SISTEMA DE ANÁLISIS DE VENTAS 📊  ", ancho, "║")
    imprimir_titulo_centrado("  📈 TU ASISTENTE PARA DATOS DE NEGOCIO 📉  ", ancho, "║")
    imprimir_titulo_centrado(" ", ancho, "║")
    imprimir_linea_horizontal("═", ancho)

    print("\n")
    imprimir_titulo_centrado("Bienvenido a la herramienta definitiva para tus ventas.", ancho)
    imprimir_titulo_centrado("Analiza tus datos y toma decisiones inteligentes.", ancho)
    print("\n")
    imprimir_titulo_centrado("Presiona ENTER para comenzar...", ancho)
    input()
    simular_limpiar_consola()

def imprimir_encabezado_seccion(titulo, caracter_borde_arriba="=", caracter_borde_abajo="-"):
    """Imprime un encabezado de sección con diseño."""
    ancho = 70
    print("\n")
    imprimir_linea_horizontal(caracter_borde_arriba, ancho)
    imprimir_titulo_centrado("✨ " + titulo.upper() + " ✨", ancho)
    imprimir_linea_horizontal(caracter_borde_abajo, ancho)

def imprimir_mensaje_con_marco(mensaje, tipo="normal"):
    """Imprime un mensaje con un marco y un icono, con pausa."""
    icono = "💬"
    caracter = "-"
    if tipo == "exito":
        icono = "✅"
        caracter = "─"
    elif tipo == "error":
        icono = "❌"
        caracter = "═"
    
    longitud_mensaje = len(mensaje)
    ancho_marco = longitud_mensaje + 10 # Ancho ajustado al mensaje
    
    print("\n")
    imprimir_linea_horizontal(caracter, ancho_marco)
    imprimir_titulo_centrado(icono + " " + mensaje + " " + icono, ancho_marco)
    imprimir_linea_horizontal(caracter, ancho_marco)
    
    if tipo == "error":
        print("Presiona ENTER para reintentar...")
    else:
        print("Presiona ENTER para continuar...")
    input()
    print("\n" * 2) # Mas saltos de linea para separar

def simular_procesando_texto(mensaje):
    """Simula un proceso de carga imprimiendo puntos suspensivos secuencialmente."""
    print("\n" + mensaje, end="") # 'end=""' para no saltar linea
    print(".", end="")
    input() # Esperar Enter
    print(".", end="")
    input() # Esperar Enter
    print(".", end="")
    input() # Esperar Enter
    print(" ¡Listo!")
    print("\n")

# --- FUNCIONES DE LÓGICA DE NEGOCIO (Sin cambios internos, solo llamadas a UI) ---

def cargar_ventas():
    """Permite al usuario cargar información de ventas."""
    ventas = []
    
    imprimir_encabezado_seccion("Ingreso de Datos de Ventas", caracter_borde_arriba="#", caracter_borde_abajo="#")
    print("\nPor favor, ingresa los detalles de cada transacción.")
    
    cantidad_valida = False
    cantidad = 0
    while not cantidad_valida:
        try:
            texto_cantidad = input("\n👉 Cuantas ventas deseas registrar (minimo 1 para el analisis)?: ")
            cantidad = int(texto_cantidad)
            if cantidad >= 1:
                cantidad_valida = True
            else:
                imprimir_mensaje_con_marco("Cantidad invalida. Ingresa un numero positivo.", "error")
                simular_limpiar_consola()
                imprimir_encabezado_seccion("Ingreso de Datos de Ventas", caracter_borde_arriba="#", caracter_borde_abajo="#")
        except ValueError:
            imprimir_mensaje_con_marco("Error: Entrada no numerica. Ingresa un numero entero.", "error")
            simular_limpiar_consola()
            imprimir_encabezado_seccion("Ingreso de Datos de Ventas", caracter_borde_arriba="#", caracter_borde_abajo="#")

    for i in range(cantidad):
        simular_limpiar_consola() # Limpia para cada nueva venta
        imprimir_encabezado_seccion("Datos de Venta #" + str(i + 1) + " de " + str(cantidad), caracter_borde_arriba="─", caracter_borde_abajo="─")
        
        # ID del producto
        id_prod_valido = False
        id_prod = 0
        while not id_prod_valido:
            try:
                texto_id = input("    ▶️ ID del producto (ej. 101): ")
                id_prod = int(texto_id)
                if id_prod >= 0:
                    id_prod_valido = True
                else:
                    imprimir_mensaje_con_marco("Error: El ID del producto no puede ser negativo.", "error")
            except ValueError:
                imprimir_mensaje_con_marco("Error: El ID debe ser un numero entero.", "error")
        
        # Categoria del producto
        cat_valida = False
        cat = ""
        while not cat_valida:
            cat = input("    ▶️ Categoria del producto (ej. 'Electronica', 'Ropa'): ")
            if len(cat) > 0:
                cat_valida = True
            else:
                imprimir_mensaje_con_marco("Error: La categoria del producto no puede estar vacia.", "error")
        
        # Precio
        precio_valido = False
        precio = 0.0
        while not precio_valido:
            try:
                texto_precio = input("    ▶️ Precio del producto (ej. 199.99): ")
                precio = float(texto_precio)
                if precio >= 0:
                    precio_valido = True
                else:
                    imprimir_mensaje_con_marco("Error: El precio no puede ser negativo.", "error")
            except ValueError:
                imprimir_mensaje_con_marco("Error: El precio debe ser un numero decimal.", "error")
        
        # Cantidad vendida
        cant_valida = False
        cant = 0
        while not cant_valida:
            try:
                texto_cant = input("    ▶️ Cantidad vendida (ej. 2): ")
                cant = int(texto_cant)
                if cant >= 0:
                    cant_valida = True
                else:
                    imprimir_mensaje_con_marco("Error: La cantidad no puede ser negativa.", "error")
            except ValueError:
                imprimir_mensaje_con_marco("Error: La cantidad vendida debe ser un numero entero.", "error")
        
        # Fecha de venta
        fecha_valida = False
        fecha = ""
        while not fecha_valida:
            fecha = input("    ▶️ Fecha de venta (dd-mm-aaaa, ej. 01-01-2023): ")
            if len(fecha) > 0:
                fecha_valida = True
            else:
                imprimir_mensaje_con_marco("Error: La fecha de venta no puede estar vacia.", "error")
        
        venta = [id_prod, cat, precio, cant, fecha]
        ventas.append(venta)
        imprimir_mensaje_con_marco("Venta #" + str(i + 1) + " cargada correctamente.", "exito")
            
    return ventas


def total_ingresos(ventas):
    total = 0.0
    for venta in ventas:
        ingreso_venta = venta[PRECIO] * venta[CANTIDAD_VENDIDA]
        total = total + ingreso_venta
    return total


def total_prod_cat_vend(ventas, categoria_buscada):
    total_productos_vendidos = 0
    # Transformar categoria_buscada a minusculas de forma basica
    categoria_buscada_minusculas = ""
    for caracter in categoria_buscada:
        if ord(caracter) >= 65 and ord(caracter) <= 90:
            categoria_buscada_minusculas = categoria_buscada_minusculas + chr(ord(caracter) + 32)
        else:
            categoria_buscada_minusculas = categoria_buscada_minusculas + caracter

    for venta in ventas:
        categoria_venta = venta[CATEGORIA]
        categoria_venta_minusculas = ""
        for caracter_v in categoria_venta:
            if ord(caracter_v) >= 65 and ord(caracter_v) <= 90:
                categoria_venta_minusculas = categoria_venta_minusculas + chr(ord(caracter_v) + 32)
            else:
                categoria_venta_minusculas = categoria_venta_minusculas + caracter_v

        if categoria_buscada_minusculas == categoria_venta_minusculas:
            total_productos_vendidos = total_productos_vendidos + venta[CANTIDAD_VENDIDA]
    return total_productos_vendidos


def promedio_ingresos_diarios(ventas):
    ingresos_por_dia_fechas = []
    ingresos_por_dia_valores = []

    for venta in ventas:
        fecha = venta[FECHA_VENTA]
        ingreso_venta = venta[PRECIO] * venta[CANTIDAD_VENDIDA]
        
        fecha_ya_registrada = False
        indice_fecha = 0
        while indice_fecha < len(ingresos_por_dia_fechas):
            if ingresos_por_dia_fechas[indice_fecha] == fecha:
                ingresos_por_dia_valores[indice_fecha] = ingresos_por_dia_valores[indice_fecha] + ingreso_venta
                fecha_ya_registrada = True
                break
            indice_fecha = indice_fecha + 1
        
        if not fecha_ya_registrada:
            ingresos_por_dia_fechas.append(fecha)
            ingresos_por_dia_valores.append(ingreso_venta)

    total_dias_con_ventas = len(ingresos_por_dia_fechas)
    
    total_ingresos_global = 0.0
    indice_valor = 0
    while indice_valor < len(ingresos_por_dia_valores):
        total_ingresos_global = total_ingresos_global + ingresos_por_dia_valores[indice_valor]
        indice_valor = indice_valor + 1

    if total_dias_con_ventas > 0:
        return total_ingresos_global / total_dias_con_ventas
    else:
        return 0.0


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    imprimir_banner_inicio() 

    ventas_registradas = cargar_ventas()

    if len(ventas_registradas) == 0:
        simular_limpiar_consola()
        imprimir_mensaje_con_marco("🚫 ANÁLISIS CANCELADO: No hay ventas para procesar. 🚫", "error")
        print("¡Gracias por usar nuestro sistema! Hasta la proxima.")
        input("Presiona ENTER para salir...")
    else:
        simular_procesando_texto("Procesando los datos de ventas") # Simula "carga"
        simular_limpiar_consola() 

        imprimir_encabezado_seccion("Resultados del Análisis de Ventas", caracter_borde_arriba="═", caracter_borde_abajo="═")

        # 1. Total de ingresos
        ingresos_totales = total_ingresos(ventas_registradas)
        # Formato de dos decimales manual (sin separador de miles)
        ingresos_totales_str = str(int(ingresos_totales * 100) / 100.0)
        if ingresos_totales_str.find('.') == -1:
            ingresos_totales_str = ingresos_totales_str + ".00"
        elif len(ingresos_totales_str) - ingresos_totales_str.find('.') - 1 == 1:
            ingresos_totales_str = ingresos_totales_str + "0"
        
        print("\n" + "─" * 70)
        imprimir_titulo_centrado("📊 RESUMEN GENERAL DE INGRESOS 📊", 70)
        print("─" * 70)
        print("  Total de ingresos generados:   $" + ingresos_totales_str + " 💰")
        print("─" * 70)
        imprimir_mensaje_con_marco("Presiona ENTER para ver mas resultados.", "normal")


        # 2. Productos vendidos por categoria.
        imprimir_encabezado_seccion("Productos Vendidos por Categoría")
        
        # Extraer categorias unicas (logica basica sin set() ni sorted())
        categorias_existentes = []
        indice_venta_cat_unica = 0
        while indice_venta_cat_unica < len(ventas_registradas):
            categoria_actual = ventas_registradas[indice_venta_cat_unica][CATEGORIA]
            # Convertir a formato capitalizado basico
            cat_formato_basico = ""
            if len(categoria_actual) > 0:
                if ord(categoria_actual[0]) >= 97 and ord(categoria_actual[0]) <= 122:
                    cat_formato_basico = cat_formato_basico + chr(ord(categoria_actual[0]) - 32)
                else:
                    cat_formato_basico = cat_formato_basico + categoria_actual[0]
                
                indice_caracter_restante = 1
                while indice_caracter_restante < len(categoria_actual):
                    caracter_restante = categoria_actual[indice_caracter_restante]
                    if ord(caracter_restante) >= 65 and ord(caracter_restante) <= 90:
                        cat_formato_basico = cat_formato_basico + chr(ord(caracter_restante) + 32)
                    else:
                        cat_formato_basico = cat_formato_basico + caracter_restante
                    indice_caracter_restante = indice_caracter_restante + 1

            encontrada_en_unicas = False
            indice_unica = 0
            while indice_unica < len(categorias_existentes):
                if categorias_existentes[indice_unica] == cat_formato_basico:
                    encontrada_en_unicas = True
                    break
                indice_unica = indice_unica + 1
            
            if not encontrada_en_unicas:
                categorias_existentes.append(cat_formato_basico)
            indice_venta_cat_unica = indice_venta_cat_unica + 1
        
        # Ordenar categorias existentes (Bubble Sort)
        for i in range(len(categorias_existentes) - 1):
            for j in range(len(categorias_existentes) - 1 - i):
                if categorias_existentes[j] > categorias_existentes[j+1]:
                    temp = categorias_existentes[j]
                    categorias_existentes[j] = categorias_existentes[j+1]
                    categorias_existentes[j+1] = temp

        if len(categorias_existentes) == 0:
            print("\n  No se encontraron categorias unicas en las ventas cargadas.")
        else:
            print("\n  Categorias disponibles para analisis:")
            indice_cat_disp = 0
            while indice_cat_disp < len(categorias_existentes):
                print("    - " + categorias_existentes[indice_cat_disp])
                indice_cat_disp = indice_cat_disp + 1

            opcion_cat_valida = False
            opcion_cat = ""
            while not opcion_cat_valida:
                opcion_cat = input("\n  🤔 Deseas ver el total de productos de TODAS las categorias (T) o de algunas ESPECIFICAS (E)? (T/E): ")
                # Convertir a mayusculas de forma basica
                opcion_cat_mayus = ""
                indice_char_opc = 0
                while indice_char_opc < len(opcion_cat):
                    char_opcion = opcion_cat[indice_char_opc]
                    if ord(char_opcion) >= 97 and ord(char_opcion) <= 122:
                        opcion_cat_mayus = opcion_cat_mayus + chr(ord(char_opcion) - 32)
                    else:
                        opcion_cat_mayus = opcion_cat_mayus + char_opcion
                    indice_char_opc = indice_char_opc + 1

                if opcion_cat_mayus == 'T' or opcion_cat_mayus == 'E':
                    opcion_cat_valida = True
                else:
                    imprimir_mensaje_con_marco("Opcion invalida. Por favor, ingresa 'T' o 'E'.", "error")
                    simular_limpiar_consola()
                    imprimir_encabezado_seccion("Productos Vendidos por Categoría")
                    print("\n  Categorias disponibles para analisis:")
                    indice_cat_disp_re = 0
                    while indice_cat_disp_re < len(categorias_existentes):
                        print("    - " + categorias_existentes[indice_cat_disp_re])
                        indice_cat_disp_re = indice_cat_disp_re + 1

            if opcion_cat_mayus == 'T':
                print("\n  --- Resultados Detallados por Categoria ---")
                print("  ╔" + "═"*30 + "╦" + "═"*20 + "╗")
                print("  ║ " + "Categoria".ljust(28) + " ║ " + "Unidades Vendidas".ljust(18) + " ║")
                print("  ╠" + "═"*30 + "╬" + "═"*20 + "╣")
                indice_cat_todos = 0
                while indice_cat_todos < len(categorias_existentes):
                    cat_nombre_actual = categorias_existentes[indice_cat_todos]
                    cant_total = total_prod_cat_vend(ventas_registradas, cat_nombre_actual)
                    print("  ║ " + cat_nombre_actual.ljust(28) + " ║ " + str(cant_total).ljust(18) + " ║")
                    indice_cat_todos = indice_cat_todos + 1
                print("  ╚" + "═"*30 + "╩" + "═"*20 + "╝")

            elif opcion_cat_mayus == 'E':
                num_categorias_valido = False
                num_categorias_a_mostrar = 0
                while not num_categorias_valido:
                    try:
                        texto_num_cat = input("\n  Cuantas categorias especificas deseas analizar?: ")
                        num_categorias_a_mostrar = int(texto_num_cat)
                        if num_categorias_a_mostrar >= 1:
                            num_categorias_valido = True
                        else:
                            imprimir_mensaje_con_marco("Por favor, ingresa un numero positivo.", "error")
                            simular_limpiar_consola()
                            imprimir_encabezado_seccion("Productos Vendidos por Categoría")
                            print("\n  Categorias disponibles para analisis:")
                            indice_cat_disp_re_2 = 0
                            while indice_cat_disp_re_2 < len(categorias_existentes):
                                print("    - " + categorias_existentes[indice_cat_disp_re_2])
                                indice_cat_disp_re_2 = indice_cat_disp_re_2 + 1
                            print("\n  --- Analisis de Categorias Especificas ---")
                    except ValueError:
                        imprimir_mensaje_con_marco("Entrada invalida. Ingresa un numero entero.", "error")
                        simular_limpiar_consola()
                        imprimir_encabezado_seccion("Productos Vendidos por Categoría")
                        print("\n  Categorias disponibles para analisis:")
                        indice_cat_disp_re_3 = 0
                        while indice_cat_disp_re_3 < len(categorias_existentes):
                            print("    - " + categorias_existentes[indice_cat_disp_re_3])
                            indice_cat_disp_re_3 = indice_cat_disp_re_3 + 1
                        print("\n  --- Analisis de Categorias Especificas ---")

                print("\n  --- Analisis de Categorias Especificas ---")
                for i in range(num_categorias_a_mostrar):
                    categoria_a_buscar_valida = False
                    categoria_a_buscar = ""
                    while not categoria_a_buscar_valida:
                        categoria_a_buscar = input("  Ingresa el nombre de la Categoria #" + str(i+1) + ": ")
                        if len(categoria_a_buscar) > 0:
                            cant_total = total_prod_cat_vend(ventas_registradas, categoria_a_buscar)
                            # Formato capitalizado de forma basica
                            cat_mostrada = ""
                            if len(categoria_a_buscar) > 0:
                                if ord(categoria_a_buscar[0]) >= 97 and ord(categoria_a_buscar[0]) <= 122:
                                    cat_mostrada = cat_mostrada + chr(ord(categoria_a_buscar[0]) - 32)
                                else:
                                    cat_mostrada = cat_mostrada + categoria_a_buscar[0]
                                
                                indice_caracter_mostrar = 1
                                while indice_caracter_mostrar < len(categoria_a_buscar):
                                    caracter_restante_mostrar = categoria_a_buscar[indice_caracter_mostrar]
                                    if ord(caracter_restante_mostrar) >= 65 and ord(caracter_restante_mostrar) <= 90:
                                        cat_mostrada = cat_mostrada + chr(ord(caracter_restante_mostrar) + 32)
                                    else:
                                        cat_mostrada = cat_mostrada + caracter_restante_mostrar
                                    indice_caracter_mostrar = indice_caracter_mostrar + 1

                            print("    ➡️  '" + cat_mostrada + "': " + str(cant_total) + " productos vendidos.")
                            categoria_a_buscar_valida = True
                        else:
                            imprimir_mensaje_con_marco("La categoria no puede estar vacia. Intenta de nuevo.", "error")
        
        # 3. Promedio diario de ingresos.
        imprimir_encabezado_seccion("Promedio de Ingresos Diarios")
        promedio_diario = promedio_ingresos_diarios(ventas_registradas)
        # Formato de dos decimales manual
        promedio_diario_str = str(int(promedio_diario * 100) / 100.0)
        if promedio_diario_str.find('.') == -1:
            promedio_diario_str = promedio_diario_str + ".00"
        elif len(promedio_diario_str) - promedio_diario_str.find('.') - 1 == 1:
            promedio_diario_str = promedio_diario_str + "0"
            
        print("\n" + "─" * 70)
        print("  📈 Promedio de ingresos por dia de actividad: $" + promedio_diario_str)
        print("─" * 70)
        imprimir_mensaje_con_marco("Presiona ENTER para finalizar el analisis.", "normal")


        # Mensaje de Finalizacion
        print("\n\n")
        imprimir_linea_horizontal("═", 80)
        imprimir_titulo_centrado(" ", 80, "║")
        imprimir_titulo_centrado("    🎉 ANÁLISIS DE VENTAS FINALIZADO CON ÉXITO 🎉    ", 80, "║")
        imprimir_titulo_centrado("       ¡Esperamos que esta información te sea útil!      ", 80, "║")
        imprimir_titulo_centrado(" ", 80, "║")
        imprimir_linea_horizontal("═", 80)
        print("\n" + "Gracias por usar el sistema. ¡Hasta la proxima!".center(80))
        input("\nPresiona ENTER para salir...")