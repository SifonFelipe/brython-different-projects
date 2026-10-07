# Sifon's blog

A small, static blog published with GitHub Pages at `www.sifonrojo.com`.

## Publish an article

There is no login built into this site: GitHub Pages only serves static files, so adding an editor with a secure login would require a separate service and setup.

The simple, secure phone-friendly workflow is GitHub itself:

1. Open this repository in the GitHub mobile app or at github.com.
2. In `posts/`, duplicate `new-article-template.html` and give it a short URL name, for example `my-first-note.html`.
3. Edit the title, date, read-time, and text. Commit the change to the publishing branch.
4. Add its title, description, date, and link to the top of the list in `index.html`.

GitHub Pages will publish the change automatically after the commit. The template is deliberately plain HTML so it can be edited comfortably from a phone without an extra login or CMS.
