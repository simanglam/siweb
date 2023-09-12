all: sitangle.texw
	make sitangle
	make weave

sitangle: sitangle.texw
	sitangle sitangle.py sitangle.texw

siweave: sitangle.texw
	sitangle siweave.py sitangle.texw

weave: sitangle.texw
	pweave -f texpweave sitangle.texw
	xelatex --shell-escape -8bit sitangle.tex