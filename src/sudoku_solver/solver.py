from enum import Enum

from z3 import ArithRef, Distinct, Int, ModelRef, Solver, sat, unknown, unsat


class SolverResult(Enum):
    SAT = "sat"
    UNSAT = "unsat"
    UNKNOWN = "unknown"


def _solution_to_list_of_lists(
    model: ModelRef, grid: list[list[ArithRef]]
) -> list[list[int]]:
    return [[model[c].as_long() for c in r] for r in grid]


def _add_puzzle(solver: Solver, puzzle: list[list[int]], grid: list[list[ArithRef]]):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                solver.add(grid[r][c] == puzzle[r][c])


def _add_sudoku_constraints(solver: Solver, grid: list[list[ArithRef]]):
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
            box = [
                grid[i][j]
                for i in range(r_start, r_start + 3)
                for j in range(c_start, c_start + 3)
            ]
            solver.add(Distinct(box))


def solve_puzzle(
    puzzle: list[list[int]],
) -> tuple[SolverResult, list[list[int]] | None]:
    grid = [[Int(f"{r}{c}") for c in range(9)] for r in range(9)]
    solver = Solver()
    _add_puzzle(solver, puzzle, grid)
    _add_sudoku_constraints(solver, grid)

    result = solver.check()

    if result == sat:
        return SolverResult.SAT, _solution_to_list_of_lists(solver.model(), grid)
    elif result == unsat:
        return SolverResult.UNSAT, None
    elif result == unknown:
        return SolverResult.UNKNOWN, None
    else:
        raise ValueError(f"Unexpected result from solver: {result}")
