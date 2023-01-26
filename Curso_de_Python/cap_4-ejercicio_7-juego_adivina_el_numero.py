#Capitulo 4: Bucles

'''
EJERCICIO 6:
Realizar un juego para adivinar un numero. Para ello generar un numero aleatorio entre 0-100 y luego ir pidiendo numeros indicando "es mayor"
o "es menor" segun sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta y mostrar el numero de intentos
'''

#PROGRAMA

import random

aleatorio = random.randint(0,100) #Generamos un numero aleatorio

print("\t.:Juego adivina el numero:.")

contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero>aleatorio:
        print("\tNo es el numero, digite un numero menor")
    elif numero<aleatorio:
        print("\tNo es el numero, digite un numero mayor")
    else:
        print(f"\tFelicitades, acabas de adivinar el numero {aleatorio}")
        break

print(f"\nNumero de intentos: {contador}")