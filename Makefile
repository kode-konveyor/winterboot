all: tests compile

compile: 
	./setup.py bdist_wheel

tests:	unittest mutationtest

unittest:
	pyTestRunner

mutationtest:
	python3 -m mutmut run

upload: compile
	python3 -m twine upload dist/*

clean:
	git clean -fdx
