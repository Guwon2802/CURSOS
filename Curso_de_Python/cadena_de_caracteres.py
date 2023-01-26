cadena = "Hola mundo" #Esto es una cadena de texto
print(cadena)

cadena = '"Estoy" "Estudiando"' #Poder usar comillas dobles, dentro de comillas simples
print(cadena)

cadena = "Hola que \"tal?\"" #Pones delante "\" y no hara efecto
print(cadena)

cadena = "Estoy \tdurmiendo" #Tabulacion
print(cadena)

cadena = "Hola \nMundo" #Salto de linea
print(cadena)

cadena = r"D:\nombre\trabajo" #Guarda en crudo toda la cadena
print(cadena)

cadena = """Hola,
Como
Estas?
""" #Cadena de varias lineas
print(cadena)

print("""Hola
Mundo
Bello
""")


cadena1 = "Hola"
cadena2 = " Mundo"

print(cadena1 + cadena2) #Unir cadenas

#Se puede usar la busqueda por indices
#Las cadenas de caracteres son inmutables

cadena = "Gabriel"

cadena = "g" + cadena[1:] #Modificar una cadena indirectamente
print(cadena)