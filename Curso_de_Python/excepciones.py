'''
Errores causados por el usuario.
Aca se ve como poder lidiar con esos errores.
'''

#El error estaria en que el usuario digite un valor de un tipo diferente al que pedimos.

try: #Significa "intentar"
    numero = int(input("Digite un numero: "))
    print(f"La suma es: {numero+10}")
#Si ocurre un error, lo captura el "except", y el programa continua.
except:
    print("Ha ocurrido un error")

print("Programa terminado")

print()
##############################################################################################


while True: #El programa no finalizaria hasta que el usuario digite un valor "int"
    try:
        numero = int(input("Digite un numero: "))
        print(f"La suma es: {numero+10}")
        break #Si el usuario digita un valor "int", rompe. Sino, continuara.
    except:
        print("Ha ocurrido un error")

print("Programa terminado")

print()
##############################################################################################


while True:
    try:
        numero = int(input("Digite un numero: "))
        print(f"La suma es: {numero+10}")
        
    except:
        print("Ha ocurrido un error")

    else: #El "caso contrario" del except. Si el "except" se ejecuta, el "else" no y viceversa.
        print("Programa finalizado correctamente")
        break

print("Programa terminado")

print()
##############################################################################################


while True:
    try:
        numero = int(input("Digite un numero: "))
        print(f"La suma es: {numero+10}")
        
    except:
        print("Ha ocurrido un error")

    else: #El "caso contrario" del except. Si el "except" se ejecuta, el "else" no y viceversa.
        print("Programa finalizado correctamente")
        break

    finally: #Se ejecutara siempre.
        print("Iteracion finalizada")
print("Programa terminado")