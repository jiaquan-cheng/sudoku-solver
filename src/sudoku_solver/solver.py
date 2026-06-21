from z3 import Int, Solver, sat, unsat, ModelRef, ArithRef

def print_puzzle(puzzle: list[list[int]]):
    for ir, r in enumerate(puzzle):
        for ic, c in enumerate(r):
            print(c, end=" ")
            if ic == 2 or ic == 5:
                print("|", end=" ")
        print("")
        if ir == 2 or ir == 5:
            print("-" * 21)
 
def print_solution(model: ModelRef, grid: list[list[ArithRef]]):
    for ir, r in enumerate(grid):
        for ic, c in enumerate(r):
            print(model[c], end=" ")
            if ic == 2 or ic == 5:
                print("|", end=" ")
        print("")    
        if ir == 2 or ir == 5:
            print("-" * 21)       
            
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
            for c2 in r[ic + 1:]:
                solver.add(c != c2)
    
    # columns must have distinct values
    for ir, r in enumerate(grid):
        for r2 in grid[ir + 1:]:
            for ic in range(len(r)):
                solver.add(r[ic] != r2[ic])

    # 3x3 box constraints
    for br in range(3):
        for bc in range(3):
            box_cells = [grid[r][c] for r in range(br*3, br*3 + 3) for c in range(bc*3, bc*3 + 3)]
            
            for i, c in enumerate(box_cells):
                for c2 in box_cells[i + 1:]:
                    solver.add(c != c2)


def solve_puzzle(puzzle: list[list[int]]):
    assert puzzle is not None, "Puzzle must be provided"
    assert len(puzzle) == 9 and all(len(r) == 9 for r in puzzle), "Puzzle must be 9x9"
    print_puzzle(puzzle)
    
    grid = [[Int(f"{r}{c}") for c in range(9)] for r in range(9)]
    solver = Solver()
    add_puzzle(solver, puzzle, grid)
    add_sudoku_constraints(solver, grid)
    
    result = solver.check()

    if result == sat:
        print("Found a solution!")
        model = solver.model()
        print_solution(model, grid)
    elif result == unsat:
        print("This puzzle is logically impossible.")
    else:
        print("The solver timed out or got stuck (unknown).")
    