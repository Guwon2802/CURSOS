'''
En las listas se pueden guardar valores enteros, flotantes, tipo cadena, booleanos y otras listas.
Los valores se ponen dentro de corchetes y se separan en comas.
'''

#El indice de la lista comienza por el 0.
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",34,1.34,[1,2,3],True]

#Muestran todos los elementos de la lista.
print(lista)

#Separandolos por dos puntos puedes mostrar los elementos desde un punto hasta otro. Siempre te toma el segundo parametro restandole 1.
print(lista[0:3])

#Te muestra, desde el principio, hasta el indice que indiques.
print(lista[:4])

#Te muestra, desde donde indiques, hasta el final.
print(lista[2:])

#Puedes usar valores negativos. Comienza por "-1" desde derecha a izquierda.
print(lista[-1])