from sudoku_solver.solver import (
    solve_puzzle,
    str_to_list_of_lists,
    SolverResult,
    puzzle_to_str,
    list_of_lists_to_str,
)
import argparse


def main():
    try:

        parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle.")
        parser.add_argument(
            "puzzle",
            nargs="?",
            type=str,
            help="optional 81-digit string representation of the puzzle, 0 for empty cells.",
        )
        args = parser.parse_args()

        if not args.puzzle:
            puzzle = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ]
        elif len(args.puzzle) != 81:
            raise ValueError(
                "Puzzle must be an 81-character string of digits (0-9). Your input length is: "
                + str(len(args.puzzle))
            )
        elif not args.puzzle.isdigit():
            raise ValueError(
                "Puzzle must be an 81-character string of digits (0-9). Your input contains non-digit characters."
            )
        else:
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
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
