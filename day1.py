from typing import List, Tuple
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


if __name__ == "__main__":
    test1 = [1721, 979, 366, 299, 675, 1456]
    assert get_sum_to_2020(test1) == (299, 1721)

    input_a = read_ints_from_file("day1_A_input.txt")
    res = get_sum_to_2020(input_a)
    print(res[0] * res[1])

