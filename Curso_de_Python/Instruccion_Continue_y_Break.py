'''
Se puede usar en cualquier tipo de bucle.
'''

for i in range(10):
    if i==5:
        continue #Cuando se cumpla la condicion, ignora lo que esta debajo y continua con el bucle.
    print(i)


for i in range(10):
    if i==5:
        break #Si la condicion se cumple, rompe el bucle.
    print(i)

print("Programa Finalizado")