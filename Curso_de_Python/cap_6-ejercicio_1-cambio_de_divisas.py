#Capitulo 6: Funciones

'''
Ejercicio 1:
Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda (de tu moneda - hacia dolar y viceversa).
'''

#Funcion que cambia pesos a dolares.
def cambio_Pesos_Dolares(pesos): 
    return pesos/166.84

#Funcion que cambiar dolares a pesos.
def cambio_Dolares_Pesos(dolares): 
    return dolares*166.84

while True:
    print("""\t.:MENU:.
1. Covertir Pesos a Dolares
2. Convertir Dolares a Pesos
3. Salir""")
    opcion = int(input("Digite una opcion: "))

    print()
    
    if opcion == 1:
        pesos = float(input("Digite la cantidad de Pesos: "))
        print(f"Dolares -> ${cambio_Pesos_Dolares(pesos):.2f}")
    
    elif opcion == 2:
        dolares = float(input("Digite la cantidad de dolares: "))
        print(f"Pesos -> ${cambio_Dolares_Pesos(dolares):.2f}")

    elif opcion == 3:
        break

    else:
        print("Se equivoco de opcion de menu")

    print()