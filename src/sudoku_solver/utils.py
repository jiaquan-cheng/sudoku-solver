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


def validate_puzzle_string(s: str) -> None:
    if not s:
        raise ValueError("No puzzle input provided.")
    if len(s) != 81:
        raise ValueError(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input length is: " + str(len(s))
        )
    if not s.isdigit():
        raise ValueError(
            "Puzzle must be an 81-character string of digits (0-9). "
            "Your input contains non-digit characters."
        )


def get_default_puzzle() -> str:
    return "530070000600195000098000060800060003400803001700020006060000280000419005000080079"  # noqa: E501
