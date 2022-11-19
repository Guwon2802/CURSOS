'''
Se le pide un dato al usuario y se lo guarda en una variable.
'''

#Con "input" se guarda un dato de tipo "str". Agregas un mensaje entre comillas. El programa no continua hasta que agregues algo. Guarda espacios.
nombre = input("Coloque aqui su nombre: ") 
print(f"Hola {nombre}")


#Permite guardar un dato tipo "int".
edad = int(input("Coloca tu edad: ")) 
print(f"Tiene {edad} años")


#Permite guardar un dato tipo "float"
numero = float(input("Coloca un numero: ")) 
print(numero)