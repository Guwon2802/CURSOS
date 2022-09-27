# Sirven para hacer converciones entre tipos de datos.

a = int("10") # Asi conviertes un valor de tipo cadena en uno tipo entero.

print(f"Tu valor en entero '{a}'")


b = float("10.8") # Asi conviertes un valor de tipo cadena en uno tipo float.

print(f"Tu valor en float '{b}'")


c = str(10) # Asi conviertes un valor de tipo entero en uno tipo cadena. Tambien se pueden convertir los float.

print(f"Tu valor en cadena '{c}'")


d = bin(10) # Los primeros dos caracteres te indican que sera un valor binario.

print(f"Tu valor en binario '{d}'")


e = hex(10) # Los primeros dos caracteres te indican que sera un valor hexadecimal.

print(f"Tu valor en hexadecimal '{e}'")


f = int("0b1010",2) # Asi convertis un valor binario en un valor entero, el segundo parametro(el 2) es para indicar en que base esta.

print(f"Tu valor binario a entero '{f}'")


g = int("0xb",16) # Asi convertis un valor hexadecimal en un valor entero, en el segundo parametro indicas en que base esta.

print(f"Tu valor hexadecimal a entero '{g}'")


h = abs(-8) # Asi sacas el valor absoluto de un numero. Es la distacia que hay desde el numero hasta el 0, siempre en positivo.

print(f"Tu valor absoluto '{h}'")


i = round(8.6) # Te redondea un numero hacia el que este mas cerca. 6.6 esta mas cerca del 7.

print(f"Tu valor redondeado '{i}'")


j = len("Gabriel") # Te dice la cantidad de caracteres de la palabra.

print(f"La cantidad de caracteres es '{j}'")