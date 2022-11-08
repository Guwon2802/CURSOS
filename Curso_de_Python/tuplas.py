'''
Las tuplas son listas inmutables.
Se usan con parentesis.
'''

tupla = (1,2,3,4,[2,4,6],"Hola","Gabriel",1,2,3)

print(tupla) #Se puede imprimir la tupla.

print(tupla[4]) #Se puede buscar por indice. Tambien con negativos.

print(tupla[2:]) #Se puede buscar desde un punto hasta otro.

print(4 in tupla) #Se puede comprobar si esta un valor.

print(tupla.index(4)) #Se puede buscar el indice de un valor.

print(tupla.count(4)) #Se puede saber cuantas veces se repite un valor.

print(len(tupla)) #Se puede saber cuantos elementos hay.

lista = list(tupla) #Asi convertis una tupla en una lista.
print(lista)

tupla = tuple(lista)
print(tupla) #Asi convertis una lista en una tupla.