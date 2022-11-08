'''
Se puede simular colas en python.
Funciona como una cola para entrar al colectivo.
'''

cola = ["Jose","Federico","Gabriel","Maria"]

#Agregamos elementos al final de la cola

cola.append("karla")
cola.append("Flor")

print(cola)

#Sacando elementos por el principio de la cola

e = cola.pop(0)
print(f"Entro {e}")
e = cola.pop(0)
print(f"Entro {e}")
e = cola.pop(0)
print(f"Entro {e}")

print(f"Quedaron: {cola}")