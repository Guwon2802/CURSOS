## METODOLOGIA BEM

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