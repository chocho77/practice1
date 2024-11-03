from strpkg.strmethods import StringMethods

def solution() -> None:
    txt = "hello, and welcome to my world."
    correct_txt = StringMethods.capitalize_method(txt)
    print(correct_txt)

def solution_one() -> None:
    txt = "Hello, And Welcome To My World!"
    correct_txt = StringMethods.casefold_method(txt)
    print(correct_txt)

def solution_two() -> None:
    txt = "banana"
    correct_txt = StringMethods.center_method(txt,20)
    print(correct_txt)

def solution_three() -> None:
    txt = "I love apples, apple are my favorite fruit"
    numbers = StringMethods.count_method(txt,"apple")
    print(f"Count {numbers}")

def solution_four() -> None:
    txt = "My name is Stale."
    x = StringMethods.encode_method(txt)
    print(x)

def solution_five() -> None:
    txt = "Hello, welcome to my world."
    x = StringMethods.endswith_method(txt,".")
    print(x)

def solution_six() -> None:
    txt = "H\te\tl\tl\to"
    x = StringMethods.expandtabs_method(txt,10)
    print(x)


if __name__ == '__main__':
    solution()
    solution_one()
    solution_two()
    solution_three()
    solution_four()
    solution_five()
    solution_six()


