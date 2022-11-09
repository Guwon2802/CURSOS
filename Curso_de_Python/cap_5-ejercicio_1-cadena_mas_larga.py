#Capitulo 5: Cadenas

'''
Ejercicio 1:
Hacer un programa donde se debera imprimir por la consola la palabra con mas caracteres de dos palabras dadas. 
En el caso de que ambas palabras tengan la misma cantidad de caracteres, deberas mostrar el mensaje "Son iguales".
'''

#PROGRAMA

cadena1 = input("Digite una cadena: ")
cadena2 = input("Digite otra palabra: ")

if len(cadena1) > len(cadena2):
    print(f"\nLa cadena mas larga es: {cadena1}")
elif len(cadena2) > len(cadena1):
    print(f"\nLa cadena mas larga es: {cadena2}")
else:
    print("\nAmbas son iguales en longitud")