'''
En python se puede simular las pilas usando las listas.
En las pilas, se agregan elementos por el final y se sacan tambien por el final.
'''

pila = [1,2,3]

#Agregando elementos a la pila por el final

pila.append(4)
pila.append(5)
pila.append(6)

print(pila)

#Sacando elementos de la pila por el final

b = pila.pop()
print(f"Sacando el elemento {b}")
b = pila.pop()
print(f"Sacando el elemento {b}")
b = pila.pop()
print(f"Sacando el elemento {b}")

print(pila)