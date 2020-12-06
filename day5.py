from typing import List
from tools import read_lines_from_file


BINARY_MAP = {
    "F": 0,
    "B": 1,
    "R": 1,
    "L": 0
}

ROW_FACTOR = [64, 32, 16, 8, 4, 2, 1]
COL_FACTOR = [4, 2, 1]


def decode_row(input: str) -> int:
    row = 0

    for n_, char in enumerate(input[:6]):
        row += BINARY_MAP[char] * ROW_FACTOR[n_]

    return row


def decode_col(input: str) -> int:
    col = 0
    for n_, char in enumerate(input[-3:]):
        col += BINARY_MAP[char] * COL_FACTOR[n_]
    return col


def calc_id(input: str) -> int:
    row = decode_row(input)
    col = decode_col(input)
    return row * 8 + col


def highest_id(inputs: List[str]) -> int:
    current_max = 0
    for in_ in inputs:
        in_ = in_.replace("\n", "")
        id_ = calc_id(in_)
        if id_ >= current_max:
            current_max = id_
    return current_max


if __name__ == "__main__":

    test1 = "BFFFBBFRRR"  #  row 70, column 7, seat ID 567.
    test2 = "FFFBBBFRRR"  # : row 14, column 7, seat ID 119.
    test3 = "BBFFBBFRLL"  # : row 102, column 4, seat ID 820.

    assert decode_row(test1) == 70
    assert decode_row(test2) == 14
    assert decode_row(test3) == 102

    assert decode_col(test1) == 7
    assert decode_col(test2) == 7
    assert decode_col(test3) == 4

    assert calc_id(test1) == 567
    assert calc_id(test2) == 119
    assert calc_id(test3) == 820

    inputs_ = read_lines_from_file("day5_A_input.txt")
    import pdb; pdb.set_trace()
    print(highest_id(inputs_))
