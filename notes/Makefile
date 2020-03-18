# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

latexpdf: Makefile
	mkdir -p build/latex
	cp "$(SOURCEDIR)/package.png" "$(BUILDDIR)/latex"
	- bash -c ' (make latex LATEXMKOPTS="-f" LATEXOPTS="-f -interaction=nonstopmode" PAPER="letter") || echo itsallfine '
	sed 's/\\llap{\\color{nbsphinxin}\[[0-9]*\]:\\,\\hspace{\\fboxrule}\\hspace{\\fboxsep}}//g' build/latex/code-packaging-minicourse.tex > tmp
	mv tmp build/latex/code-packaging-minicourse.tex
	make -C build/latex code-packaging-minicourse.pdf LATEXMKOPTS="-f" LATEXOPTS="-f -interaction=nonstopmode" PAPER="letter"

html: Makefile
	- bash -c ' (make latexpdf LATEXMKOPTS="-f" LATEXOPTS="-f -interaction=nonstopmode" PAPER="letter") || echo itsallfine '
	mkdir -p build/html/pdf
	rm -f build/html/pdf/code-packaging-*.pdf
	cp build/latex/code-packaging-minicourse.pdf build/html/pdf/code-packaging-rev"$(shell python get_git_hash.py)".pdf
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -a $(O)

purehtml: Makefile
	@$(SPHINXBUILD) -M $(subst pure,,$@) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
