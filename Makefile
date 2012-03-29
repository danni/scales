scales.pdf: scales.ly scales-include.ly
	lilypond $<

scales-include.ly: scales.py
	python < $< > $@
