# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Cryptnox Product Documentation'
copyright = '2019 - 2026, Cryptnox SA'
author = 'Cryptnox'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx_multiversion']

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

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/cryptnox-logo.png'
html_favicon = '_static/favicon.png'

html_css_files = [
    'custom.css',
]

html_theme_options = {
    'analytics_id': 'GT-PJ7HDFB',
    'logo_only': False,
    'prev_next_buttons_location': 'none',
    'style_external_links': False,
    'style_nav_header_background': '#101f2e',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False,
}

html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

# -- sphinx-multiversion config ----------------------------------------------

smv_branch_whitelist   = r'^(main|v\d+\.\d+\.\d+)$'
smv_tag_whitelist      = r'^v\d+\.\d+\.\d+$'
smv_remote_whitelist   = r'^origin$'
smv_released_pattern   = r'^refs/(heads/v\d+\.\d+\.\d+|tags/v\d+\.\d+\.\d+)$'
smv_outputdir_format   = '{ref.name}'
smv_prefer_remote_refs = False
