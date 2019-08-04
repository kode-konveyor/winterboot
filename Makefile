all: deliver

deliver: compile
	mv dist shippable
	touch deliver

compile: tests shippable
	./setup.py bdist_wheel
	touch compile

shippable:
	mkdir -p shippable

tests:	unittest mutationtest
	touch tests

unittest:
	pyTestRunner
	touch unittest

mutationtest:
	python3 -m mutmut run
	touch mutationtest

publish_release: deliver
	python3 -m twine upload shippable/dist/*

clean:
	git clean -fdx
