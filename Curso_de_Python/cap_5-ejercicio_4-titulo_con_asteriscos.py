#Capitulo 5: Cadenas

'''
Ejercicio 4:
Hacer un programa donde se reemplacen todos los espacios de una cadena por asteriscos y ademans cada palabra comience por mayuscula.
'''

#PROGRAMA

cadena = input("Digite una cadena: ")

cadena = cadena.title().replace(" ","*")

print(f"\nCadena modificada: {cadena}")