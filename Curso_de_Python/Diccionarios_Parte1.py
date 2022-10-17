'''
Tienen dos elementos por pisicion, la clave y el valor.
No pueden haber claves duplicadas.
Son desordenados.
Puedes colocarles dentro otras tipos de colecciones.
'''

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"] = "yellow" #Agregas una clave, con su valor, al diccionario.
diccionario["azul"] = "BLUE" #Tambien se puede modificar.

del(diccionario["rojo"]) #Eliminar una clave, con su valor.

print(diccionario) #Imprimes todo el diccionario.

print(diccionario["azul"]) #Imprimes el valor de una clave.


diccionario = {"Gabriel":(18,1.64),"Jose":(17,1.70),"Maria":(20,1.67)} #Se pueden usar listas como valor.
print(diccionario)


diccionario = {"Gabriel":{"Edad":18,"Estatura":1.64},"Jose":{"Edad":17,"Estatura":1.70},"Maria":{"Edad":20,"Estatura":1.67}} #Se pueden usar diccionarios, dentro de un diccionario.
print(diccionario["Gabriel"])