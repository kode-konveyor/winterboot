all: tests compile

compile: 
	./setup.py bdist_wheel

tests:
	tools/pyTestRunner

upload: compile
	python3 -m twine upload dist/*

clean:
	git clean -fdx
