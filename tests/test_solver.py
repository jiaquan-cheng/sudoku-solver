from z3 import Solver, Int, sat, unsat
from sudoku_solver import add_sudoku_constraints, add_puzzle

def test_empty_grid_is_solvable():
    solver = Solver()
    grid = [[Int(f"{r}{c}") for c in range(9)] for r in range(9)]
    add_sudoku_constraints(solver, grid)
    result = solver.check()
    assert result == sat

def test_impossible_grid_fails():
    solver = Solver()
    grid = [[Int(f"{r}{c}") for c in range(9)] for r in range(9)]
    add_sudoku_constraints(solver, grid)
    broken_puzzle = [
        [5, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    add_puzzle(solver, broken_puzzle, grid)
    
    result = solver.check()
    
    assert result == unsat