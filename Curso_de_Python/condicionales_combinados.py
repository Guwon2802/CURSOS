'''
CONDICIONALES COMBINADOS
'''

edad = int(input("Coloque su edad: "))

#Esto es un condicional combinado
if edad>0 and edad<100: 
    print("Edad correcta")

    #Esto es un condicional anidado.
    if edad>=18: 
        print("Es mayor de edad")

else:
    print("Edad incorrecta")


print()


edad = int(input("Coloque su edad: "))

#Esto es un condicional relacional combinado.
if 0<edad>100: 
    print("Edad correcta")
    if edad>=18: 
        print("Es mayor de edad")

else:
    print("Edad incorrecta")