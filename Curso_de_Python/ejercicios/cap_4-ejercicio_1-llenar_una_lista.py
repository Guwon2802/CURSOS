#Capitulo 4: Bucles

'''
EJERCICIO 1:
Llenar una lista con los numeros del 1 al 50, luego mostrar los elementos con un bucle for, los elementos deben mostrarse
de la siguiente manera:

1-2-3-4-5...-50
'''

#PROGRAMA 1

lista = []

#Agregamos a la lista los elementos del 1 al 50
i = 1
while i<=50:
    lista.append(i)
    i+=1

#Imprimiendo los elementos de la lista
for i in lista:
    print(i,end="-")


#Salto de linea
print() 


#PROGRAMA 2

#Agregamos a la lista los elementos del 1 al 50, de una manera mas facil
lista = list(range(1,51))

#Imprimiendo los elementos de la lista
for i in lista:
    print(i,end="-")