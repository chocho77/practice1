def solution() -> None:
    raining = False
    print("Let's go to the ", 'beach' if not raining else 'library')
    raining = True
    print("Let's go to the ", 'beach' if not raining else 'library')

def solution_one() -> None:
    age = 12
    s = 'minor' if age < 21 else 'adult'
    print(s)
    age = 22
    s = 'minor' if age < 21 else 'adult'
    print(s)


if __name__ == '__main__':
    solution()
    solution_one()
