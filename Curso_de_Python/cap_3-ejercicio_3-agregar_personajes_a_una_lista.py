#Capitulo 3: Colecciones

'''
EJERCICIO 3:
Escriba un programa donde cree una lista con los siguientes personajes del Señor de los anillos
- Nombre: Aragon - Clase: Guerrero - Raza: Dunadan del Norte
- Nombre: Gandalf - Clase Mago - Raza: Istar
- Nombre: Legolas - Clase: Arquero - Raza: Elfo Sindar 
'''

#PROGRAMA

personajes = [] #Creamos una lista vacia

p = {"Nombre":"Aragon","Clase":"Guerrero","Raza":"Dunadan del Norte"}
personajes.append(p) #Agregamos el personaje a la lista

p = {"Nombre":"Gandalf","Clase":"Mago","Raza":"Istar"}
personajes.append(p) #Agregamos el personaje a la lista

p = {"Nombre":"Legolas","Clase":"Arquero","Raza":"Elfo Sindar"}
personajes.append(p) #Agregamos el personaje a la lista

print(personajes)