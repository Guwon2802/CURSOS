## DISPLAY-FLEX

*display flex* se aplica al contenedor y afecta a los elementos dentro de este. El contenedor se volvera un *flex-container* y los elementos dentro se vuelven *flex-items*.

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

>Estos *flex-items* se pondran uno al lado del otro horizontalmente. Los *flex-items* se ajustaran para que siempre tengan el mismo alto.