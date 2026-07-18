from sudoku_solver import Puzzle, SolverResult, get_default_puzzle, solve_puzzle


def test_empty_puzzle_is_solvable() -> None:
    empty_puzzle = Puzzle.from_str("0" * 81)
    result, _ = solve_puzzle(empty_puzzle)
    assert result == SolverResult.SAT


def test_default_puzzle_is_solvable() -> None:
    default_puzzle = Puzzle.from_str(get_default_puzzle())
    result, solution = solve_puzzle(default_puzzle)
    assert result == SolverResult.SAT
    assert solution is not None
    assert "0" not in solution.as_str


def test_impossible_puzzle_fails() -> None:
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
