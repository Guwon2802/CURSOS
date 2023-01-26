'''
Tiene un numero indeterminado de interacciones donde solo hace falta que se cumpla una determinada condicion para que el bucle se repita las veces necesarias
'''

#Bucle indeterminado(Se repite las veces que sean necesarias)
import math

numero = int(input("Digite un numero: "))

#Significa "mientras". Mientras la condicion se cumpla, se seguira ejecutando el bucle
while numero<0: 
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

#Usando "math.sqrt(numero)" se saca la raiz
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}") 



#Bucle determinado(Se repite las veces que quieras)
i = 0

#El bucle se repetira mientras el valor de "i" sea menor a 10
while i<10:
    print("Hola mundo")
    #Le sumamos 1 a cada repeticion asi no se hace infinito
    i += 1 