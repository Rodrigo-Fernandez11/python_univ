## programacion modular
# una funcion es un bloque de codigo que se puede reutilizar, nacieron por la especializacion de tareas
# las funciones en python se definen con la palabra reservada def, seguida del nombre de la funcion y los argumentos entre parentesis
# ejemplo de funcion en python
def suma(a, b):
    return a + b

# las funciones son llamadas por su nombre, y se les pasan los argumentos entre parentesis , para ser usadas en el programa principal
resultado = suma(5, 10)
print(resultado)  # imprime 15

# las funciones pueden tener argumentos por defecto, que se utilizan si no se pasan argumentos al llamar a la funcion
def suma_con_defecto(a, b=10):
    return a + b

resultado = suma_con_defecto(5)  # b toma el valor por defecto de 10

print(resultado)  # imprime 15

# el pasaje de parametros entre una funcion y el programa principal por posicion o por nombre, es decir, se pueden pasar los argumentos en el orden que se desee, o por su nombre
def suma_con_nombre(a, b=10):
    return a + b        

# return es una palabra reservada que indica el final de la funcion y devuelve el resultado al programa principal
# el return puede devolver varios valores, separados por comas, y se pueden asignar a variables diferentes
def suma_resta(a, b):
    return a + b, a - b 

resultado_suma, resultado_resta = suma_resta(5, 10)  # devuelve dos valores
print(resultado_suma)  # imprime 15
print(resultado_resta)  # imprime -5

# ventajas de las funciones:
# 1- evitan la repeticion de codigo, ya que se pueden reutilizar en diferentes partes del programa
# 2- facilitan la lectura y comprension del codigo, ya que se pueden dar nombres descriptivos a las funciones
# 3- permiten la modularidad del codigo, ya que se pueden agrupar funciones relacionadas en modulos o librerias
# 4- facilitan la depuracion y mantenimiento del codigo, ya que se pueden probar y depurar las funciones de forma independiente
# 5- permiten la recursion, es decir, una funcion puede llamarse a si misma para resolver un problema
# 6- permiten la programacion orientada a objetos, ya que se pueden definir metodos dentro de clases
# 7- permiten la programacion funcional, ya que se pueden pasar funciones como argumentos a otras funciones

# reglas de los nombres de funciones en python:
# 1- deben comenzar con una letra o un guion bajo
# 2- pueden contener letras, numeros y guiones bajos
# 3- no pueden contener espacios ni caracteres especiales
# 4- no pueden ser palabras reservadas de python
# 5- deben ser descriptivos y significativos, para facilitar la lectura y comprension del codigo

# parametros y argumentos:
# los parametros son las variables que se definen en la funcion, y los argumentos son los valores que se pasan a la funcion al llamarla

#parametros reales y formales:
# los parametros formales son los que se definen en la funcion, y los parametros reales son los que se pasan al llamar a la funcion
# los argumentos pueden ser posicionales o por nombre, es decir, se pueden pasar en el orden que se desee, o por su nombre
# los argumentos pueden ser obligatorios o opcionales, es decir, se deben pasar al llamar a la funcion, o se pueden omitir y tomar el valor por defecto

def calcularpromedio(a, b):
    total = (a + b) / 2
    return total

def imprimirpromedio(a, b):
    promedio = calcularpromedio(a, b)
    print("El promedio es:", promedio)
    