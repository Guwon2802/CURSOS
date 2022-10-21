'''
Tiene un numero indeterminado de interacciones donde solo hace falta que se cumpla una determinada condicion para que el bucle se repita las veces necesarias.
'''

#Bucle indeterminado(Se repite las veces que sean necesarias).

import math

numero = int(input("Digite un numero: "))

while numero<0: #Significa "mientras". Mientras la condicion se cumpla, se seguira ejecutando el bucle.
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}") #Usando "math.sqrt(numero)" se saca la raiz.



#Bucle determinado(Se repite las veces que quieras).

i = 0

#El bucle se repetira mientras el valor de "i" sea menor a 10.
while i<10:
    print("Hola mundo")
    i += 1 #Le sumamos 1 asi no se hace infinito.