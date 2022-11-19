'''
Son grupos de elementos desordenados.
No pueden haber duplicados.
'''
#Asi creas un conjunto vacio. Si usas llaves, sera un diccionario, no un conjunto.
conjunto = set() 
#Asi creas un conjunto con elementos.
conjunto = {1,2,3,"Gabriel",4.56} 


#Añadis elementos al conjunto. Los agrega de forma aleatoria.
conjunto.add(5)
conjunto.add("Acuña") 
conjunto.add(3.78)
print(f"Elementos añadidos: {conjunto}")


#Elimina un valor.
conjunto.discard(3) 
print(f"Valor eliminado: {conjunto}")


#Elimina todos lo elementos.
conjunto.clear() 
print(f"Eementos eliminados: {conjunto}")


#Saber si un elemento esta.
print(f"CONJUNTO4: {3 in conjunto}") 


#Saber si un valor no esta.
print(f"CONJUNTO5: {4 not in conjunto}") 