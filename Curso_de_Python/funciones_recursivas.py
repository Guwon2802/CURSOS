'''
Son funciones que se llaman a si mismas.
Se comporta como un ciclo.
'''
def cuenta_regresiva(num):
    if num>0: #Si "num" es mayor a 0.
        print(num) #Lo imprime.
        cuenta_regresiva(num - 1) #Vuelves a llamar a la funcion y le restas 1. 
    else: #El tope para que no se vuelva infinito.
        print("BOOOOOOM!!!!")

cuenta_regresiva(5)