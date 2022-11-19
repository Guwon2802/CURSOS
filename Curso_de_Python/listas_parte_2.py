'''
Segunda parte de las listas.
'''

lista = [1,2,3,4,5,6,7,34,1.34]

#Imprime la cantidad de elementos que hay.
print(f"Cantidad de elementos: {len(lista)}")

print()

#Agrega aun elemento al final.
lista.append(6) 
print(f"Elemento agregado al final: {lista}")

print()

#Agrega un elemento en la posicion que vos le indiques. Primer parametro, donde lo queres agregar. Segundo parametro, el valor a agregar.
lista.insert(2,3) 
print(f"Elemento agregado en la posicion deseada: {lista}")

print()

#Agrega varios elementos.
lista.extend ([5,6,7,8]) 
print(f"Elementos varios agregados: {lista}")

print()

#Sumas de listas.
lista2 = [5,4,3,2]

lista3 = lista+lista2 
print(f"Suma de listas: {lista3}")

print()

#Con el condicional "in" podes comprobar si un elemento esta en una lista. 
print(f"Comprobacion: {3 in lista}")

print()

#Te muestra en que indice esta el elemento.
print(f"Indice en el que esta: {lista.index(34)}") 

print()

#Te muestra cuantas veces se repite ese elemento en la lista.
print(f"Repeticion del elemento: {lista.count(1)}")

print()

#Elimina el elemento que este dentro del indice que le indiques. Si lo dejas vacio, elimina el ultimo elemento.
lista.pop(3)
print(f"Eliminacion dentro del indice: {lista}")

print()

#Elimina el elemento que le indiques.
lista.remove(1.34)
print(f"Eliminacion indicada: {lista}")

print()

#Invierte la lista.
lista.reverse()
print(f"Lista invertida: {lista}")

print()

#La ordena de forma ascendente.
lista.sort()
print(f"Ordenada ascendentemente: {lista}")

print()

#La ordena de forma descendente
lista.sort(reverse=True)
print(f"Ordenada descendentemente: {lista}")

print()

#Copia los elementos la cantidad indicada.
print(f"Elementos copiados: {lista*2}")

print()

#Elimina todos los elementos.
lista.clear()
print(f"Eliminacion completa: {lista}")