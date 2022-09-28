'''
EJERCICIO 1:
Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son.
'''

num1 = int(input("Coloque el primer numero: "))
num2 = int(input("Coloque el segundo numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
if num1%2==0:
    print("El primer numero es par")
    