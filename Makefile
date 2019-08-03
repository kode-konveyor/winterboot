all: tests compile

compile: 
	./setup.py bdist_wheel

tests:	unittest mutationtest

unittest:
	tools/pyTestRunner

mutationtest:
	mutmut run

upload: compile
	python3 -m twine upload dist/*

clean:
	git clean -fdx
