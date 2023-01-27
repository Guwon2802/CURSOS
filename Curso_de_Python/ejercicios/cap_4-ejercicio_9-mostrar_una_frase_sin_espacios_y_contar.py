#Capitulo 4: Bucles

'''
EJERCICIO 9:
Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco y ademas un contador de
cuantos caracteres tiene la frase(sin contar los espacios en blanco)
Ejemplo:
        Frase: Hola que tal?
        Frase final: Holaquetal?
        N° de caracteres: 11
'''

#PROGRAMA

frase = input("Digite una frase: ")
frase2 = ""

for i in frase:
    if i!=" ":
        frase2 += i

frase = frase2

print(f"\nFrase final: {frase}")
print(f"N° de caracteres: {len(frase)}")