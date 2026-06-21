from sudoku_solver.solver import solve_puzzle
import argparse

def str_to_list_of_lists(s: str) -> list[list[int]]:
    assert len(s) == 81, "Input string must be 81 characters long"
    return [[int(s[i * 9 + j]) for j in range(9)] for i in range(9)]

def list_of_lists_to_str(puzzle: list[list[int]]) -> str:
    return ''.join(str(num) for row in puzzle for num in row)

def main():
    parser = argparse.ArgumentParser(description="Solve a Sudoku puzzle.")
    parser.add_argument("puzzle", nargs="?", type=str, help="optional 81-digit string representation of the puzzle, 0 for empty cells.")
    args = parser.parse_args()
    
    if args.puzzle:
        puzzle = str_to_list_of_lists(args.puzzle)
    else: 
        puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]


    print(f"Puzzle as string: {list_of_lists_to_str(puzzle)}")

    solve_puzzle(puzzle)

if __name__ == "__main__":
    main()
