all: assignment1.pdf assignment2.pdf assignment3.pdf

%.pdf: %.tex
	pdflatex $<
	pdflatex $<
	pdflatex $<
	- bash -c " ( grep Rerun $*.log && pdflatex $< ) || echo noRerun "
	- bash -c " ( grep Rerun $*.log && pdflatex $< ) || echo noRerun "

.PHONY: clean

clean:
	$(RM) *.log *.aux *.dvi *.out *.bib
	$(RM) *~

spotless: clean
	$(RM) assignment1.pdf
	$(RM) assignment2.pdf
	$(RM) assignment3.pdf
