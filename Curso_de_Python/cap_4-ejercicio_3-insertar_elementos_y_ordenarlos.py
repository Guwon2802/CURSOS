#Capitulo 4: Bucles

'''
EJERCICIO 3:
Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por ultimo, muestra los numeros ordenados de menor a mayor.
'''

lista = []

salir = False

while not salir:
    numero = int(input("Digite un numero: "))
    if numero==0:
        salir = True
    else:
        lista.append(numero)

lista.sort()

print(f"\nLista ordenada: \n{lista}")