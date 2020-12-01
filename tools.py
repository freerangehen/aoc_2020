from typing import List


def read_ints_from_file(filename: str) -> List[int]:
    with open(filename, "r") as f:
        lines = f.readlines()
        ints = [
            int(each_line.replace("\n", "")) for each_line in lines
        ]
    return ints
