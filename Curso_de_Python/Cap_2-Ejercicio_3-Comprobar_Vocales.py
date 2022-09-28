# Capitulo 2: Condicionales

'''
EJERCICIO 3:
Hacer un programa que pida un caracter e indique si es una vocal o no.
'''

letra = input("Coloque una letra: ").lower() # El ".lower()" hace que lo que el usuario coloco se tranforme en minuscula.

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print(f"Es una vocal")
else:
    print(f"No es una vocal")
