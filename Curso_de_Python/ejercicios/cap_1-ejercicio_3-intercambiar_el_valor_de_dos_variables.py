#Capitulo 1: Elementos Basicos

'''
EJERCICIO 3:
Hacer un programa para intercambiar el valor de 2 variables
Por ejemplo:
    a = 10      a = 5
            ->
    b = 5       b = 10
'''

#PROGRAMA

a = (input("a -> "))
b = (input("b -> "))

a , b = b , a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")