.PHONY: lint format test all

all: format lint test

lint:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run ruff format .

test:
	poetry run pytest