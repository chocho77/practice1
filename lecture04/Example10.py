def solution() -> None:
    number = int(input("Enter int number : "))
    if number >= 10:
        print("Great. Number greater than 10.")
    else:
        print("Bad. Number less than 10.")


if __name__ == '__main__':
    continue_str = 'y'
    while continue_str == 'y' :
        solution()
        continue_str = input("Continue? y/n")
    print("Goodbye. Have a nice day.")





