## ETIQUETA DE ENLACE

- Etiqueta **a**: Para redirigir a otra pagina. 
  - Se le coloca el *atributo* **href** y dentro a donde va a redirigir el enlace. 
  - Con el atributo **target** y el *valor* **_blank** abre la pagina en otra pestaña, por defecto la abre en la misma.

Hay 2 tipos de rutas:
  - Rutas locales: Las que estan en nuestra carpeta.
  - Rutas externas: Paginas de internet.
>Si la pagina no es tuya, la agregas con "https://".

Para abrir una pagina tuya que esta dentro de la misma carpeta, pones el nombre del archivo.

```html
<a href="imagen1.jpg">enlace a la imagen 1</a>
```

Si el archivo esta una carpeta adelante, le agregas "/" y el nombre del archivo.

```html
<a href="/imagen2.jpg">enlace a la imagen 2</a>
```

Si el archivo esta una carpeta detras, le agregas "../" y el nombre del archivo.

```html
<a href="../imagen3.jpg">enlace a la imagen 3</a>
```