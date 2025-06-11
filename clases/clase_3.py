# variables acumuladoras
# Se utiliza para acumular valores en una variable, por ejemplo, para sumar los sueldos de los empleados

i = 1
suma = 0

while i <= 35:
    nota = int(input("ingrese la nota del alumno: "))
    if nota >= 0 and nota <= 10:
        print("la nota no es valida")
    else:
        suma += nota
print("la suma de las notas es: ", suma) 