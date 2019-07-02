# http://clarkgrubb.com/makefile-style-guide

MAKEFLAGS += --warn-undefined-variables --no-print-directory
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

export USERNAME=jscrobinson
export PASSWORD=empty

.PHONY: bumppatch
bumppatch:
	@bumpversion patch setup.py reckoner_values/__init__.py

.PHONY: init
init:
	@python3 -m pip install --user --upgrade setuptools wheel twine

.PHONY: clean
clean:
	@rm -fr build
	@rm -fr dist
	@rm -fr .eggs
	@rm -fr .pytest_cache

.PHONY: prebuild
prebuild: clean


.PHONY: build
build: prebuild
	@python setup.py sdist
	@python setup.py bdist_wheel --universal

.PHONY: testpush
testpush: build
	@python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --username $(USERNAME) --password $(PASSWORD)

.PHONY: push
push: testpush
	@python3 -m twine upload dist/* --username $(USERNAME) --password $(PASSWORD)

.PHONY: all
all: build push