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

#PROGRAMA

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
        #Pedimos el nombre y lo pasamos a minuscula
        nombre = input("Nombre del contacto -> ").lower() 
        #Pedimos el numero
        numero = input("Numero del contacto -> ") 
        
        if nombre not in agenda:
            #Agregamos el nombre y el numero como contacto a la agenda
            agenda[nombre] = numero
            print(f"\nSe agrego el contacto de {nombre} a su agenda")
        else:
            print("Ese nombre de contacto ya existe")
    
    elif opcion == 2:
        #Pedimos el nombre del contacto que quiere eliminar
        eliminar = input("Nombre del contacto que quiere eliminar -> ").lower() 
        #Si el contacto esta en la agenda
        if eliminar in agenda:
            #Elimina el contacto
            del(agenda[eliminar]) 
            print(f"\nSe elimino el contacto de {eliminar} de su agenda")
        #Si el contacto no esta
        else:
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