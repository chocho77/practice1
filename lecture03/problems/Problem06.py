def solution_one() -> None:
    name = "john smith"
    print(name)
    name = name.title()
    print(name)
    text = "Hello, there !!!"
    text = text.replace("!", ".")
    print(text)
    print(text.find(","))
    comma_index = text.find(",")
    print(text[comma_index+1:])
    #print(help(text.find(","))) # print help for find method
    print(text.find("@"))
    if text.find("@") == -1:
        print("The symbol @ is not find in the text.")
    pass


if __name__ == '__main__':
    solution_one()