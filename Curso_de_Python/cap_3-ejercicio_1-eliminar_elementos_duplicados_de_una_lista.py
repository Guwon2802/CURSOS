#Capitulo 3: Colecciones

'''
EJERCICIO 1:
Escriba un programa donde tenga una lista y que, a continuacion, elimine los elementos repetidos, por ultimo mostrar la lista.
'''

#Primer programa

lista = [1,2,1,2,3,4,3,4,6,5,7,6,7,8,5,4,3,2,6,7,8]

conjunto = set(lista)

lista = list(conjunto)

print(lista)


#Segundo programa

lista = [1,2,1,2,3,4,3,4,6,5,7,6,7,8,5,4,3,2,6,7,8,"Gabriel","Gabriel"]

lista = list(set(lista))

print(lista)