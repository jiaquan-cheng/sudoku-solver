.PHONY: lint format test all

all: format lint test

lint:
	poetry run ruff check .
	poetry run mypy .

format:
	poetry run ruff format .

test:
	poetry run pytest

IMAGE_NAME = sudoku-solver

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm $(IMAGE_NAME) $(ARGS)

docker-clean:
	docker rmi -f $(IMAGE_NAME)