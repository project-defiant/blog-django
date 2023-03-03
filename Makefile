SHELL := /usr/bin/bash
VERSION := $(shell grep "version" setup.cfg | cut -f3 -d" ")
.ONESHELL:

install:
	python3 -m venv .venv
	. .venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install --upgrade setuptools wheel
	python -m pip install -e .[dev]


clean:
	rm -rf .venv
	rm -rf build
	rm -rf *.egg-info

typecheck:
	. .venv/bin/activate
	mypy ./src

format:
	. .venv/bin/activate
	@isort ./src ./tests
	@black ./src ./tests
	@docformatter --in-place ./src ./tests

lint:
	. .venv/bin/activate
	flake8 ./src
	pylint ./src

test:
	. .venv/bin/activate
	pytest -vv -s

changelog:
	. .venv/bin/activate
	towncrier

start-db:
	docker compose --env-file .env up -d
