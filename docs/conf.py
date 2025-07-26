# Configuration file for the Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Kraken Wallet'
copyright = '2025'
author = 'Carson McCullers'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

extensions = ['sphinx_sitemap']
html_baseurl = "https://krakenhelpusa.readthedocs.io/en/latest/"
