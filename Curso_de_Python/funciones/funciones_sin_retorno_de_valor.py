'''
Sirven para resolver un problema especifico y reciclar codigo.
El nombre de la funcion debe ser lo que realizara.
'''

def saludar(): #El parentesis puede estar vacio o contener parametros.
    print("Hola amig@")

saludar() #Llamamos a la funcion. Puedes hacerlo cuantas veces quieras.

print()

def saludar(nombre): #Indicas los parametros que contendra.
    print(f"Hola {nombre}")

saludar("Sol") #Le das el valor que usara.
saludar("Carlos")

print()

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num}*{i} = {num*i}")

tabla_multiplicar(4)
print()
tabla_multiplicar(2)