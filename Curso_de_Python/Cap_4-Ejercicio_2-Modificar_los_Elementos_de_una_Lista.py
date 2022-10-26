#Capitulo 4: Bucles

'''
EJERCICIO 2:
Llenar una lista con los numeros del 1 al 10, luegos modificar los elementos de la lista multiplicandolos por un valor que el usuario digite.
'''

#PROGRAMA 1

lista = list(range(1,11))
print("Lista original: ")
for i in lista:
    print(i,end="-")

valor = int(input("\nValor a multiplicar: "))

#Multiplicar todos los elementos de la lista.
indice = 0
for i in lista:
    lista[indice] *= valor
    indice += 1


print(f"\nLista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i,end="-")

print()
print()

#PROGRAMA 2

# lista = list(range(1,11))
# print("Lista original: ")
# for i in lista:
#     print(i,end="-")

# valor = int(input("\nValor a multiplicar: "))

# #Multiplicar todos los elementos de la lista.
# for indice,i in enumerate(lista): #Hace lo mismo que el primer programa, pero sin crear el indice y sin estar sumandole valores.
#     lista[indice] *= valor


# print(f"\nLista final con los elementos multiplicados por {valor}")
# for i in lista:
#     print(i,end="-")