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

Dentro va la etiqueta **li** y ahi se escribe.

## MULTIMEDIA

- Etiqueta **img**: Para colocar una imagen. Con el *atributo* **src**, hace lo mismo que el *atributo* **href**.

Hay dos formas de poder poner la imagen:
  - Usando la de otra pagina.
  - Descargandola y guardandola en la carpeta de tu pagina.

- Etiqueta **video**: Para agregar un video. Con el *atributo* **src** y el *atributo* **controls** para que el navegador te lo reproduzca.

- Etiqueta **audio**: para agregar un audio. Con el *atributo* **src** y el *atributo* **controls**.

## DIVS

- Etiqueta **div**: Separa y agrupa.

## FORMULARIOS

- Etiqueta **form**: Para crear formularios.
