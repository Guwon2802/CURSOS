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