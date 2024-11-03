def solution() -> None:
    txt = "Hello World"
    result = txt.split("o") # split string by symbol "o"
    print(result)
    print(txt.startswith("H"))
    print(txt.endswith("d"))
    print(txt.endswith("@"))


if __name__ == '__main__':
    solution()



