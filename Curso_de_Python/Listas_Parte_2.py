# Segunda parte de las listas.

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",34,1.34,[1,2,3],True]

print(f"LISTA: {len(lista)}") #Te imprime la cantidad de elementos que hay en la lista.

####################################################################################################################################

lista2 = [1,2,3,4,5]

lista2.append(6) #Agrega aun elemento a tu lista, lo agrega al final.

print(f"LISTA2: {lista2}")

####################################################################################################################################

lista3 = [1,2,4,5,6,7]

lista3.insert(2,3) #Agrega un elemento a tu lista en la posicion que vos le indiques.
                   #El primer parametro es en el indice donde lo queres agregar. El segundo es el valor que queres agregar.

print(f"LISTA3{lista3}")

####################################################################################################################################

lista4 = [1,2,3,4]

lista4.extend ([5,6,7,8]) #Agrega varios elementos a la lista.

print(f"LISTA4: {lista4}")

####################################################################################################################################

lista1 = [9,8,7,6]
lista2 = [5,4,3,2]

lista5 = lista1+lista2 #Asi sumas listas.

print(f"LISTA5: {lista5}")

####################################################################################################################################

lista6 = [1,2,3,4,5]

print(f"LISTA6: {3 in lista6}") #Con el condicional "in" podes comprobar si un elemento esta en una lista. 

####################################################################################################################################

lista7 = [1,2,3,4,5,6]

print(f"LISTA7: {lista7.index(4)}") #Te muestra en que indice esta el elemento.

####################################################################################################################################

lista8 = [1,2,3,4,1,1,2,3]

print(f"LISTA8: {lista8.count(1)}") #Te muestra cuantas veces se repite ese elemento en la lista.

####################################################################################################################################

lista9 = [1,2,3,4,5,6]

lista9.pop(3) #Elimina el elemento que este dentro del indice que le indiques. Si lo dejas vacio, elimina el ultimo elemento.

print(f"LISTA9: {lista9}")

####################################################################################################################################

lista10 = [1,2,3,4,5]

lista10.remove(2) #Elimina el elemento de la lista que le indiques.

print(f"LISTA10: {lista10}")

####################################################################################################################################

lista11 = [1,2,3,4,5,6,7,8,9,"Gabriel"]

lista11.clear() #Elimina todos los elementos de la lista.

print(f"LISTA11: {lista11}")

####################################################################################################################################

lista12 = [1,3,4,5,6,"Gabriel"]

lista12.reverse() #Invierte la lista

print(f"LISTA12: {lista12}")

####################################################################################################################################

lista13 = [2,6,7,4,-6,-1,8]

lista13.sort() #La ordena de forma ascendente

print(f"LISTA13: {lista13}")

####################################################################################################################################

lista14 = [2,6,7,4,-6,-1,8]

lista14.sort(reverse=True) #La ordena de forma descendente

print(f"LISTA14: {lista14}")

####################################################################################################################################

lista15 = [1,2,3,4,5,"Gabriel"]*2 #Asi haces que se copien los elementos de la lista la cantidad de veces que quieras.

print(f"LISTA15: {lista15}")

####################################################################################################################################