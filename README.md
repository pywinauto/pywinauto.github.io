# Setup

To install "pelican":  
`pip install pelican`  
`pip install Markdown`  


# Site generation

To generate HTML sources from the provided markdown styles switch to `gh-pages` branch and run python 2.7:

`pelican content && python ghp-import.py -b master output`

