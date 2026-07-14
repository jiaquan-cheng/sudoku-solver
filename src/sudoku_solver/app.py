import streamlit as st
from solver import (
    SolverResult,
    list_of_lists_to_str,
    puzzle_to_str,
    solve_puzzle,
    str_to_list_of_lists,
)

try:
    st.title("Sudoku Solver")
    st.write(
        "Enter your Sudoku puzzle as an 81-character string (use 0 for empty cells). "
        "The solver does not check if puzzle has unique solution."
    )
    user_input = st.text_area(
        "Paste your 81-char puzzle:",
        value="530070000600195000098000060800060003400803001700020006060000280000419005000080079",
    )
    solve_button = st.button("Solve")

    if not user_input:
        st.error("No puzzle input provided.")
        st.stop()
    elif len(user_input) != 81:
        st.error(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input length is: " + str(len(user_input))
        )
        st.stop()
    elif not user_input.isdigit():
        st.error(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input contains non-digit characters."
        )
        st.stop()
    if solve_button:
        puzzle = str_to_list_of_lists(user_input)
        result, solution = solve_puzzle(puzzle)
        if result == SolverResult.SAT:
            solution_str = list_of_lists_to_str(solution)
            st.success("Solved Puzzle:" + "\n" + solution_str)
            st.write("Formatted Solution:")
            st.text(puzzle_to_str(solution))
        elif result == SolverResult.UNSAT:
            st.error("The puzzle is unsolvable.")
        elif result == SolverResult.UNKNOWN:
            st.warning("The solver could not determine a solution.")
except Exception as e:
    st.error(f"Error: {e}")
