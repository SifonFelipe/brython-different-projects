## Crear un artículo nuevo

- Duplicá `new-article-template.html` y asignale un nombre corto para la URL.
- Agregalo a la lista de `index.html`.


## Agregar una imagen

Subí una imagen a la carpeta `images/` en GitHub y luego usá esto dentro de la sección `article-copy` del artículo:

```html
<figure class="article-image">
  <img src="../images/tu-foto.jpg" alt="Describí lo que se ve en la imagen">
  <figcaption>Un epígrafe breve y opcional.</figcaption>
</figure>
```

El `../` de la ruta es importante: los artículos viven dentro de `posts/`, mientras que las imágenes están en la raíz del repositorio. Mantené los nombres de archivo de las imágenes cortos, en minúsculas y con guiones (por ejemplo, `primer-banco-de-trabajo.jpg`).
