#creando una lista(se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",1.64,True]

#creando una tupla(no se pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",1.64,True)

#esto es valido
lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"

#creando un conjunto (set) (no se accede a elementos po indice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",1.64,True}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dic) (la estructura es key : value y separamos por comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy dalto"
}