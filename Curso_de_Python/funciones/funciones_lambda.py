'''
Son funciones anonimas, sin nombre
Son para acciones sencillas
Retorna automaticamente
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

#creando una funcion lamba para multiplicar por dos
multiplicar_por_dos = lambda numero: numero*2

#creando funcion comun que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
#usando filter con una funcion comun
numero_pares = filter(es_par,numeros)
#"filter" agrega a la lista los valores que retornan "True", sino los descarta

#creando lo mismo que antes pero con lambda
numero_pares = filter(lambda numero:numero%2==0,numeros)

print(list(numero_pares))