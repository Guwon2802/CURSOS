#Capitulo 2: Condicionales

'''
EJERCICIO 2:
Hacer un programa que pida 3 numeros y determine cual es el mayor
'''

#PROGRAMA

num1 = int(input("Coloque el primer numero: "))
num2 = int(input("Coloque el segundo numero: "))
num3 = int(input("Coloque el tercer numero: "))

if num1>=num2 and num1>=num3:
    print(f"El numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"El numero mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es {num3}")