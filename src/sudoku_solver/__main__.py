import argparse

from sudoku_solver.solver import (
    SolverResult,
    solve_puzzle,
)
from sudoku_solver.utils import (
    get_default_puzzle,
    list_of_lists_to_str,
    puzzle_to_str,
    str_to_list_of_lists,
    validate_puzzle_string,
)


def main():
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

    if not args.puzzle:
        puzzle = str_to_list_of_lists(get_default_puzzle())
    else:
        try:
            validate_puzzle_string(args.puzzle)
        except ValueError as e:
            print(f"Invalid puzzle input: {e}")
            return

        puzzle = str_to_list_of_lists(args.puzzle)

    print(puzzle_to_str(puzzle))

    result, solution = solve_puzzle(puzzle)
    if result == SolverResult.SAT:
        print("Found a solution!")
        print("Solution:" + list_of_lists_to_str(solution))
        print("Formatted Solution:")
        print(puzzle_to_str(solution))
    elif result == SolverResult.UNSAT:
        print("This puzzle is logically impossible.")
    elif result == SolverResult.UNKNOWN:
        print("The solver timed out or got stuck (unknown).")


if __name__ == "__main__":
    main()
