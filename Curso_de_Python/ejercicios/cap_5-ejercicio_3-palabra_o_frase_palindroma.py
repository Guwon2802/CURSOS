#Capitulo 5: Cadenas

'''
Ejercicio 3:
Hacer un programa que determine si una palabra o frase es palindroma.
Una cadena palindroma se lee igual de izquierda a derecha que se derecha a izquierda.
Ejemplos:
    - oso
    - reconocer
    - anita lava la tina
'''

#PROGRAMA

cadena = input("Digite una cadena: ")

#Primero, quitamos los espacios en blaco de la cadena
cadena = cadena.replace(" ","")

#Segundo, invertimos la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("La cadena es un palindromo")
else:
    print("La cadena NO es un palindromo")