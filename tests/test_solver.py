from sudoku_solver import SolverResult, solve_puzzle


def test_empty_puzzle_is_solvable():
    empty_puzzle = [[0] * 9 for _ in range(9)]
    result, _ = solve_puzzle(empty_puzzle)
    assert result == SolverResult.SAT


def test_impossible_puzzle_fails():
    impossible_puzzle = [
        [5, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    result, _ = solve_puzzle(impossible_puzzle)
    assert result == SolverResult.UNSAT
