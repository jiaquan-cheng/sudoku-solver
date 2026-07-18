.PHONY: lint format test test-cov all docker-build docker-run docker-clean

PACKAGE_NAME = sudoku_solver

IMAGE_NAME = sudoku-solver

DATA_DIR = data

PROFILE_PATH = $(DATA_DIR)/profile.html

all: format lint test-cov

lint:
	poetry run ruff check . --fix
	poetry run mypy .

format:
	poetry run ruff format .

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=$(PACKAGE_NAME) --cov-branch --cov-report=term-missing

profile:
	poetry run pyinstrument -m ${PACKAGE_NAME} 

profile-html:
	poetry run pyinstrument -r html -o $(PROFILE_PATH) -m ${PACKAGE_NAME}

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm $(IMAGE_NAME) $(PUZZLE)

docker-clean:
	docker rmi -f $(IMAGE_NAME)