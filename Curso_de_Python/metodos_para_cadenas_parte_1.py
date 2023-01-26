cadena = "hola Mundo 1000" 

print(cadena.upper()) #Todo mayuscula.

print(cadena.lower()) #Todo minuscula.

print(cadena.capitalize()) #Primera letra en mayuscula.

print(cadena.title()) #Primera letra de cada palabra en mayuscula.

print(cadena.count('a')) #Cuenta caracteres o palabras.

print(cadena.find('o')) #Busca el primer caracter o palabra y te dice el indice.
print(cadena.rfind('o')) #Lo mismo pero con la ultima.

#Resultados booleanos(True,False)
print(cadena.isdigit()) #Si solo hay caracteres numericos.
print(cadena.isalpha()) #Si solo hay caracteres alfabeticos.
print(cadena.isalnum()) #Si solo hay caracteres alfanumericos.
print(cadena.islower()) #Si todo esta en minuscula.
print(cadena.isupper()) #Si todo esta en mayuscula.
print(cadena.istitle()) #Si la primera letra de cada palabra esta en mayuscula.
print(cadena.isspace()) #Si toda la cadena son espacios.