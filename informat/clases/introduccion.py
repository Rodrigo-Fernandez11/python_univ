#formas de comentar el codigo
'''
sknflanlfn
falsnfklasns
aksnfkasnf
'''
print("hello word")

#separador de texto
print("hola soy programador")
print()
print("hola soy estudiante de la universidad")

#variables : es un espacio en memoria que almacena un valor

#ram tengo la parte de los programas que se estan ejecutando, se guardan con una direccion de memoria
#iniciabilizar una variable significa que se le asigna un valor, python no necesita que se le asigne un tipo de dato
#python es un lenguaje de programacion debilmente tipado
#declarar es decir que tipo de dato es y inicializar es asignarle un valor
#int
numero = 10

#reglas para crear nombres de variables

#no se puede empezar con un numero
#no se puede tener espacios
#no se puede tener caracteres especiales
#no se puede tener palabras reservadas
#solo se puede tener letras, numeros y guion bajo
#no tiene problemas con mayusculas y minusculas
# deben evitarse nombre de variblaes llamdas l y O ya que se pueden confundir con 1 y 0

#tipode de datos que acepta python en una variable
#int
numero = 10 #entero
#float  numeros decimales
numero_decimal = 10.5
#string
cadena = "hola soy un string"
#boolean
verdadero = True
falso = False

#tipos de variables
#locales: solo se pueden usar en un bloque de codigo    (dentro de una funcion)
#globales: se pueden usar en cualquier parte del codigo (fuera de una funcion)

#constantes: son variables que no cambian su valor, que sea constante no significa que no se pueda cambiar su valor
#se deben declarar en mayusculas
PI = 3.141

# a una variable se le puede asignar el valor de otra variable
numero = 10

#asignacion de expresion expresion significa que .....

#ejemplo del uso de todos los operadores
numero1 = 10
numero2 = 5
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2

#orden de evaluacion
#potenciacio
#multiplicacion y division y modulo
#suma y resta
#signo menor

#ingresar datos por pantalla
#input() siempre devuelve un string
nombre = input("ingrese su nombre: ")
print("hola",nombre)

#convertir un string a un entero
numero = int(input("ingrese un numero: "))
print(numero)

#int() convierte un string a un entero
#float() convierte un string a un decimal
#str() convierte un entero o decimal a un string

#variables auxiliares
#se utilizan para hacer intercambio de valores
numero1 = 10
numero2 = 5
aux = numero1
numero1 = numero2
numero2 = aux
print(numero1)