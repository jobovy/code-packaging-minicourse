# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'code-packaging-minicourse'
author = 'Jo Bovy'
# Also get the git hash for the current revision
try:
    import subprocess
    p = subprocess.Popen(['git','log','-1','--format=%h'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if out:
        git_hash= out.decode().strip()
except Exception:
    pass

# Get the date for the last commit (not necessarily today)
import time
try:
    import subprocess
    p = subprocess.Popen(['git','log','-1',
                          '--date=format:%a %b %d %H:%M:%S %Y',
                          '--format=%ad'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if out:
        git_time= time.strftime('%B %d, %Y',
                                time.strptime(out.decode().strip()))
        git_year= time.strftime('%Y',
                                time.strptime(out.decode().strip()))
except Exception:
    pass

if int(git_year) > 2020:
    copyright = '2020-{git_year}, Jo Bovy'.format(git_year=git_year)
else:
    copyright = '2020, Jo Bovy'

rst_epilog = """
.. |gitHash| replace:: {githash}
.. |gitTime| replace:: {gittime}
""".format(
    githash = git_hash,
    gittime = git_time,
    )

# To make sure that |today| is consistent with |gitTime| in format
today= "{}".format(time.strftime('%B %d, %Y',time.localtime()))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["nbsphinx","sphinx.ext.extlinks","sphinx_copybutton",
              "sphinx.ext.mathjax"]

# Link to PDF version that includs the git hash
extlinks = {'pdf_link': ('pdf/code-packaging-rev{}.pdf'.format(git_hash),
                         'PDF version')}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['.ipynb_checkpoints/*']


# -- Options for HTML output -------------------------------------------------

html_title= "Python code packaging for scientific software"

html_use_index= False

nbsphinx_prompt_width= 0.

nbsphinx_prolog = r"""

.. only:: html

   .. raw:: html
      
      <style>
      div.nbinput.container div.prompt,
      div.nboutput.container div.prompt {
       min-width: %(nbsphinx_prompt_width)s;
       padding-top: 0.3rem;
       padding-right: 0px;
       text-align: right;
       flex: 0;
      }
      div.nbinput.container div.input_area {
        border-color: #0c4762;
        border-style: dotted;
        border-width: thin;
        border-radius: 0px;
        background-color: #f0f0f0;
      }

      /* hide copybtn icon on output area */
      .nboutput a.copybtn {
        display: none;
      }
      </style>

"""

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'haiku'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'package.ico'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'package.png'

# -- Options for LaTeX output -------------------------------------------------

latex_documents= [
  ('index', 'code-packaging-minicourse.tex',
   u'Python code packaging for scientific software',
   u'Jo Bovy', 'manual',True),
]

latex_show_pagerefs= True

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{xcolor}
\definecolor{faintyellow}{HTML}{FBFBF5}

\newcommand{\githash}{"""
+"{}".format(git_hash)
+r"""}
\newcommand{\gittime}{"""
+"{}".format(git_time)
+r"""}
\newcommand{\mytoday}{"""
+"{}".format(time.strftime('%B %d, %Y',time.localtime()))
+r"""}

\sphinxsetup{VerbatimColor={named}{nbsphinx-code-bg}}
\sphinxsetup{VerbatimBorderColor={named}{nbsphinx-code-border}}
""",

# Title page
'maketitle': r"""
\makeatletter
\begin{titlepage}
\pagecolor{faintyellow}
\vspace*{9em}
{\raggedright\huge\texttt{Python code packaging for\par}\\
{\raggedleft\huge\texttt{scientific software}\par}
\vspace{1em}\centering{\includegraphics[width=0.25\textwidth]{package.png}}\\
\vspace{3em}
{\large\scshape Jo Bovy\\ (University of Toronto)\par}
\vspace{6.5em}
{Rev. \githash}\\
{Last changed \gittime}\\
{Last built \mytoday\vfill\par}
%{Last changed \gittime, rev. \githash; last built \mytoday\vfill\par}
\end{titlepage}
\makeatother
\nopagecolor

\vspace*{4em}
All of the code snippets and examples in these notes are being shared
under a \href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0
1.0 Public Domain} license, so you can re-use and re-mix them in your
own work. Otherwise, the text is shared under a
\href{https://creativecommons.org/licenses/by-nc-nd/4.0/}{CC BY-NC-ND
4.0 International} Creative Commons License, meaning that you may
distribute the work in full only, you are not allowed to modify it in
any way, and you may not use it for commercial means or to gain
monetary compensation (note that this summary is no substitute for the
full license terms).  \clearpage
""",

# No index
'printindex': '',
}

# -- Options for linkcheck output ---------------------------------------------

linkcheck_ignore = [
    'index.html','pdf/code-packaging-','https://sourceforge.net/'
]
