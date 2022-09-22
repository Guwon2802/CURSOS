## DISPLAY-FLEX

*display flex* se le agrega al contenedor y se aplicara a los elementos dentro de este. El contenedor se volvera un *flex-container* y los elementos dentro se vuelven *flex-items*.

```css
.flex-container {
    display: flex;
}
```

```html
<div class="flex-container">
    <h2 class="flex-item">

    </h2>
    <p class="flex-item">

    </p>
    <div class="flex-item">

    </div>
</div>
```

>Estos *flex-items* se pondra uno al lado del otro horizontalmente. El alto de los flex-items sera siempre el mismo sin importar nada.