import os
import sys
# On indique à Sphinx où se trouve le code source
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../app'))


project = 'toolbox'
copyright = '2026, seb'
author = 'seb'
release = 'mark1'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',    # Génère la doc à partir des docstrings
    'sphinx.ext.napoleon',   # Supporte le format Google/NumPy
    'sphinx.ext.viewcode',   # Ajoute des liens vers le code source
    'myst_parser',           # Permet de lire le README.md (Markdown)
]

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'  # Thème moderne avec mode sombre automatique



html_theme = 'alabaster'
html_static_path = ['_static']
