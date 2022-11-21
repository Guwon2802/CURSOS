equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristriano Ronaldo",17:"Mario Mandzukich"}

print()

#Primer parametro es la clave, el segundo es lo que mostrara si colocas una clave que no esta en el diccionario.
print(equipo.get(18,"El jugador no existe en este equipo"))

print()

#Busqueda directa.
print(f"Busqueda directa: {10 in equipo}")

print()

#Muestra todas las claves.
print(f"Claves: {equipo.keys()}") 

print()

#Muestra todos los valores.
print(f"Valores: {equipo.values()}") 

print()

#Te muestra todos los elementos dentro de parentesis. Que a su vez estan dentro de una tupla.
print(f"Todos los elementos: {equipo.items()}") 

print()

#Cuantos elementos hay.
print(f"Cuantos elementos hay: {len(equipo)}") 

print()

#Elimina todos los elementos.
equipo.clear() 
print(f"Elementos eliminados: {equipo}")