#Capitulo 1: Elementos Basicos

'''
EJERCICIO 4:
Hacer un programa para ingresar el radio de un circulo y se resporte su area y la longitud de la circunferencia
'''

#PROGRAMA

import math

r = float(input("Coloque el radio del circulo: "))

area = math.pi * r**2

longitud= 2 * math.pi * r

print(f"El valor del area es: {area:.2f}") #Asi haces que te muestre solamente la cantidad de decimales que queres
print(f"El valor de la longitud es: {longitud:.2f}")