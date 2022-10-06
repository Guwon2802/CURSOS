'''
En las listas se pueden guardar valores enteros, flotantes, tipo cadena, booleanos y otras listas.
Los valores se ponen dentro de corchetes y se separan en comas.
'''

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",34,1.34,[1,2,3],True] #El indice de la lista comienza por el 0.

print(lista) #Asi se muestran todos los elementos de la lista.

print(lista[0:3]) #Separandolos por dos puntos puedes mostrar los elementos desde un punto hasta otro. Siempre te toma el segundo numero restandole 1.

print(lista[:4]) #Asi te muestra, desde el principio, hasta el indice que indiques.

print(lista[2:]) #Asi te muestra, desde donde indiques, hasta el final.

print(lista[-1]) #Tambien puedes usar valores negativos. Comienza por "-1" desde derecha a izquierda.