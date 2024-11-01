def solution() -> None:
    first_name = "first name"
    middle_name = "middle name"
    last_name = "last name"
    full_name = f"{first_name} {middle_name} {last_name}"
    print(full_name)


def print_sentence() -> None:
    full_name = "Chavdar Momchilov"
    sentence = "My full name is {}".format(full_name)
    print(sentence)
    first_name = "Kalojan"
    last_name = 'Georgiev'
    full_name = "{} {}".format(first_name, last_name)
    print(full_name)


if __name__ == '__main__':
    print_sentence()
    solution()

