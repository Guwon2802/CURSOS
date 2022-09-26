## PSEUDO-ELEMENTOS

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