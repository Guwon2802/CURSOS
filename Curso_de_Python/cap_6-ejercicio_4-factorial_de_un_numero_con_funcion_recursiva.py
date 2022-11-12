#Capitulo 6: Funciones

'''
Ejercicio 4:
Desarrollar un programa para calcular el factorial de un numero con ayuda de una funcion recursiva.

Recuerda:
    5! = 5*4*3*2*1 => 120
'''

def factorial(num):
    if num>0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1
    return resultado

valor = factorial(5)
print(valor)