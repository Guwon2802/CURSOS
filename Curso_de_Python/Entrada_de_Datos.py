#Sirve para pedirle un dato al usuario y que se guarde en una variable.

nombre = input("Coloque aqui su nombre: ") # Con "input" se guarda un dato de tipo "str".
#Si quieres agregar un mensajito, lo haces entre comillas.
#El programa no continuara hasta que le coloques algo.
#Tambien guarda espacios, como para agregar tu nombre completo. 

print(f"Hola {nombre}") #Asi le estas agregando texto.



edad = int(input("Coloca tu edad: ")) #Asi permite guardar un dato tipo "int".

print(f"Tiene {edad} años")



numero = float(input("Coloca un numero:")) #Asi permite guardar un dato tipo "float"

print(numero)