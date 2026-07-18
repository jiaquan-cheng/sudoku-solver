import argparse

from sudoku_solver.solver import (
    SolverResult,
    solve_puzzle,
)
from sudoku_solver.utils import (
    Puzzle,
    get_default_puzzle,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle.")
    parser.add_argument(
        "puzzle",
        nargs="?",
        type=str,
        help=(
            "Optional 81-digit string representation of the puzzle, 0 for empty cells."
        ),
    )
    args = parser.parse_args()

    try:
        puzzle = Puzzle.from_str(args.puzzle or get_default_puzzle())
    except ValueError as e:
        print(f"Invalid puzzle input: {e}")
        return

    print(puzzle)

    result, solution = solve_puzzle(puzzle)
    if result == SolverResult.SAT and solution is not None:
        print("Found a solution!")
        print("Solution:" + solution.as_str)
        print("Formatted Solution:")
        print(solution)
    elif result == SolverResult.UNSAT:
        print("This puzzle is logically impossible.")
    elif result == SolverResult.UNKNOWN:
        print("The solver timed out or got stuck (unknown).")


if __name__ == "__main__":
    main()
