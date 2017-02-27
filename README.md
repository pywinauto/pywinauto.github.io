# Setup

To install "pelican":  
`pip install pelican`  
`pip install Markdown`  

# Site preview

Make sure you are at `gh-pages` Git branch.
`cd output`
Python2.7: `python -m SimpleHTTPServer`

# Site generation

To generate HTML sources from the provided markdown styles switch to `gh-pages` branch and run python 2.7:

`pelican content && python ghp_import.py -b master output`

Optionally, use commit_html.cmd to have a nice commit message in the master branch linking to the appropriate commit hash in gh-pages

