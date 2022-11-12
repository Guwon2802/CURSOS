#Capitulo 6: Funciones

'''
Ejercicio 5:
Desarrollar un programa que permita sumar los digitos de un numero con ayuda de una funcion recursiva.
Ejemplo:

Entrada = 123
Salida = 6
'''

def sumarDigitos(num):
    if num==0: #Caso base
        resultado = 0
    else: #Caso recursivo
        resultado = sumarDigitos(int(num/10)) + (num%10)

    return resultado

valor = sumarDigitos(165)
print(valor)