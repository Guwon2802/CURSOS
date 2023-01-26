#Capitulo 2: Condicionales

'''
EJERCICIO 1:
Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son
'''

#PROGRAMA

num1 = int(input("Coloque el primer numero: "))
num2 = int(input("Coloque el segundo numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos numeros son impares")