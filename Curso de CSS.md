# CSS

Para empezar se debe colocar en el *head*, del *html*, la etiqueta **link** con los atributos **rel**, **type** y **href**.    
  - En el **rel** colocas el valor **stlysheet**, significa "hoja de estilo".
  - En el **type**(significa "tipear") colocas el valor **text/css**.
  - En el **href** colocas la ruta hacia el archivo css. 
>Tienes que crear un archivo ".css" en la carpeta de la pagina.


## ESTRUCTURA

La estructura de CSS es:

```css
selector{
    propiedad: valor;
}
```
El *selector* son los elementos, o el elemento, a la cual queremos cambiarle las propiedades.

La *propiedad* es lo que le queres cambiar.

## TIPOS DE SELECTORES

- **Universal**: Selecciona todos los elementos. 

```css
*{
    Propiedad: valor;
}
```
>Asi se usa


- **De tipo**: Seleccionas una etiqueta y edita todas las etiquetas iguales.

```css
h2{
    Propiedad: valor;
}
```
>Aqui se editarian todas las etiquetas **h2**


- **Clases**: Agregas etiquetas a una *clase* y al editarla, solo se editan las etiquetas dentro de ella. 
Para hacerlo les agregas el atributo **class** y el valor que le tenes que dar sera el nombre de la *clase*. 
Para editarla tenes que poner un "." y el nombre de la *clase*.

```html
<h2 class="etiquetah2">

</h2>
```
>Aqui le di la *clase* y le puse el nombre.

```css
.etiquetah2{
    Propiedad: valor;
}
```
>Aqui estoy editandola.


- **Id**: Seleccionas a una unica etiqueta.
Se utiliza poniendole a una etiqueta el atributo **id** y como valor ponerle una palabra, o varias, para identificarla.
>Separar las palabras con una "-".

En css se edita poniendo "#" y la palabra que contenga el **id** que queres editar.
>No puede haber mas de un id con las mismas palabras.


- **Por atributo**: Le creas un atributo, con un valor, a una etiqueta.
Para editar esa etiqueta en css copias el atributo, con su valor, y lo agregas entre corchetes.

```html
<h2 arroz"con-leche"></h2>
```
>Aqui le agregue un atributo que me invente.

```css
[arroz"con-leche"]{
    Propiedad: valor;
}
```
>Aqui estoy editando esa etiqueta mediante el atributo que le di.


- **Descendiente**: Sirve para seleccionar un elemento que este dentro de otro elemento.

```css
h2 p{
    Propiedad: valor;
}
```
>Asi estaria editando los **p** que esten dentro de un **h2**.

```css
.h2-class b{
    Propiedad: valor;
}
```
>Asi estaria editando los **b** que estan dentro de un **h2** con la clase **h2-class**.


- **Pseudo-clases**: Sirve para agregarle un evento a una etiqueta cuando haces algo en concreto. Por ejemplo, que cuando coloques el mouse encima cambie de color.

## ESPECIFICIDAD

| Nivel de importancia de los selectores |
| -------------------------------------- |
| !importan                              |
| Estilos en linea                       |
| Identificadores                        |
| Clases; Pseudo-clases; Atributos       |
| Elementos; Pseudo-elementos            |

>El que este mas arriba es mas importante. Si usas 2 selectores de diferente importancia para editar una misma etiqueta, tomara el que tenga mayor importancia. Si usas 2 selectores que tienen la misma importancia, tomara el que este escrito por debajo.

## METODOLOGIA GEM

Este metodo sirve para que no hayan tantos problemas al utilizar tantos selectores.

```html
<div class"contenedor-div">
    <p class"contenedor-div__p">
        <h2 class"contenedor-div__p-h2"></h2>
        <h2 class"contenedor-div__p-h2"></h2>
        <h2 class"contenedor-div__p-h2--active"></h2>
        <h2 class"contenedor-div__p-h2"></h2>
        <h2 class"contenedor-div__p-h2"></h2>
    </p>
</div>
```
>Al contenedor le agregas una clase intuitiva. Al que este por debajo le agregas la misma clase pero añadiendole dos "__" y la etiqueta que es. Si hay mas etiquetas dentro, le agregas lo anterior mas un "-" y la respectiva etiqueta. Los guiones bajos solo se usan una vez dentro del contenedor.

