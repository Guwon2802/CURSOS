#Capitulo 3: Colecciones

'''
EJERCICIO 2:
Escriba un programa que tenga dos listas y que, a continuacion, cree las listas (en las que no debe haber repeticiones):
-> Lista de elementos que aparecen en las dos listas
-> Lista de elementos que aparecen en la primera lista, pero no en la segunda
-> Lista de elementos que aparecen en la segunda lista, pero no en la primera
-> Lista de elementos que aparecen en ambas listas
'''

#PROGRAMA

lista = [1,2,3,4,"Gabriel","Maria",1,2,3,4,"Gabriel","Maria"]
lista2 = [3,4,5,6,"Gabriel","Acuña",3,4,5,6,"Gabriel","Acuña",]

#Elimine los elementos repetidos de las listas
a = set(lista)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(f"Lista de elementos que aparecen en las dos listas: {union}")
print(f"Lista de elementos que aparecen en la primera lista, pero no en la segunda: {soloA}")
print(f"Lista de elementos que aparecen en la segunda lista, pero no en la primera: {soloB}")
print(f"Lista de elementos que aparecen en ambas listas: {interseccion}")