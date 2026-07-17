.PHONY: lint format test test-cov all docker-build docker-run docker-clean

PACKAGE_NAME = sudoku_solver

IMAGE_NAME = sudoku-solver

all: format lint test-cov

lint:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run ruff format .

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=$(PACKAGE_NAME) --cov-branch --cov-report=term-missing

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm $(IMAGE_NAME) $(ARGS)

docker-clean:
	docker rmi -f $(IMAGE_NAME)