## Create new article
- Duplicate `new-article-template.html` and give a short URL name.
- Add to the list in `index.html`


## Add an image

Upload an image to the `images/` folder in GitHub, then use this inside the article's `article-copy` section:

```html
<figure class="article-image">
  <img src="../images/your-photo.jpg" alt="Describe what is visible in the image">
  <figcaption>An optional, short caption.</figcaption>
</figure>
```

The `../` in the path matters: articles live inside `posts/`, while images live at the repository root. Keep image filenames short, lowercase, and use hyphens (for example, `first-workbench.jpg`).
