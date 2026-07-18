from sudoku_solver import Puzzle, SolverResult, solve_puzzle


def test_empty_puzzle_is_solvable():
    empty_puzzle = Puzzle.from_str("0" * 81)
    result, _ = solve_puzzle(empty_puzzle)
    assert result == SolverResult.SAT


def test_impossible_puzzle_fails():
    impossible_puzzle = Puzzle.from_str(
        "550000000"
        "000000000"
        "000000000"
        "000000000"
        "000000000"
        "000000000"
        "000000000"
        "000000000"
        "000000000"
    )
    result, _ = solve_puzzle(impossible_puzzle)
    assert result == SolverResult.UNSAT
