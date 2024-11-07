def solution() -> None:
    #ternary operator
    x = 3
    text = "X is even" if x % 2 == 0 else "X is odd"
    print(text)

def solution_one() -> int:
    _a = 3
    _b = 2
    if _a > _b:
        _m = _a
        return _m
    else:
        _m = _b
        return _m

def solution_two() -> int:
    _a = 3
    _b = 2
    _m = _a if _a > _b else _b
    return _m


if __name__ == '__main__':
    solution()
    res = solution_one()
    print(res)
    res = solution_two()
    print(res)



