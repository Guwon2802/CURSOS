'''
Es un bucle con un numero determinado de interacciones
'''
print()

#Las repeticiones son iguales a la cantidad de elementos que tenga
for i in [10,6,2,22,"Gabriel"]: 
    print("Hola mundo")

print()

#Demostracion de como funciona el bucle for
for i in [10,6,2,22,"Gabriel"]: 
    print(f"Elemento: {i}")

print()

#Se pueden usar listas.
lista = [10,2,5,7,"Acuña"] 
#Se pueden usar tuplas.
tupla = (15,32,67,82,"Ezequil") 
#Se pueden usar conjuntos.
conjunto = {1,2,3,4,5} 

#Se puede usar una variable que contenga la coleccion
for i in lista: 
    print(f"Lista: {i}")

print()

for i in tupla:
    print(f"Tupla: {i}")

print()

for i in conjunto:
    print(f"Conjunto: {i}")

print()

#Se pueden usar diccionarios
diccionario = {"Gabriel":18,"Maria":22,"Jose":19,"Jorge":24} 

for i in diccionario:
    #Imprime las claves
    print(f"Diccionario: {i}") 

print()

for i in diccionario:
    #Imprime los valores
    print(f"Diccionario: {diccionario[i]}") 

print()

for i in diccionario:
    #Muestra las claves y valores
    print(f"{i} -> {diccionario[i]}") 

print()

#Muestra las claves y valores, de una forma mas sencilla
for clave,valor in diccionario.items(): 
    print(f"{clave} -> {valor}")

print()

#Se pueden usar cadenas
cadena = "Gabriel" 

for i in cadena:
    #Imprime igual a la cantidad de caracteres de la cadena
    print(f"Hola") 

print()

for i in cadena:
    #Imprime la cadena caracter por caracter
    print(f"{i}") 

print()

for i in cadena:
    #Imprime caracter por caracter, en la misma linea y dejando un espacio
    print(f"{i}",end=" ") 

print()