from typing import List, Tuple, Dict, Any
from tools import read_ints_from_file 

def get_sum_to_2020(inputs: List[int]) -> Tuple[int, int]:
    """returns two numbers in the list that sums up to 2020
    """
    bag = set()
    for each_num in inputs:
        search = 2020 - each_num
        if search in bag:
            return each_num, search
        else:
            bag.add(each_num)
    raise ValueError("no two numbres sums to 2020")


def _update_lookup(bag: Dict[int, Any], num: int, numbers: List[int]) -> Dict[int, Any]:
    for each_num in numbers:
        bag.update(
            {num + each_num: (num, each_num)}
        )
    return bag


def get_triple_sum_to_2020(inputs: List[int]) -> Tuple[int, int, int]:
    """returns three numbers in the list that sums up to 2020
    """
    bag = {}  # all entries as {a + b : (a, b)}
    for n_, each_num in enumerate(inputs):
        search = 2020 - each_num
        if search in bag:
            int1, int2 = bag[search]
            return each_num, int1, int2
        else:
            bag = _update_lookup(bag, each_num, inputs[:n_])

    raise ValueError("cannot find 3 numbers that adds up to 2020")


if __name__ == "__main__":
    # part 1
    test1 = [1721, 979, 366, 299, 675, 1456]
    assert get_sum_to_2020(test1) == (299, 1721)

    input_a = read_ints_from_file("day1_A_input.txt")
    res = get_sum_to_2020(input_a)
    print(res[0] * res[1])

    # part 2
    assert get_triple_sum_to_2020(test1) == (675, 366, 979)

    part2 = get_triple_sum_to_2020(input_a)
    print(part2[0] * part2[1] * part2[2])
