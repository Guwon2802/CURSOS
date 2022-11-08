'''
CONDICIONALES
Aqui hago un programa que comprueba el numero que colocas y te dice si es positivo, negativo o es cero. 
'''

numero = int(input("Coloque aqui un numero: "))

if numero>0: #Significa "SI"
    print('"El numero es positivo"')
elif numero==0: #Significa "Caso contrario"
    print('"El numero es cero"')
else: #Significa "SINO"
    print('"El numero es negativo"')

#Comprueba de arriba a abajo si se cumple algun caso y te lo muestra.