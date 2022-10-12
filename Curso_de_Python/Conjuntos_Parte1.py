'''
Son grupos de elementos desordenados.
No pueden haber duplicados.
'''

conjunto = set() #Asi creas un conjunto vacio, para despues agregarle cosas.

conjunto = {1,2,3,"Gabriel",4.56} #Asi creas un conjunto donde le colocaras valores.

conjunto.add(5)
conjunto.add("Acuña") #Añadis elementos al conjunto. Los agrega de forma aleatoria.
conjunto.add(3.78)

print(f"CONJUNTO: {conjunto}")

############################################################################################################

conjunto2 = {1,2,3,"Gabriel",4.56}

conjunto2.discard(3) #Elimina un valor.

print(f"CONJUNTO2: {conjunto2}")

############################################################################################################

conjunto3 = {1,2,3,"Gabriel",4.56}

conjunto3.clear() #Elimina todos lo elementos.

print(f"CONJUNTO3: {conjunto3}")

############################################################################################################

conjunto4 = {1,2,3,"Gabriel",4.56}

print(f"CONJUNTO4: {3 in conjunto4}") #Para saber si un elemento esta en el conjunto.

############################################################################################################

conjunto5= {1,2,3,"Gabriel",4.56}

print(f"CONJUNTO5: {4 not in conjunto5}") #Para saber si un valor no esta en el conjunto.