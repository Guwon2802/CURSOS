'''
Hay dos bloques de errores al programar:
El primero es causado por el programador.
El segundo es causado por el usuario.
Aqui se vera el primero.
'''

#Errores de sintaxis
print("Hola amiga" #Falta un parentesis


if 15>10 #Faltan los dos puntos
    print("Es mayor")


#Errores de nombre
prin("Hola amiga") #Le falta una letra


#Errores semanticos
lista = [1,2,3]

lista.pop()
lista.pop()
lista.pop()
lista.pop() #La lista ya no tiene elementos que eliminar.

print(lista)
print(lista(5)) #Se intenta acceder a una posicion en la lista que no existe.


numero = input("Digite un numero: ") #El numero se esta guardando como dato de tipo "str"
print(f"La suma es {numero+10}")