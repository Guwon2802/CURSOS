#Capitulo 5: Cadenas

'''
Ejercicio 2:
Hacer un programa para detectar si una frase introducida por el usuario finaliza con un "." o no.
Deberas imprimir por la consola una de las siguientes opciones; 
"Termina con un punto" o por el contrario "No termina con un punto".
'''

#PROGRAMA

cadena = input("Digite una frase: ")

if cadena.endswith("."):
    print("\nTermina con un punto")
else:
    print("\nNo termina con un punto")