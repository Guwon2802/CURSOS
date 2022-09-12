## NORMALIZE

Los navegadores traen estilos predeteminados y eso causa problemas a la hora de editar los estilos de nuestra pagina. Para solucionar ese problema se usa *normalize* que reinicia los estilos del navegador.

Para usarlo simplemente se debe ir al navegador y buscar "normalize", una vez en la pagina dale a descargar y te saldra todo el codigo, dale click derecho y a "guardar como" y ubicalo en la carpeta de tu pagina.

Una vez lo tengas tenes que editarlo, busca dentro del archivo el selector **img** y agregale esta propiedad y valor "max-width: 100%". Despues anda arriba del todo y usa el selector universal y agregale las propiedades "box-sizing:border-box;" "padding: 0;" "margin: 0;". 
>Si no queres tener que editarlo nomas copialo de este repositorio y pegalo en un archivo ".css".