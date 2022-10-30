#Capitulo 4: Bucles

'''
EJERCICIO 11:
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono,
el programa tendra el siguiente menu de opciones:
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir
'''

#PROGRAMA 1

agenda = {}

while True:
    print("\t.:MENU DE AGENDA:.") 
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Eliga una opcion del menu: "))

    print()

    if opcion == 1:
        nombre = input("Nombre del contacto -> ").lower() #Pedimos el nombre y lo pasamos a minuscula
        numero = input("Numero del contacto -> ") #Pedimos el numero
        
        if nombre not in agenda:
            agenda[nombre] = numero #Agregamos el nombre y el numero como contacto a la agenda
            print(f"\nSe agrego el contacto de {nombre} a su agenda")
        else:
            print("Ese nombre de contacto ya existe")
    
    elif opcion == 2:
        eliminar = input("Nombre del contacto que quiere eliminar -> ").lower() #Pedimos el nombre del contacto que quiere eliminar
        
        if eliminar in agenda: #Si el contacto esta en la agenda
            del(agenda[eliminar]) #Elimina el contacto
            print(f"\nSe elimino el contacto de {eliminar} de su agenda")
        else: #Si el contacto no esta
            print(f"El contacto {eliminar} no esta en su agenda")
    
    elif opcion == 3:
        print(f"Contactos de su agenda:")
        for clave,valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")

    elif opcion == 4:
        print("Gracias por usar su agenda de contactos")
        break
    
    else:
        print("Error, se equivoco de opcion de menu")

    print()