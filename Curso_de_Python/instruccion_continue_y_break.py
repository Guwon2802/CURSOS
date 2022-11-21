'''
Se puede usar en cualquier tipo de bucle.
'''

print()

for i in range(10):
    if i==5:
        #Cuando se cumpla la condicion, ignora lo que esta debajo y continua con el bucle.
        continue 
    print(i)

print()

for i in range(10):
    if i==5:
        #Si la condicion se cumple, rompe el bucle.
        break 
    print(i)

print()

print("Programa Finalizado")

print()