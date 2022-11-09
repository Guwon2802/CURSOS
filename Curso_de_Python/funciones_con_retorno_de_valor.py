def multiplicar(num1,num2):
    mult = num1*num2
    return mult #Te retorna el resultado de la variable.

#Puedes guardar la funcion en una variable e imprimir la variable.
mult = multiplicar(5,4) 
print(mult) 

print()

#O puedes imprimir la funcion directamente.
print(multiplicar(3,4))
print(multiplicar(7,2))
print(multiplicar(8,9))

print()

def prueba():
    return "hola",45,[1,2,3] #Puede retornarte varios valores.

print(prueba()) #Te imprime los valores dentro de una tupla

print()

#Cadena,Numero,Lista.
c,n,l = prueba() #Puedes guardarlos en variables.
print(c)
print(n)
print(l)