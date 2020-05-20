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
$ conda create -n pelican python=3.7 jupyter notebook
$ source activate pelican
$ conda install -c conda-forge pelican Markdown ghp-import
```

Install the optional packages for the activated plugins:

```
# For "filetime_from_git" https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git
$ conda install -c conda-forge gitpython
```
```
# For "summary" https://github.com/getpelican/pelican-plugins/tree/master/summary
$ conda install -c conda-forge beautifulsoup4
```
For the extension embedding tweets: https://github.com/lqez/pelican-embed-tweet
```
$ wget https://github.com/lqez/pelican-embed-tweet/raw/master/embed_tweet.py
$ mv embed_tweet.py ../plugins/
# Edit the pelicanconf.py file accordingly.
```

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make github
```

## Attribution

This is based off the templates of both [Jake VanderPlas](https://jakevdp.github.io/)
and the theme's author, [Daniel Rodriguez](http://danielfrg.com/). Thanks to
both for all their work on Pelican blogs.
