import streamlit as st

from sudoku_solver import (
    SolverResult,
    get_default_puzzle,
    list_of_lists_to_str,
    puzzle_to_str,
    solve_puzzle,
    str_to_list_of_lists,
    validate_puzzle_string,
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

    try:
        validate_puzzle_string(user_input)
    except ValueError as e:
        st.error(f"Invalid puzzle input: {e}")
        st.stop()

    if solve_button:
        puzzle = str_to_list_of_lists(user_input)
        result, solution = solve_puzzle(puzzle)
        if result == SolverResult.SAT and solution is not None:
            solution_str = list_of_lists_to_str(solution)
            st.success("Solved Puzzle:" + "\n" + solution_str)
            st.write("Formatted Solution:")
            st.text(puzzle_to_str(solution))
        elif result == SolverResult.UNSAT:
            st.error("The puzzle is unsolvable.")
        elif result == SolverResult.UNKNOWN:
            st.warning("The solver could not determine a solution.")
except Exception as e:  # noqa: BLE001
    st.error(f"Error: {e}")
