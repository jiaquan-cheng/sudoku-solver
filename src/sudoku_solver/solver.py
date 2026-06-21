from z3 import Int, Solver, ModelRef, ArithRef, sat, unsat, unknown
from enum import Enum


class SolverResult(Enum):
    SAT = "sat"
    UNSAT = "unsat"
    UNKNOWN = "unknown"


def str_to_list_of_lists(s: str) -> list[list[int]]:
    return [[int(s[i * 9 + j]) for j in range(9)] for i in range(9)]


def list_of_lists_to_str(puzzle: list[list[int]]) -> str:
    return "".join(str(num) for row in puzzle for num in row)


def puzzle_to_str(puzzle: list[list[int]]) -> str:
    lines = []
    for ir, r in enumerate(puzzle):
        row_str = ""
        for ic, c in enumerate(r):
            row_str += f"{c} "
            if ic == 2 or ic == 5:
                row_str += "| "
        lines.append(row_str)
        if ir == 2 or ir == 5:
            lines.append("-" * 21)
    return "\n".join(lines)


def solution_to_list_of_lists(
    model: ModelRef, grid: list[list[ArithRef]]
) -> list[list[int]]:
    return [[model[c].as_long() for c in r] for r in grid]


def add_puzzle(solver: Solver, puzzle: list[list[int]], grid: list[list[ArithRef]]):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                solver.add(grid[r][c] == puzzle[r][c])


def add_sudoku_constraints(solver: Solver, grid: list[list[ArithRef]]):

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
    add_puzzle(solver, puzzle, grid)
    add_sudoku_constraints(solver, grid)

    result = solver.check()

    if result == sat:

        return SolverResult.SAT, solution_to_list_of_lists(solver.model(), grid)
    elif result == unsat:
        return SolverResult.UNSAT, None
    elif result == unknown:
        return SolverResult.UNKNOWN, None
    else:
        raise ValueError(f"Unexpected result from solver: {result}")
