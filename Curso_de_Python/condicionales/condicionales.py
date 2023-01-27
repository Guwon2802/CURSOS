'''
Aqui hago un programa que comprueba el numero que colocas y te dice si es positivo, negativo o es cero. 
'''

numero = int(input("Coloque aqui un numero: "))

#Comprueba de arriba a abajo si se cumple algun caso y te lo muestra.

#Significa "SI"
if numero>0: 
    print('"El numero es positivo"')

#Significa "Caso contrario"
elif numero==0: 
    print('"El numero es cero"')

#Significa "SINO"
else: 
    print('"El numero es negativo"')