>Si queres que una etiqueta sea diferente, le agregas dos "--" y una palabra intuitiva. Podras editar esa etiqueta aparte.

## UNIDADES DE MEDIDA

En CSS hay dos unidades de medida:

- **Relativas**: Son variables. Dependen de la caja contenedora.
>Sirve para que tu pagina web se adapte a moviles y tablets.

>La unidad de medida es "em". La equivalencia normal es 1em son 16px.

>Para cambiar la equivalencia, agregale la medida que quieras a la caja contenedora, y todo lo que este dentro tendra como equivalencia esa medida.


- **Fijas**: Son fijas, como los milimetros(mm), pixeles(px), punto(pt), centrimetros(cm).

La propiedad para editar el tamaño de la letra es **font-side**.

## PROPIEDADES DE TEXTO

- **font-size**: Para ajustar el tamaño de la letra.
- **font-family**: Para la tipografia.
- **line-height**: Para el espacio que ocupara.
- **font-weight**: Para el grosor de la letra.

## TIPOGRAFIAS EXTERNAS

Para usar tipografias externas tenes que ir a la siguiente pagina "https://fonts.google.com".

Despues tenes que:
1. Elegir la tipografia que te guste y darle click.
2. Bajar hasta donde dice "styles"
3. Elegir el estilo que te guste.
4. Darle al mas que hay a la derecha para seleccionarla.
5. Ir arriba a la derecha donde pone "View selected families" y ahi te pondra los codigos que tenes que poner en html y css.

## NORMALIZE

Los navegadores traen estilos predeteminados y eso causa problemas a la hora de editar los estilos de nuestra pagina. Para solucionar ese problema se usa *normalize* que reinicia los estilos del navegador.

Para usarlo simplemente se debe ir al navegador y buscar "normalize", una vez en la pagina dale a descargar y te saldra todo el codigo, dale click derecho y a "guardar como" y ubicalo en la carpeta de tu pagina.

Una vez lo tengas tenes que editarlo, busca dentro del archivo el selector **img** y agregale esta propiedad y valor "max-width: 100%". Despues anda arriba del todo y usa el selector universal y agregale las propiedades "box-sizing:border-box;" "padding: 0;" "margin: 0;". 
>Si no queres tener que editarlo nomas copialo de este repositorio y pegalo en un archivo ".css".

## CAJAS

Hay etiquetas que son en linea, ocupan todo el ancho del contenedor, y otras que son en bloque, ocupan solo el ancho de la letra. Para invertirlo usas la propiedad **display** con los valores **block** o **inline**.

## PADDING

Esta propiedad es para cambiar el espacio que hay entre el texto y la caja. 

Se usa la propiedad **padding**.
- **padding-top**: Modifica el espacio superior.
- **padding-right**: Modifica el espacio derecho.
- **padding-bottom**: Modifica el espacio inferior.
- **padding-left**: Modifica el espacio izquierdo.

Esto se puede abrebiar usando el **padding** y luegos los valores.

```css
h2 {
    padding: 10px;
}
```
>Aqui le estas dando 20px a los cuatro lados.

```css
h2 {
    padding: 10px 20px;
}
```
>Aqui le estas dando 10px al eje Y y 20px al eje X.

```css
h2 {
    padding: 10px 20px 30px;
}
```
>Aqui le estas dando 10 px al top, 20px al eje X y 30px al bottom.

```css
h2 {
    padding: 10px 20px 30px 40px;
}
```
>Aqui le estas dando 10px en top, 20px en right, 30px en bottom y 40px en left.

## HEIGHT Y WIDHT

- **height**: Es el alto de la caja.
- **Widht**: Es el ancho de la caja.

## BOX-SIZING

Con esta propiedad puedes hacer 2 cosas:
- Con el valor **content-box** los valores del **padding** estaran por fuera de los del **height** y el **widht**.
- Con el valor **border-box** el **padding** no pasara los valores del **height** y el **width**.
>Con la propiedad **text-aling** y el valor **center** centra el texto horizontalmente.

