## Diplomatik Static Docs

Documentation is served by Jekyll and uses [just-the-docs](https://github.com/just-the-docs/just-the-docs) template. 
The docs is updated in prod via github actions at `.github/workflows/pages.yml` everytime the contents in this `docs` 
directory is changed. 

To have view the docs locally via Jekyll, do the following:

1. Make sure Ruby is running on your system
2. `bundle install`
3. `bundle exec jekyll serve`