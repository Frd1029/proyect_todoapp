black: 
	black test_linters.py

flake8:
	flake8 test_linters.py

linters:
	make flake8
	make black

#Comentario