"""estructura:
    if condicion:
        accion
"""
#if True:
    #accion se ejecuta
    
#if False:
    #accion no se ejecuta
    
contraseña_almacenada = "DaltoMaestro"
contraseña_escrita = "DaltoMaestro"

#si
if contraseña_escrita == contraseña_almacenada:
    print("INICIANDO SESION...")
#caso contrario
else:
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")