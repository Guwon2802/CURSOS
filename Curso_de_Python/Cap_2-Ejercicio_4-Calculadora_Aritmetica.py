# Capitulo 2: Condicionales

'''
EJERCICIO 4:
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas basicas (suma, resta, multiplicacion y devision). 
El usuario debe especificar la operacion con el primer caracter del nombre de la operacion.

S, s - Suma
R, r - Resta
P, p, M, m - Multiplicacion
D, d - Division
'''

num1 = float(input("Coloque un numero: "))
num2 = float(input("Coloque un numero: "))

operacion = input("Coloque la operacion: ").upper() # ".upper()" transforma todo lo que el usuario coloque, en mayuscula.

if operacion=='S':
    suma = num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion=='R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion=='P':
    producto = num1*num2
    print(f"\nEl producto es: {producto}")
elif operacion=='M':
    multiplicacion = num1*num2
    print(f"\nLa multiplicacion es: {multiplicacion:.2f}")
elif operacion=='D':
    division = num1/num2
    print(f"\nLa division es: {division:.2f}")
else:
    print("Se equivoco de operacion")