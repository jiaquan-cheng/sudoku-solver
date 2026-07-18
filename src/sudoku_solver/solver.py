from enum import Enum

from z3 import ArithRef, Distinct, Int, Solver, sat, unknown, unsat

from sudoku_solver.utils import Puzzle


class SolverResult(Enum):
    SAT = "sat"
    UNSAT = "unsat"
    UNKNOWN = "unknown"


def _add_puzzle(solver: Solver, puzzle: Puzzle, grid: list[list[ArithRef]]) -> None:
    for r in range(9):
        for c in range(9):
            if puzzle.as_list_of_lists[r][c] != 0:
                solver.add(grid[r][c] == puzzle.as_list_of_lists[r][c])


def _add_sudoku_constraints(solver: Solver, grid: list[list[ArithRef]]) -> None:
    # cells must be between 1 and 9
    for r in grid:
        for c in r:
            solver.add(c >= 1, c <= 9)

    # rows and columns must have distinct values
    for i in range(9):
        solver.add(Distinct(grid[i]))
        solver.add(Distinct([grid[r][i] for r in range(9)]))

    # 3x3 box constraints
    for r_start in range(0, 9, 3):
        for c_start in range(0, 9, 3):
            solver.add(Distinct(_get_box(grid, r_start, c_start)))


def _get_box(grid: list[list[ArithRef]], r_start: int, c_start: int) -> list[ArithRef]:
    return [
        grid[r][c]
        for r in range(r_start, r_start + 3)
        for c in range(c_start, c_start + 3)
    ]


def solve_puzzle(
    puzzle: Puzzle,
    timeout_ms: int | None = None,
) -> tuple[SolverResult, Puzzle | None]:
    grid = [[Int(f"{r}{c}") for c in range(9)] for r in range(9)]
    solver = Solver()
    if timeout_ms is not None:
        solver.set(timeout=timeout_ms)
    _add_puzzle(solver, puzzle, grid)
    _add_sudoku_constraints(solver, grid)

    result = solver.check()

    if result == sat:
        return SolverResult.SAT, Puzzle.from_solver(solver.model(), grid)
    elif result == unsat:
        return SolverResult.UNSAT, None
    elif result == unknown:
        return SolverResult.UNKNOWN, None
    else:
        raise ValueError(f"Unexpected result from solver: {result}")
