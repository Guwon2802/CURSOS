'''
Las tuplas son listas inmutables.
Se usan con parentesis.
'''

tupla = (1,2,3,4,[2,4,6],"Hola","Gabriel",1,2,3)

#Imprimir tupla.
print(f"Tupla: {tupla}")


#Busqueda por indice. Tambien con negativos.
print(f"Busqueda por indice: {tupla[4]}")


#Busqueda desde un punto hasta otro.
print(f"Busqueda por rango: {tupla[2:]}")


#Comprobar si esta un valor.
print(f"Comprobacion: {4 in tupla}")


#Buscar el indice de un valor.
print(f"Busqueda del indice: {tupla.index(4)}") 


#Cuantas veces se repite un valor.
print(f"Repeticion: {tupla.count(4)}") 


#Cuantos elementos hay.
print(f"Cantidad de elementos: {len(tupla)}") 


#"tupla" a "lista".
lista = list(tupla) 
print(f"Tupla a lista: {lista}")


#"lista" a "tupla".
tupla = tuple(lista)
print(f"Lista a tupla: {tupla}") 