## MARGIN

Esta propiedad separa la caja de las demas cosas por los cuatro lados. Funciona igual que el **padding**.
>Con el valor **auto** Centra la caja horizontalmente al medio de la pagina.

## BORDES

La propiedad **border-radius** sirve para redonder el borde, se puede usar px, em, % y demas.

La propiedad **border** es para colocarle un borde a la caja. Sus valores son 3:
1. Primero se coloca lo que medira la caja.
2. Segundo se coloca el estilo de borde.

Estan estos estilos de borde.
- **solid**
- **dashed**
- **double**
- **goove**
- **ridge**
- **inset**
- **outset**
3. Tercero se coloca el color que tendra le borde.

## BOX MODEL

Aquí explicare la jerarquia en la que se van poniendo las cosas.

Primero está el **content**, que es el contenido de la caja. Después, fuera del **content** esta el **padding**, que es el espacio entre el **content** y la caja. Fuera del **padding** está el **border**, que son los bordes de la caja. Y por ultimo esta el **margin**, que es el margen que tiene la caja con el resto de cosas.

## SOMBRAS

Aqui se usa la propiedad **box-sadow** para poder darles sombra a la caja. Esta propiedad esta conformada por 5 valores.

```css
H2 {
    box-shadow: 2px 4px 10px 0px red;
}
```
>El primer valor es lo que se movera en el eje Y. El segundo valor es lo que se movera en el eje X. El tercer valor es cuan desenfocada estara. El cuarto valor es cuanto borde va a tener. Y el quinto valor es el color que tendra. ME REFIERO A LA SOMBRA.

Tambien esta la propiedad **text-shadow** para darle sombra al texto. 
>Es lo mismo que el **box-shadow** pero sin el cuarto valor.

Se puede intensificar el efecto copiando y pegando otra vez los valores, separandolos con punto y coma.

## OUTLINE  

Es una propiedad que agrega un borde que no ocupa espacio. Como un resaltador. Funciona igual que el **border**.

## POSITION

>Antes de leer todo lo que sigue tenes que saber que cada elemento en html tiene un lugar reservado.

Esta propiedad posiciona un elemento, al hacerlo adquiere nuevas propiedades.
- **top**: Desplaza el elemento hacia abajo. Se usan unidades de medida. Se pueden usar medidas negativas.
- **left**: Desplaza el elemento hacia la derecha. Se usan unidades de medida. Se pueden usar medidas negativas.
- **right**: Esta se vuelve inutil si esta left.
- **bottom**: Esta se vuelve inutil si esta top.
- **z-index**: Esta propiedad sirve para superponer elementos. Le das un valor numerico a un elemento y este se pondra por delante de los que tenga un valor numerico inferior.

Hay 5 valores con los que posicionar un elemento:
- **static**: Es el valor predeterminado.
- **relative**: Esta propiedad permite desplazar al elemento sin que este pierda su lugar reservado y el punto de referencia para el desplazamiento sera el lugar reservado.
- **absolute**: Esta propiedad permite hacer lo mismo que *relative* pero el elemento pierde su lugar reservado. Su punto de referencia es el contenedor o el viewport. La caja se ajusta al tamaño del contenido.
>Solo toma al contenedor como punto de referencia si este esta posicionado.
- **fixed**: Esta propiedad hace lo mismo que *absolute* pero con esta el elemento queda fijo.
- **sticky**: Esta propiedad hace lo mismo que *relative* y lo mismo que *fixed* pero solo se comporta como *fixed* cuando llegas al punto que le decis.

## DISPLAY

Esta propiedad afecta el comportamiento de la caja. Su valores son:
- **block**: La caja se comporta en bloque. 
- **inline**: La caja se comporta en linea. A los elementos en linea no se les puede cambiar el alto ni el ancho y se ajustan al contenido.
- **inline-block**: La caja se comporta como en linea pero si se le puede cambiar la altura y el ancho.
- **flex**
- **grid**
- **inline-flex**
- **inline-grid**
>Estos ultimos 4 los explico mas adelante.

