def solution() -> None:
    num = 23
    real_num = 3.7
    is_real = True
    name = "John"
    text = "{} {} {} {}".format(num, real_num, is_real, name)
    print(text)

def solution_one(num, real_num, is_real, name) -> str:
    text = "{} {} {} {}".format(num, real_num, is_real, name)
    return text


if __name__ == '__main__':
    solution()
    text = solution_one(24,2.3,False,"John")
    print(f"String : {text}")
    text = solution_one(45,56.56,True,"Viktor")
    print(f"String : {text}")

