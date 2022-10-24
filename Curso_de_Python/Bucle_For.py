'''
Es un bucle con un numero determinado de interacciones.
'''

for i in [10,6,2,22,"Gabriel"]: #Las veces que se repetira el bucle son iguales a la cantidad de elementos de la coleccion.
    print("Hola mundo")

for i in [10,6,2,22,"Gabriel"]: #Aqui una demostracion de como funciona el bucle for.
    print(f"Elemento: {i}")


lista = [10,2,5,7,"Acuña"] #Se pueden usar listas.
tupla = (15,32,67,82,"Ezequil") #Se pueden usar tuplas.
conjunto = {1,2,3,4,5} #Se pueden usar conjuntos.

for i in lista: #Se puede usar una variable que contenga la coleccion.
    print(f"Lista: {i}")

for i in tupla:
    print(f"Tupla: {i}")

for i in conjunto:
    print(f"Conjunto: {i}")



diccionario = {"Gabriel":18,"Maria":22,"Jose":19,"Jorge":24} #Se pueden usar diccionarios.

for i in diccionario:
    print(f"Diccionario: {i}") #Imprime las claves.

for i in diccionario:
    print(f"Diccionario: {diccionario[i]}") #Imprime los valores.

for i in diccionario:
    print(f"{i} -> {diccionario[i]}") #Muestra las claves y valores.

for clave,valor in diccionario.items(): #Muestra las claves y valores, de una forma mas sencilla.
    print(f"{clave} -> {valor}")


cadena = "Gabriel" #Se pueden usar cadenas.

for i in cadena:
    print(f"Hola") #Imprime igual a la cantidad de caracteres de la cadena.´

for i in cadena:
    print(f"{i}") #Imprime la cadena, caracter por caracter.

for i in cadena:
    print(f"{i}",end=" ") #Imprime caracter por caracter, en la misma linea y dejando un espacio.