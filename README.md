# Source for Stochastic Stenography

This repository contains the source for https://magsol.github.io.

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/magsol/magsol.github.io-source.git
$ git submodule update --init --recursive
```

Install the required packages:

```
$ conda create -n pelican-blog python=3.5 jupyter notebook
$ source activate pelican-blog
$ pip install pelican Markdown ghp-import
```

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish-to-github
```

## Attribution

This is based off the templates of both [Jake VanderPlas](https://jakevdp.github.io/)
and the theme's author, [Daniel Rodriguez](http://danielfrg.com/). Thanks to
both for all their work on Pelican blogs.
