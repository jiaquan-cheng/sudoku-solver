from enum import Enum

from z3 import ArithRef, Int, ModelRef, Solver, sat, unknown, unsat


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

    # rows must have distinct values
    for r in grid:
        for ic, c in enumerate(r):
            for c2 in r[ic + 1 :]:
                solver.add(c != c2)

    # columns must have distinct values
    for ir, r in enumerate(grid):
        for r2 in grid[ir + 1 :]:
            for ic in range(len(r)):
                solver.add(r[ic] != r2[ic])

    # 3x3 box constraints
    for br in range(3):
        for bc in range(3):
            box_cells = [
                grid[r][c]
                for r in range(br * 3, br * 3 + 3)
                for c in range(bc * 3, bc * 3 + 3)
            ]

            for i, c in enumerate(box_cells):
                for c2 in box_cells[i + 1 :]:
                    solver.add(c != c2)


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
