# HTML5

## ETIQUETAS PRINCIPALES

**Primero se pone la etiqueta *DOCTYPE html***

- **html**: Dentro va toda la pagina.
- **body**: Aqui va lo que se puede ver en la pagina.
- **head**: Aqui va lo que no se puede ver en la pagina.

## ETIQUETAS DE TITULOS

- **h1**: Para el titulo. Solo se pone una.
- **h2**: Para los subtitulos.
- **h3**,**h4**,**h5** y **h6**: Para subtitulos dentro de un h2.  

## ETIQUETA DE TEXTO

- **p**: Para escribir parrafos.
- **b**: Letras en negritas.
- **i**: Inclinar las letras.
- **strike**: Tachar las letras. 
- **small**: Letras chiquitas.
- **br**: Punto aparte.

## ETIQUETA DE ENLACE

- Etiqueta **a**: Para redirigir a otra pagina. Se le coloca el *atributo* **href** y dentro a donde va a redirigir el enlace. Y con el atributo **target** y el *valor* **_blank** abre la pagina en otra pestaña, por defecto la abre en la misma.

Hay 2 tipos de rutas:
  - Rutas locales: Las que estan en nuestra carpeta.
  - Rutas externas: Paginas de internet.

Si la pagina no es tuya, la agregas con el https://.

Para abrir una pagina tuya que esta dentro de la misma carpeta, pones el nombre del archivo.

```html
<a href="imagen1.jpg">enlace a la imagen 1</a>
```

Si el archivo esta una carpeta adelante, le agregas **/** y el nombre del archivo.

```html
<a href="/imagen2.jpg">enlace a la imagen 2</a>
```

Si el archivo esta una carpeta detras, le agregas **../** y el nombre del archivo.

```html
<a href="../imagen3.jpg">enlace a la imagen 3</a>
```

## LISTAS

2 tipos de listas

- Etiqueta **ul**: listas desordenadas.

    - asi
    - se
    - ve

- Etiqueta **ol**: Listas ordenadas.

    1. asi
    2. se
    3. ve

>Dentro va la etiqueta **li** y ahi se escribe.

## MULTIMEDIA

- Etiqueta **img**: Para colocar una imagen. Con el *atributo* **src**, hace lo mismo que el *atributo* **href**.

>Hay dos formas de poder poner la imagen:
>- Usando la de otra pagina.  
>- Descargandola y guardandola en la carpeta de tu pagina.

- Etiqueta **video**: Para agregar un video. Con el *atributo* **src** y el *atributo* **controls** para que el navegador te lo reproduzca.

- Etiqueta **audio**: para agregar un audio. Con el *atributo* **src** y el *atributo* **controls**.

## DIVS

- Etiqueta **div**: Separa y agrupa.

## FORMULARIOS

- Etiqueta **form**: Para crear formularios. Dentro se usa la etiqueta **input**, es donde el usuario debe colocar informacion.

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

## METADATOS

Los metadatos son información que describe otra información. Esto va dentro del “head”.

Aqui se utiliza la etiqueta **meta** con los *atributos*:

- **charset**: Para poner un conjunto de caracteres. Con el *valor* **utf-8** te reconoce las tildes.
- **name**: Aqui va el tipo de metadato que queres usar.

Tipos de metadatos:

- **keywords**: Para poner palabras claves y asi, si la gente las usa, pueda aparecer tu pagina.
- **description**: Para colocar una descripcion de la pagina.
- **author**: Para indicar quien es el autor de la pagina.
- **copyright**: Por si la pagina es para una empresa que tiene derechos de autor. Dentro de **content** va el nombre de la empresa.

>Los datos que quieras agregar van dentro del *atributo* **content**, el cual va despues del **name**.

## HTML SEMANTICO

Primero se coloca el encabezado (*header*) y por ultimo el pie de pagina (*footer*).

## NAV

Con la etiqueta **nav** colocas la barra de navegacion. Normalmente se coloca dentro del *header*.

En la barra de navegacion van los accesos a la cuenta y demas. Estos se colocan con las listas.

>Al crear esos accesos tenes que crear otros archivos de html con los respectivos nombres de los accesos. En todos el **nav** tiene que ser igual.

## SECCION Y ARTICULO

- Etiqueta **article**: para mostar un articulo. Dentro se coloca la etiqueta **section** para hacer una seccion.

## ASIDE

Va al costado del articulo, es una parte secundaria.
Se utiliza la etiqueta **aside**.

## FOOTER

Esto es el pie de pagina y va al final de la pagina. Se utiliza la etiqueta **footer**.
Es para poner si la pagina tiene copy o no, otros enlaces para contactarnos o redes sociales.
Aquí se utiliza la etiqueta **h4**.

## TABLAS

- Etiqueta **table**: Para hacer columnas con filas.
- Con la etiqueta **tr** haces las filas
- Con la etiqueta **td** haces las columnas.

## ALT y TITLE

- *Atributo* **alt**: Para ponerle un nombre de referencia a una imagen cuando no aparece en la pagina.
- *Atributo* **title**: Para ponerle un titulo a una imagen. Aparece cuando pones el cursor encima.

## ID

Sirve para enlazar un link con alguna etiqueta de la pagina.

Usas la etiqueta **a** con el *atributo* **href** y en el *valor* pones un **#** con una palabra clave.
Despues en la etiqueta pones el *atributo* **id** y en el *valor* pones la palabra clave.

```html
<a herf=#pagina2>ir a la pagina 2</a>
```
>Aqui es donde le das click y te manda al otro punto

```html
<a id="pagina2">pagina 2</a>
```
>Aqui es donde te manda el link