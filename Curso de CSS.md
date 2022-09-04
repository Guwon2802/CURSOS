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

- **De tipo**: Seleccionas una etiqueta y edita todas las etiquetas iguales.

```css
h2{
    Propiedad: valor;
}
```

- **Clases**: Agregas elementos a una *clase* y al editar la *clase*, solo se editan los elementos dentro de ella. 
Para hacerlo les agregas el atributo **class** y el valor que le tenes que dar sera el nombre de la *clase*. 
Para editar la clase tenes que poner un **.** y el nombre de la *clase*.
- **Id**: Seleccionas a una etiqueta y la volves unica.