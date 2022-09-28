# CONDICIONALES COMBINADOS

edad = int(input("Coloque su edad: "))

if edad>0 and edad<100: # Esto es un condicional combinado
    print("Edad correcta")
    if edad>=18: # Esto es un condicional anidado.
        print("Es mayor de edad")
else:
    print("Edad incorrecta")



edad = int(input("Coloque su edad: "))

if 0<edad>100: # Esto es un condicional relacional combinado.
    print("Edad correcta")
    if edad>=18: 
        print("Es mayor de edad")
else:
    print("Edad incorrecta")