## OVERFLOW

Con esta propiedad se define que se hara con lo que sobresalga de la caja, por defecto deja que se vea. Esta es una propiedad abreviada de **overflow-y** y **overflow-x**.

Sus valores son:
- **scroll**: Si usas la propiedad abreviada, pone obligatoriamente el *scroll* en los dos ejes. Si usas la propiedad con el eje Y, agrega el *scroll* solo en ese eje. Si usas la propiedad con el eje X, agrega el *scroll* en los 2 ejes.
- **auto**: Agrega un *scroll* en el eje que sea necesario.
- **hidden**: Oculta el contenido que sobre.

## FLOAT

El unico uso que se le puede dar ahora a esta propiedad es para colocar una imagen que sea envuelta por texto.

Esto se hace colocando una imagen y texto dentro de un contenedor, primero va la imagen y luego el texto.

Sus valores son:
- **left**: Coloca la imagen a la izquierda.
- **right**: Coloca la imagen a la derecha.

## PSEUDOELEMENTOS

Los pseudoelementos se agregan a un elemento.

Los pseudoelementos son:
- **first-line**: Para editar la primera linea de texto.
- **first-letter**: Para editar la primera letra del texto.
>Estas dos etiquetas no funcionan con elementos en linea.
- **spaceholder**: Agregas texto al imput el cual desaparece cuando escribis. Lo agregas como atributo y como valor, el texto.
- **selection**: Para editar la seleccion. Actua como elemento en linea.
- **before**: Para agregar algo antes del texto. No puede ser seleccionado.
- **after**: Para agregar algo despues del texto. No puede ser seleccionado.

```css
.texto::first-line {
    propiedad: valor;
}
```
>Asi se agregan los pseudoelementos.

## PSEUDOCLASES

Las pseudoclases son eventos que ocurren cuando haces algo en concreto.

Estas son las pseudoclases:
- **hover**: Le das efectos a un elemento cuando esta el mouse encima.
- **link**: Cambias el color a un link que nunca visito el usuario. Si el usuario ya lo visito, tendra el color original.
- **visited**: Cambias el color a un link que el usuario ya visito.
- **active**: Cambia el elemento cuando mantenes apretado encima.
- **focus**: Cambia cuando tenes seleccionado un input.

```css
.caja1:hover {
    propiedad: valor;
}
```
>Asi se agregan las pseudoclases.

## OBJET-FIT

Con esta propiedad modificas la resolucion de las imagenes.

Sus valores son:
- **contain**: La imagen se ajustara a su resolucion original sin importar que sobre espacio en el contenedor.
- **cover**: La resolucion de la imagen se adapta al contenedor y recorta lo que sobra.
- **none**: Pone la resolucion original de la imagen sin importar el tamaño del contenedor.
- **scale-down**: Elige entre *contain* y *none* y el que tenga menor resolucion, es el que pondra.

## OBJET-POSITION

Esta propiedad sirve para  la imagen dentro del contenedor.

Sus valores son 
- **top** 
- **right** 
- **bottom** 
- **left** 
- **unidades de medidad**

## CURSOR

En la siguiente pagina podes elegir cursores que podes poner en tu pagina durante ciertos momentos.

https://www.w3schools.com/cssref/tryit.asp?filename=trycss_cursor

## COLORIZACION

Aca se explica como se define un color con CSS.

Las formas de definir un color son:

- **Con el nombre del color en ingles**

```css
.caja {
    background: red;
}
```

- **Usando RGB**

```css
.caja {
    background: rgb(0,0,0)
}
```
>Dentro de los parentesis pones 3 numeros, separados por una coma, del 0 al 255. 
El primer numero, es cuanto rojo queres ponerle. 
El segundo numero, es cuanto verde queres ponerle. 
El tercer numero, es cuanto azul queres ponerle.

- **Usando RGBA**

```css
.caja {
    background: rgba(0,0,0,0)
}
```
>Este es casi lo mismo que RGB pero el cuarto numero es la *opacidad*, su valor es de 0 a 1.

- **Exadecimal**


## CONCEPTO DE FLEXBOX

* hola
  * hola

- hola
  - hola