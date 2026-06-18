# Sudoku Solver

[![CI](https://github.com/jiaquan-cheng/sudoku-solver/actions/workflows/ci.yml/badge.svg?branch=ci-testing)](https://github.com/jiaquan-cheng/sudoku-solver/actions/workflows/ci.yml)

Sudoku Solver built using the Z3 SMT solver.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the dependencies, run:

```bash
poetry install
```

## Usage

Change the `puzzle` variable in `solver.py` to solve different puzzles. The solution will be printed to the console. To execute the solver, run:

```bash
poetry run solve
```
