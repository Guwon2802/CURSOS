#Capitulo 2: Condicionales

'''
EJERCICIO 5:
Hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendra el siguiente menu de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

#PROGRAMA

saldo = 1000

print("/t.:MENU:.") #El "/t" da una tabulacion
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Eliga una opcion del meno: "))

print() #Esto dara un salto de linea entre el menu y lo demas

if opcion==1:
    extra = float(input("Cuanto dinero quiere ingresar -> "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}") 

elif opcion==2:
    retirar = float(input("Cuanto dinero quiere retirar -> "))
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==4:
    print("Gracias por utilizar su cajero automatico")
else:
    print("Error, se equivoco de opcion de menu")