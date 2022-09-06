# CSS

Para empezar se debe colocar en el *head*, del *html*, la etiqueta **link** con los atributos **rel**, **type** y **href**.

En el **rel** colocas el valor **stlysheet**, significa "hoja de estilo".

En el **type**(significa "tipear") colocas el valor **text/css**.

En el **href** colocas la ruta hacia el archivo css. 
>Tienes que crear un archivo ".css" en la carpeta de la pagina.

## ESTRUCTURA

La estructura de CSS es:

```css
selector{
    propiedad: valor;
}
```
El *selector* son las etiquetas, o la etiqueta, a la cual queremos cambiarle las propiedades.

La *propiedad* es lo que le queres cambiar.

## TIPOS DE SELECTORES

- **Universal**: Selecciona todas las etiquetas. 

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
| ----- |
| !importan |
| Estilos en linea |
| Identificadores |
| Clases; Pseudo-clases; Atributos |
| Elementos; Pseudo-elementos |

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

>la unidad de medida es "em". La equivalencia normal es 1em son 16px.
- **Fijas**: Son fijas, como los milimetros(mm), pixeles(px), punto(pt), centrimetros(cm).

La propiedad para editar el tamaño de la letra es **font-side**.