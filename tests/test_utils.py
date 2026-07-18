import pytest

from sudoku_solver import Puzzle


def test_empty_puzzle_string() -> None:
    with pytest.raises(ValueError):
        Puzzle.from_str("")


def test_invalid_str_type() -> None:
    with pytest.raises(ValueError):
        Puzzle.from_str(123)  # type: ignore[arg-type]


def test_invalid_string_length() -> None:
    with pytest.raises(ValueError):
        Puzzle.from_str("123")


def test_invalid_string_characters() -> None:
    with pytest.raises(ValueError):
        Puzzle.from_str("12345678X" * 9)


def test_round_trip_conversion() -> None:
    original = "1" * 81
    puzzle = Puzzle.from_str(original)
    assert puzzle.as_str == original


def test_empty_puzzle_list() -> None:
    with pytest.raises(ValueError):
        Puzzle(as_list_of_lists=[])


def test_invalid_list_type() -> None:
    with pytest.raises(ValueError):
        Puzzle(as_list_of_lists="not a list")  # type: ignore[arg-type]


def test_invalid_list_dimensions() -> None:
    with pytest.raises(ValueError):
        Puzzle(as_list_of_lists=[[0] * 9 for _ in range(8)])


def test_invalid_row_type() -> None:
    with pytest.raises(ValueError):
        Puzzle(as_list_of_lists=[[0] * 9 for _ in range(8)] + [tuple([0] * 9)])  # type: ignore[list-item]


def test_invalid_values_in_grid() -> None:
    with pytest.raises(ValueError):
        invalid_grid = [[10] + [0] * 8 for _ in range(9)]
        Puzzle(as_list_of_lists=invalid_grid)
