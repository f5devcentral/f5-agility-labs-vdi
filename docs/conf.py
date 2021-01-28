# -*- coding: utf-8 -*-
#
#
# BEGIN CONFIG
# ------------
#
# REQUIRED: Your class/lab name
classname = "VDI the F5 Way"

# OPTIONAL: The URL to the GitHub Repository for this class
github_repo = "https://github.com/f5devcentral/f5-agility-labs-vdi"

# OPTIONAL: Google Analytics
# googleanalytics_id = 'UA-85156643-4'

#
# END CONFIG
# ----------

import os
import sys
import time
import re
import pkgutil
import string
sys.path.insert(0, os.path.abspath('.'))
import f5_sphinx_theme

year = time.strftime("%Y")
eventname = "Agility %s Hands-on Lab Guide" % (year)

rst_prolog = """
.. |classname| replace:: %s
.. |classbold| replace:: **%s**
.. |classitalic| replace:: *%s*
.. |ltm| replace:: Local Traffic Manager
.. |adc| replace:: Application Delivery Controller
.. |gtm| replace:: Global Traffic Manager
.. |dns| replace:: DNS
.. |asm| replace:: Application Security Manager
.. |afm| replace:: Advanced Firewall Manager
.. |apm| replace:: Access Policy Manager
.. |pem| replace:: Policy Enforcement Manager
.. |ipi| replace:: IP Intelligence
.. |iwf| replace:: iWorkflow
.. |biq| replace:: BIG-IQ
.. |bip| replace:: BIG-IP
.. |aiq| replace:: APP-IQ
.. |ve|  replace:: Virtual Edition
.. |icr| replace:: iControl REST API
.. |ics| replace:: iControl SOAP API
.. |f5|  replace:: F5 Networks
.. |f5i| replace:: F5 Networks, Inc.
.. |year| replace:: %s
.. |github_repo| replace:: %s
""" % (classname,
       classname,
       classname,
       year,
       github_repo)

if 'github_repo' in locals() and len(github_repo) > 0:
    rst_prolog += """
.. |repoinfo| replace:: The content contained here leverages a full DevOps CI/CD
              pipeline and is sourced from the GitHub repository at %s.
              Bugs and Requests for enhancements can be made by
              opening an Issue within the repository.
""" % (github_repo)
else:
    rst_prolog += ".. |repoinfo| replace:: \ \n"

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_snops = os.environ.get('SNOPS_ISALIVE', None) == 'True'

print("on_rtd = %s" % on_rtd)
print("on_snops = %s" % on_snops)

branch_map = {
    "stable":"master",
    "latest":"master"
}

try:
    if not on_rtd:
        from git import Repo
        repo = Repo("%s/../" % os.getcwd())
        git_branch = repo.active_branch
        git_branch_name = git_branch.name
    else:
        git_branch_name = os.environ.get('READTHEDOCS_VERSION', None)
except:
    git_branch_name = 'master'

print("guessed git branch: %s" % git_branch_name)

if git_branch_name in branch_map:
    git_branch_name = branch_map[git_branch_name]
    print(" remapped to git branch: %s" % git_branch_name)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
  'sphinx.ext.todo',
  'sphinx.ext.extlinks',
  'sphinx.ext.graphviz',
  'sphinxcontrib.nwdiag',
  'sphinxcontrib.blockdiag'
  #'sphinx.ext.autosectionlabel'
]

if 'googleanalytics_id' in locals() and len(googleanalytics_id) > 0:
  extensions += ['sphinxcontrib.googleanalytics']
  googleanalytics_enabled = True

graphviz_output_format = 'svg'
graphviz_font = 'DejaVu Sans:style=Book'
graphviz_dot_args = [
     "-Gfontname='%s'" % graphviz_font,
     "-Nfontname='%s'" % graphviz_font,
     "-Efontname='%s'" % graphviz_font
]

html_context = {
  "github_url":github_repo,
  "github_branch":git_branch_name
}

diag_fontpath = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
diag_html_image_format = 'SVG'
diag_latex_image_format = 'PNG'
diag_antialias = False

blockdiag_fontpath = nwdiag_fontpath = diag_fontpath
blockdiag_html_image_format = nwdiag_html_image_format = diag_html_image_format
blockdiag_latex_image_format = nwdiag_latex_image_format = diag_latex_image_format
blockdiag_antialias = nwdiag_antialias = diag_antialias

eggs_loader = pkgutil.find_loader('sphinxcontrib.spelling')
found = eggs_loader is not None

if found:
  extensions += ['sphinxcontrib.spelling']
  spelling_lang='en_US'
  spelling_word_list_filename='../wordlist'
  spelling_show_suggestions=True
  spelling_ignore_pypi_package_names=False
  spelling_ignore_wiki_words=True
  spelling_ignore_acronyms=True
  spelling_ignore_python_builtins=True
  spelling_ignore_importable_modules=True
  spelling_filters=[]

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = classname
copyright = '2019, F5 Networks, Inc.'
author = 'F5 Networks, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_emit_warnings = True
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'f5_sphinx_theme'
html_theme_path = f5_sphinx_theme.get_html_theme_path()
html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html','relations.html']}
html_theme_options = {
                        'site_name': 'Community Training Classes & Labs',
                        'next_prev_link': True
                     }
html_last_updated_fmt = '%Y-%m-%d %I:%M:%S'

def setup(app):
    app.add_css_file('css/f5_agility_theme.css')

if on_rtd:
    templates_path = ['_templates']

extlinks = {
    'issues':( ("%s/issues/%%s" % github_repo), 'issue ' )
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

cleanname = re.sub('\W+','',classname)

# Output file base name for HTML help builder.
htmlhelp_basename =  cleanname + 'doc'

# -- Options for LaTeX output ---------------------------------------------

front_cover_image = 'front_cover'
back_cover_image = 'back_cover'

front_cover_image_path = os.path.join('_static', front_cover_image + '.png')
back_cover_image_path = os.path.join('_static', back_cover_image + '.png')

latex_additional_files = [front_cover_image_path, back_cover_image_path]

template = string.Template(open('preamble.tex').read())

latex_contents = r"""
\frontcoverpage
\contentspage
"""

backcover_latex_contents = r"""
\backcoverpage
"""

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'preamble': template.substitute(eventname=eventname,
                                    project=project,
                                    author=author,
                                    frontcoverimage=front_cover_image,
                                    backcoverimage=back_cover_image),

    'tableofcontents': latex_contents,
    'printindex': backcover_latex_contents
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '%s.tex' % cleanname, '%s Documentation' % classname,
     'F5 Networks, Inc.', 'manual', True),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, cleanname.lower(), '%s Documentation' % classname,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, classname, '%s Documentation' % classname,
     author, classname, classname,
     'Training'),
]



