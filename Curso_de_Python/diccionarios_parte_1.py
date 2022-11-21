'''
Tienen dos elementos por pisicion, la clave y el valor.
No pueden haber claves duplicadas.
Son desordenados.
Puedes colocarles dentro otras tipos de colecciones.
'''

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

#Agregar una clave, con su valor, al diccionario.
diccionario["amarillo"] = "yellow"

#Modificar un valor de una clave.
diccionario["azul"] = "BLUE" 

#Eliminar una clave, con su valor.
del(diccionario["rojo"]) 

#Imprimir todo el diccionario.
print(diccionario) 

#Imprimes el valor de una clave.
print(diccionario["azul"]) 

#Se pueden usar listas como valor.
diccionario = {"Gabriel":(18,1.64),"Jose":(17,1.70),"Maria":(20,1.67)} 
print(diccionario)

#Se pueden usar diccionarios, dentro de un diccionario.
diccionario = {"Gabriel":{"Edad":18,"Estatura":1.64},"Jose":{"Edad":17,"Estatura":1.70},"Maria":{"Edad":20,"Estatura":1.67}} 
print(diccionario["Gabriel"])