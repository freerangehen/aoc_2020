from typing import List, Dict
from functools import partial
import re

from tools import read_text_from_file


def bounded_4digit(input: str, upper: int, lower: int) -> bool:
    if len(input) != 4:
        return False

    if int(input) < lower or int(input) > upper:
        return False

    return True


def hgt(input: str) -> bool:
    if "cm" in input:
        _input = int(input.replace("cm", ""))
        return _input >= 150 and _input <= 193
    elif "in" in input:
        _input = int(input.replace("in", ""))
        return _input >= 59 and _input <= 76

    return False


def hcl(input:str) -> bool:
    pattern = re.compile("^#[a-f0-9]{6}$")
    if re.search(pattern, input):
        return True

    return False


def ecl(input: str) -> bool:
    return input in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def pid(input: str) -> bool:

    pattern = re.compile("^[0-9]{9}$")
    if re.search(pattern, input):
        return True

    return False


REQUIRED = {
        "byr": partial(bounded_4digit, upper=2002, lower=1920),
        "iyr": partial(bounded_4digit, upper=2020, lower=2010),
        "eyr": partial(bounded_4digit, upper=2030, lower=2020),
        "hgt": hgt,
        "hcl": hcl,
        "ecl": ecl,
        "pid": pid,
#    "cid"
}


def count_valid_passports(passports: List[Dict[str, str]]) -> int:
    valid = 0
    for pp in passports:
        if is_valid_passport(pp):
            valid += 1

    return valid


def count_valid_passports2(passports: List[Dict[str, str]]) -> int:
    valid = 0
    for pp in passports:
        if is_valid_passport2(pp):
            valid += 1

    return valid

def is_valid_passport(passport: Dict[str, str]) -> bool:
    for field in REQUIRED:
        if field not in passport:
            return False
    return True


def is_valid_passport2(passport: Dict[str, str]) -> bool:
    for field in REQUIRED:
        if field not in passport:
            return False
        else:
            if REQUIRED[field](passport[field]) is False:
                return False
    return True


def read_passports_from_text(input: str) -> List[Dict]:
    all_passports = input.split("\n\n")
    passports_descriptors = []
    for passport in all_passports:
        _pp_dict = {}
        _passport = passport.replace("\n", " ")
        _passport = re.sub(" +", " ", _passport)
        _passport = _passport.split(" ")
        for item in _passport:
            if ":" in item:
                key, val = item.split(":")
                _pp_dict.update({key: val})
        passports_descriptors.append(_pp_dict)
    return passports_descriptors


if __name__ == "__main__":
    test1 = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm

    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """

    assert count_valid_passports(read_passports_from_text(test1)) == 2

    input_data = read_text_from_file("day4_A_input.txt")
    print(count_valid_passports(read_passports_from_text(input_data)))

    print(count_valid_passports2(read_passports_from_text(input_data)))
