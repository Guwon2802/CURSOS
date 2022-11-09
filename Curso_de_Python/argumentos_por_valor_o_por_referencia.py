#Argumentos por valor
'''
Las funciones toman una copia de las variables que no sean una coleccion.
Fuera de la funcion, la variable sigue conservando su valor.
'''
def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 5
doblar_valor(n)

print(n)


print()


#Para que la variable se pase por referencia
def doblar_valor(numero):
    return numero*2

n = 5
n = doblar_valor(n)

print(n)


print()


#Argumentos por referencia
'''
Los cambios que se hagan en la funcion, afectan las colecciones.
'''
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n)

print(n)


print()


#Para que la coleccion se pase por valor
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n[:]) #Le pones dos puntos, entre cochetes.

print(n)