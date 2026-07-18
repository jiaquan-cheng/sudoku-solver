import streamlit as st

from sudoku_solver import (
    Puzzle,
    SolverResult,
    get_default_puzzle,
    solve_puzzle,
)

try:
    st.title("Sudoku Solver")
    st.write(
        "Enter your Sudoku puzzle as an 81-character string (use 0 for empty cells). "
        "The solver does not check if puzzle has unique solution."
    )
    user_input = st.text_area(
        "Paste your 81-char puzzle:",
        value=get_default_puzzle(),
    )
    solve_button = st.button("Solve")

    if solve_button:
        try:
            puzzle = Puzzle.from_str(user_input)
        except ValueError as e:
            st.error(f"Invalid puzzle input: {e}")
            st.stop()

        result, solution = solve_puzzle(puzzle)
        if result == SolverResult.SAT and solution is not None:
            st.success("Solved Puzzle:" + "\n" + solution.as_str)
            st.write("Formatted Solution:")
            st.text(solution)
        elif result == SolverResult.UNSAT:
            st.error("The puzzle is unsolvable.")
        elif result == SolverResult.UNKNOWN:
            st.warning("The solver could not determine a solution.")
except Exception as e:  # noqa: BLE001
    st.error(f"Error: {e}")
