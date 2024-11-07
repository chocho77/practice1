def solution_one() -> None:
    filename = "hello.py"
    find_index = filename.find(".")
    name = filename[:find_index]
    print(name)

def solution_two() -> None:
    name = "$$$John Smith"
    print(name)
    correct_name = name.lstrip("$") # same result
    correct_name = name.strip() # same result
    correct_name = name[3:] # same result
    correct_name = name.replace("$", "")
    print(correct_name)


if __name__ == '__main__':
    solution_one()
    solution_two()

