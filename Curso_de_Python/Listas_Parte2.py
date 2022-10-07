# Segunda parte de las listas.

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",34,1.34,[1,2,3],True]

print(len(lista)) #Te imprime la cantidad de elementos que hay en la lista.

############################################################

lista2 = [1,2,3,4,5]

lista2.append(6) #Agrega aun elemento a tu lista, lo agrega al final.

print(lista2)

############################################################

lista3 = [1,2,4,5,6,7]

lista3.insert(2,3) #Agrega un elemento a tu lista en la posicion que vos le indiques.
                   #El primer parametro es en el indice donde lo queres agregar. El segundo es el valor que queres agregar.

print(lista3)

############################################################

lista4 = [1,2,3,4]

lista4.extend ([5,6,7,8]) #Agrega varios elementos a la lista.

print(lista4)

############################################################

lista5 = [9,8,7,6]
lista6 = [5,4,3,2]

lista7 = lista5+lista6 #Asi sumas listas.

print(lista7)

############################################################

lista8 = [1,2,3,4,5]

print(3 in lista8) #Con el condicional "in" podes comprobar si un elemento esta en una lista. 

############################################################

lista9 = [1,2,3,4,5,6]

print(lista9.index(4)) #Te muestra en que indice esta el elemento.

############################################################

lista10 = (1,2,3,4,1,1,2,3)

print(lista.count(1)) #Te muestra cuantas veces se repite ese elemento en la lista.

############################################################

lista11 = (1,2,3,4,5,"Gabriel")*2 #Asi haces que se copien los elementos de la lista la cantidad de veces que quieras.

print(lista11)

############################################################