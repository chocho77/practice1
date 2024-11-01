name = "Chavdar Ventsislavov Momchilov"

def solution_one() -> str:
    _str_one = name[:7]
    return _str_one


def solution_two() -> str:
    _str_one = name[8:20]
    return _str_one

def main_solution() -> str:
    _str_one = solution_one()
    _str_two = solution_two()
    _str_three = f"{_str_one} {_str_two}"
    return _str_three

def test_solution() -> str:
    return name[:90]


if __name__ == '__main__':
    str_demo = main_solution()
    print(len(str_demo))
    print(str_demo)
    test = test_solution()
    print(len(test))
    print(test)



