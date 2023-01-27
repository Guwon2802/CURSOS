#Capitulo 4: Bucles

'''
EJERCICIO 5:
Hacer un programa para calcular el factorial de un numero positivo
'''

#PROGRAMA

numero = int(input("Digite un numero: "))

while numero<0: #Mientras el numero sea negativo
    print("Error -> El numero debe ser positivo")
    numero = int(input("Digite un numero: "))

#Calcular el factorial
factorial = 1

for i in range(1,numero+1):
    factorial *= i

print(f"\nEl factorial del numero {numero} es {factorial}")