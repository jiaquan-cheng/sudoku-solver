# Sudoku Solver

[![CI](https://github.com/jiaquan-cheng/sudoku-solver/actions/workflows/ci.yaml/badge.svg)](https://github.com/jiaquan-cheng/sudoku-solver/actions/workflows/ci.yaml) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sudoku-solver-jia.streamlit.app/)

Sudoku Solver built using the Z3 SMT solver.

## Demo
You can try the solver online [here](https://sudoku-solver-jia.streamlit.app/).

## Installation
**Prerequisites**: Python 3.13+ and [Poetry](https://python-poetry.org/).

To install the dependencies, run:

```bash
poetry install
```

## Usage

If you run without any arguments, the program will solve a default Sudoku puzzle.

```bash
poetry run solve
```

You can also provide a Sudoku puzzle as a 81-character string (use 0 for empty cells):

```bash
poetry run solve "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

```

Note: The solver does not check if the puzzle has a unique solution.

## Docker
Build the image:
```bash
make docker-build
```

Run with default puzzle:

```bash
make docker-run
```

Provide a puzzle:

```bash
make docker-run ARGS="530070000600195000098000060800060003400803001700020006060000280000419005000080079"

```

Clean up the image:

```bash
make docker-clean
```

Note: You can run `docker builder prune` to clean up unused build cache.

## Development

To install the dependencies for development, run:

```bash
poetry install --with dev
```

- `make` : Runs the test suite and quality checks.
- `make lint` : Runs [Ruff](https://docs.astral.sh/ruff/) and [Mypy](https://mypy-lang.org/) for code quality and type safety.
- `make format` : Auto-format code.
- `make test` : Runs [Pytest](https://pytest.org/).
- `make test-cov` : Runs tests with coverage report.