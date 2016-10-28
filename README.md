# Setup

To install "pelican":
`pip install pelican`

To use ghp-import on MS Windows use version 0.4.2 that is currently only available from its repository:  
`pip install https://github.com/davisp/ghp-import/archive/master.zip`


# Site generation

To generate HTML sources from the provided markdown styles switch to `gh-pages` branch and run:
`pelican content && ghp-import -b master output`

