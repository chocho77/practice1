def solution() -> None:
    school = "Vasil Drumev"
    print(school)

def solution_one() -> None:
    country = "usa"
    correct_country = country.upper()
    print(correct_country)

def solution_two() -> None:
    country = "USA"
    correct_country = country.lower()
    print(correct_country)

def solution_three() -> None:
    filename = "hello.py"
    print(filename.endswith(".java"))
    print(filename.index("py"))
    print(filename.find("py"))
    print(filename.startswith("word"))


if __name__ == '__main__':
    solution()
    solution_one()
    solution_two()
    solution_three()


