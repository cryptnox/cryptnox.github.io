# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Cryptnox Docs'
copyright = '2026, Cryptnox'
author = 'Cryptnox'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- SEO meta tags -----------------------------------------------------------

html_baseurl = 'https://docs.cryptnox.com/'

html_meta = {
    'description': 'Access the official Cryptnox technical documentation. Explore setup guides, features, and integration details for secure and efficient solutions.',
    'keywords': 'Cryptnox, hardware wallet, smartcard, JavaCard, CLI, SDK, documentation, BIP32, ECDSA, NFC, secure element',
    'author': 'Cryptnox',
    'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'basic'
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

# Disable sidebar — landing page needs no navigation panel
html_sidebars = {'**': []}

html_show_sourcelink = False
html_copy_source = False
