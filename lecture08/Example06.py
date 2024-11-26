# sort list
def sol_one() -> None:
    l = [5, 4, 3, 2, 1]
    print(sum(l), max(l), min(l), sorted(l), type(sorted(l)))

def sol_two() -> None:
    l = [1, 4, 3, 5, 2]
    print(l)
    l.sort()
    print(l)

def sol_three() -> None:
    l = [2, 6, 3, 1]
    print(l)
    print(id(l))
    sort_l = sorted(l)
    print(sort_l)
    print(id(sort_l))

def sol_four() -> None:
    l = [2, 6, 3, 1]
    print(l)
    print(id(l))
    l.sort()
    print(l)
    print(id(l))


if __name__ == '__main__':
    sol_one()
    print("---")
    sol_two()
    print("---")
    sol_three()
    print("---")
    sol_four()


