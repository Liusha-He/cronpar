SHELL := /bin/bash

init:
	pip install poetry
	poetry install

compile:
	poetry update

build:
	pipx install .

test:
	poetry run pytest tests/ --cov --cov-fail-under 89

format:
	poetry run black --preview --line-length 120 cronpar
	poetry run isort --line-length 120 cronpar

lint:
	poetry run black .
	poetry run isort .
	poetry run flake8 .

PHONY: init compile build test format lint
