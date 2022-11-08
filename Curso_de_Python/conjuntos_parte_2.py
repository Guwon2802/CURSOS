a = {1,2,3,4,5,6,7,8}
b = {2,1,3,9,10,11,12,13,14}

print(a == b) #Saber si son iguales 2 conjuntos. Solo hace falta que tengan los mismo valores, el orden da igual


print(len(a)) #Saber cuantos valores tiene.


c = a | b #Unir conjuntos.
print(c)


c = a & b #Sacar la interseccion(los valores que tienen en comun).
print(c)


c = a - b #Muestra la diferencia(valores que solo estan en "a").
print(c)


c = a ^ b #Muestra la diferencia simetrica(valores que no tienen en comun).
print(c)


c = {1,2,3,4,5,6,7,8,9,10}
print(a.issubset(c)) #Para saber si "a" es un subconjunto de "c".


c = {1,2,3,4,5,6,7,8,9,10}
print(c.issuperset(a)) #Para saber si "c" es un superconjunto de "a".


print(a.isdisjoint(b)) #Para saber si no comparten ningun valor.


a = frozenset({1,2,3,4,}) #Vuelves al conjunto inmutable.