def solution() -> None:
    user_input = input("Enter your input : ")
    user_choice = 0
    if user_input.lower() == "true":
        user_choice = 1
    else:
        user_choice = 0
    print(bool(user_choice))


if __name__ == '__main__':
    solution()


