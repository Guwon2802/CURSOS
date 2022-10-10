'''
Las tuplas son listas inmutables.
Se usan con parentesis.
'''

tupla = (1,2,3,4,[2,4,6],"Hola")

print(tupla) #Se puede imprimir la tupla.

###########################################################################

tupla2 = (1,2,3,4,[2,4,6],"Hola")

print(tupla2[4]) #Se puede buscar por indice. Tambien con negativos.

###########################################################################

tupla3 = (1,2,3,4,[2,4,6],"Hola")

print(tupla3[2:]) #Se puede buscar desde un punto hasta otro.

###########################################################################

tupla4 = (1,2,3,4,[2,4,6],"Hola")

print(4 in tupla4) #Se puede comprobar si esta un valor.

###########################################################################

tupla5 = (1,2,3,4,[2,4,6],"Hola")

print(tupla5.index(4)) #Se puede buscar el indice de un valor.

###########################################################################

tupla6 = (1,2,3,4,[2,4,6],"Hola")

print(tupla6.count(4)) #Se puede saber cuantas veces se repite un valor.

###########################################################################

tupla7 = (1,2,3,4,[2,4,6],"Hola")

print(len(tupla7)) #Se puede saber cuantos elementos hay.

###########################################################################

tupla8 = (1,2,3,4,[2,4,6],"Hola","Gabriel")
lista = list(tupla8) #Asi convertis una tupla en una lista.

print(lista)

###########################################################################

lista2 = [1,2,3,4,[2,4,6],"Hola","Gabriel",1,2,3]
tupla = tuple(lista2)

print(tupla) #Asi convertis una lista en una tupla.