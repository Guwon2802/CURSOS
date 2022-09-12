## FORMULARIOS

- Etiqueta **form**: Para crear formularios. 
  - Dentro se usa la etiqueta **input**, es donde el usuario debe colocar informacion.

Dentro del **input** se pueden usar los *atributos*:
  
  - **text**: Solo puede escribir texto.
  - **password**: Solo puede escribir contraseña.
  - **number**: Solo puede escribir numeros.
  - **email**: Solo puede escribir emails.
  - **color**: Deja seleccionar un color.
  - **range**: Deja elegir un numero del 0 a X. Agrega el *atributo* **min** para poner un minumo y **max** para un maximo.
  - **date**: Para poner una fecha.
  - **time**: Para poner un horario.
  - **button**: Es un boton. Agregale el *atributo* **Value** para escribir algo.
  - **submit**: Un boton para enviar el formulario.
  - **textarea**: Puede escribir y cambiar el tamaño. Con el *atributo* **readonly** solo puede leer el contenido.

> Con el *atributo* **required** el usuario tiene que llenar obligatoriamente dicho **input**.

Cuando se trabaja con la etiqueta **form** se usa el *atributo* **method**. Dentro se puede usar un metodo de encriptado(enc) o **post** para enviar el formulario al servidor.