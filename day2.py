from typing import List, Dict, Any, Tuple
from tools import read_lines_from_file


def check_valid_2(loc1: int, loc2: int, char: str, passwd: str) -> bool:
    # edge case is len(passwd) < loc2 or loc1 or both
    if loc1 > len(passwd) and loc2 > len(passwd):
        return False
    elif loc1 > len(passwd): # single test case
        return passwd[loc2] == char
    elif loc2 > len(passwd): # sigle test case
        return passwd[loc1] == char
    else: # one and only one of loc1, loc2 should match
        return (
            passwd[loc1] == char and passwd[loc2] != char
        ) or (
            passwd[loc1] != char and passwd[loc2] == char
        )


def check_valid(min_rule: Dict[str, Any], max_rule: Dict[str, Any], passwd) -> bool:
    """
    Parameters
    ---------
    min_rule, max_rule:
        e.g. {"a": 4, "b": 6} "a" is allowed to appear max 4 and "b" max 6 times
    """
    # in the end min_rule must all <= 0 and max_rule must all >=0
    for char in passwd:
        if char in max_rule:
            max_rule[char] -= 1
        if char in min_rule:
            min_rule[char] -= 1
    
    for _, max_ in max_rule.items():
        if max_ < 0:
            return False

    for _, min_ in min_rule.items():
        if min_ > 0:
            return False

    return True


def build_rule_dicts(min_: int, max_: int, char: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    min_rule = {char: min_}
    max_rule = {char: max_}
    return min_rule, max_rule


def unpack_rule_passwd(line: str) -> Tuple[Dict[str, int], Dict[str, int], str]:
    _rule, passwd = line.split(": ")

    passwd = passwd.replace("\n", "")

    _min_max, char = _rule.split(" ")
    min_, max_ = _min_max.split("-")
    min_ = int(min_)
    max_ = int(max_)
    min_rule, max_rule = build_rule_dicts(min_, max_, char)

    return min_rule, max_rule, passwd


def unpack_rule_passwd_2(line: str) -> Tuple[int, int, str, str]:
    _rule, passwd = line.split(": ")

    passwd = passwd.replace("\n", "")

    _locs, char = _rule.split(" ")
    loc1, loc2 = _locs.split("-")
    loc1 = int(loc1) - 1
    loc2 = int(loc2) - 1

    return loc1, loc2, char, passwd


def valid_count(inputs: List[str]) -> int:
    count = 0
    for each_line in inputs:
        if check_valid(*unpack_rule_passwd(each_line)):
            count += 1
    return count


def valid_count_2(inputs: List[str]) -> int:
    count = 0
    for each_line in inputs:
        if check_valid_2(*unpack_rule_passwd_2(each_line)):
            count += 1
    return count


if __name__ == "__main__":
    test1 = "1-3 a: abcde"
    test2 = "1-3 b: cdefg"
    test3 = "2-9 c: ccccccccc"

    assert check_valid(*unpack_rule_passwd(test1))
    assert check_valid(*unpack_rule_passwd(test3))

    assert not check_valid(*unpack_rule_passwd(test2))

    all_ = read_lines_from_file("day2_A_input.txt")
    print(valid_count(all_))

    # part 2
    assert check_valid_2(*unpack_rule_passwd_2(test1))
    assert not check_valid_2(*unpack_rule_passwd_2(test2))
    assert not check_valid_2(*unpack_rule_passwd_2(test3))

    print(valid_count_2(all_))
