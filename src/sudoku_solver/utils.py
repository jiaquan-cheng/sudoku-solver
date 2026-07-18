from dataclasses import dataclass

from z3 import ArithRef, ModelRef


@dataclass
class Puzzle:
    as_list_of_lists: list[list[int]]

    @property
    def as_str(self) -> str:
        return _list_of_lists_to_str(self.as_list_of_lists)

    def __str__(self) -> str:
        return _puzzle_to_str(self.as_list_of_lists)

    @classmethod
    def from_str(cls, puzzle_str: str) -> "Puzzle":
        _validate_puzzle_str(puzzle_str)
        return cls(as_list_of_lists=_str_to_list_of_lists(puzzle_str))

    @classmethod
    def from_solver(cls, model: ModelRef, grid: list[list[ArithRef]]) -> "Puzzle":
        data = [[model[c].as_long() for c in r] for r in grid]
        return cls(as_list_of_lists=data)

    def __post_init__(self) -> None:
        _validate_puzzle_list_of_lists(self.as_list_of_lists)


def _str_to_list_of_lists(s: str) -> list[list[int]]:
    return [[int(s[i * 9 + j]) for j in range(9)] for i in range(9)]


def _list_of_lists_to_str(puzzle: list[list[int]]) -> str:
    return "".join(str(num) for row in puzzle for num in row)


def _puzzle_to_str(puzzle: list[list[int]]) -> str:
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


def _validate_puzzle_str(puzzle: str) -> None:
    if not puzzle:
        raise ValueError("No puzzle input provided.")
    elif not isinstance(puzzle, str):
        raise ValueError(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input type is: " + str(type(puzzle))
        )
    elif len(puzzle) != 81:
        raise ValueError(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input length is: " + str(len(puzzle))
        )
    elif not puzzle.isdigit():
        raise ValueError(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input contains non-digit characters."
        )


def _validate_puzzle_list_of_lists(puzzle: list[list[int]]) -> None:
    if not puzzle:
        raise ValueError("No puzzle input provided.")
    elif not isinstance(puzzle, list):
        raise ValueError(
            "Puzzle must be a list of lists of integers (0-9). "
            "Your input type is: " + str(type(puzzle))
        )
    elif len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
        raise ValueError(
            "Puzzle must be a list of lists of dimensions 9x9. "
            f"Your input dimensions are: {len(puzzle)}x{len(puzzle[0])}"
        )
    else:
        for row_idx, row in enumerate(puzzle):
            if not isinstance(row, list):
                raise ValueError(f"Row {row_idx} is not a list.")

            for col_idx, num in enumerate(row):
                if not isinstance(num, int) or not (0 <= num <= 9):
                    raise ValueError(
                        f"Invalid value '{num}' found "
                        f"at position ({row_idx}, {col_idx}). "
                        "Values must be integers between 0 and 9."
                    )


def get_default_puzzle() -> str:
    return (
        "530070000"
        "600195000"
        "098000060"
        "800060003"
        "400803001"
        "700020006"
        "060000280"
        "000419005"
        "000080079"
    )
