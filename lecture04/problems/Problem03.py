def solution() -> None:
    try:
        _input_user = int(input("Enter int number : "))
        print(_input_user)
    except ValueError:
        print("Wrong input .")


if __name__ == '__main__':
    solution()
