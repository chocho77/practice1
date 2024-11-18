def solution() -> None:
    user_input = "+"
    try:
        int(user_input)
    except ValueError:
        print("Value error")


if __name__ == '__main__':
    solution()

