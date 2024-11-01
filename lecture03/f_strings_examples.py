def f_string_example_one() -> None:
    john = "John"
    sentence_one = f"Hello, {john}"
    print(sentence_one)


def f_string_example_two() -> None:
    john = "John"
    smith = "Smith"
    sentence_two = f"Hello, {john} {smith}"
    print(sentence_two)


def f_string_example_three() -> None:
    banana = "Banana"
    sentence_three = f"{banana}"
    print(sentence_three)


if __name__ == '__main__':
    f_string_example_one()
    f_string_example_two()
    f_string_example_three()
