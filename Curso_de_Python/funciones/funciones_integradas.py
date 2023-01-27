'''
Sirven para hacer converciones entre tipos de datos.
'''

#Valor de tipo "str" a "int"
a = int("10")
print(f"Tu valor en entero '{a}'")


#Valor de tipo "str" a "float"
b = float("10.8")
print(f"Tu valor en float '{b}'")


#Valor de tipo "int" a "str". Tambien se puede con los "float"
c = str(10)
print(f"Tu valor en cadena '{c}'")


#Primeros dos caracteres indican que sera un valor binario.
d = bin(10)
print(f"Tu valor en binario '{d}'")


#Primeros dos caraceteres indican que sera un valor hexadecimal.
e = hex(10)
print(f"Tu valor en hexadecimal '{e}'")


#Valor "binario" a "int". Segundo parametro(2) indica en que base esta.
f = int("0b1010",2)
print(f"Tu valor binario a entero '{f}'")


#Valor "hexadecimal" a "int". Segundo parametro indica en que base esta.
g = int("0xb",16)
print(f"Tu valor hexadecimal a entero '{g}'")


#Valor absoluto de un numero. Distancia del numero hasta el 0, siempre en positivo
h = abs(-8)
print(f"Tu valor absoluto '{h}'")


#Redonde el numero hasta el mas cercano.
i = round(8.6)
print(f"Tu valor redondeado '{i}'")


#Cantidad de caracteres de la palabra.
j = len("Gabriel")
print(f"La cantidad de caracteres es '{j}'")