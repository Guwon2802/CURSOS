'''
Cuando creas que el usuario pueda dañar tu programa, puedes lanzar tu propia excepcion.
'''


def verificandoEdad(edad):
    if edad<0: #La edad es negativa
        raise ValueError ("La edad no puede ser negativa") #Con "raise" lanzas tu propia excepcion, una ya definida. Al lado puedes ponerle texto.
    
    elif edad<18:
        print("Eres muy joven")
    
    elif edad<30:
        print("Eres joven")
    
    elif edad<50:
        print("Eres maduro")

edad = int(input("Digite su edad: "))
#Identificas donde esta la excepcion.
try:
    verificandoEdad(edad)
#Capturas tu propia excepcion.
except ValueError as EdadNegativa: #Le podes cambiar el nombre.
    print(EdadNegativa) #Imprimis y saldra tu mensaje.

print("Programa terminado")