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