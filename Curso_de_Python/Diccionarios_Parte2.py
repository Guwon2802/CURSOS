equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristriano Ronaldo",17:"Mario Mandzukich"}

print(equipo.get(10,"El jugador no existe en este equipo")) #El primer parametro es la clave, el segundo es lo que mostrara si colocas una clave que no esta en el diccionario.

print(10 in equipo) #Busqueda directa.

print(equipo.keys()) #Muestra todas las claves.

print(equipo.values()) #Muestra todos los valores.

print(equipo.items()) #Te muestra todos los elementos dentro de parentesis. Que a su vez estan dentro de una tupla.

print(len(equipo)) #Cuantos elementos hay.

equipo.clear() #Elimina todos los elementos.
print(equipo)