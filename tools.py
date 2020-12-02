from typing import List


def read_ints_from_file(filename: str) -> List[int]:
    lines = read_lines_from_file(filename)

    ints = [
            int(each_line.replace("\n", "")) for each_line in lines
    ]
    return ints

def read_lines_from_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines
