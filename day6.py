from typing import List

from tools import read_text_from_file


def yes_sum1(input: List[str]) -> int:
    sum_ = 0
    for grp in input:
        sum_ += len(set(grp))
    return sum_


def split_groups1(input: str) -> List[str]:
    grps = input.split("\n\n")
    grps = [grp.replace("\n", "").replace(" ", "") for grp in grps]
    return grps


def yes_sum2(input: str) -> List[List[str]]:
    grps = input.split("\n\n")

    sum_ = 0
    for grp in grps:
        grp_ans = []
        for person in grp.split("\n"):
            ans = person.replace(" ", "")
            ans = set(ans)
            if len(ans) > 0:
                grp_ans.append(ans)
        sum_ += len(set.intersection(*grp_ans))

    return sum_


if __name__ == "__main__":
    test1 = """
abc

a
b
c

ab
ac

a
a
a
a

b
    """
    assert yes_sum1(split_groups1(test1)) == 11

    input_ = read_text_from_file("day6_A_input.txt")
    print(yes_sum1(split_groups1(input_)))

    # part 2
    print(yes_sum2(test1))

    print(yes_sum2(input_))
