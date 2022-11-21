a = {1,2,3,4,5,6,7,8}
b = {2,1,3,9,10,11,12,13,14}

print()

#Si 2 conjuntos tienen los mismo valores.
print(f"Mismos valores: {a == b}") 

print()

#Cuantos valores tiene.
print(f"Valores que tiene: {len(a)}")

print()

#Unir conjuntos.
c = a | b 
print(f"Conjuntos unidos: {c}")

print()

#Sacar la interseccion(los valores que tienen en comun).
c = a & b 
print(f"Interseccion: {c}")

print()

#Muestra la diferencia(valores que solo estan en "a").
c = a - b 
print(f"Diferencia: {c}")

print()

#Muestra la diferencia simetrica(valores que no tienen en comun).
c = a ^ b 
print(f"Diferencia simetrica: {c}")

print()

#Para saber si "a" es un subconjunto de "c".
c = {1,2,3,4,5,6,7,8,9,10}
print(f"Subconjunto: {a.issubset(c)}") 

print()

#Para saber si "c" es un superconjunto de "a".
c = {1,2,3,4,5,6,7,8,9,10}
print(f"Superconjunto: {c.issuperset(a)}") 

print()

#Para saber si no comparten ningun valor.
print(f"Comparten valor: {a.isdisjoint(b)}") 

print()

#Vuelves al conjunto inmutable.
a = frozenset({1,2,3,4,}) 