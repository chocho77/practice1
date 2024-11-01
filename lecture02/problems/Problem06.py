from math import sqrt


def pitagor_theorem() -> None:
    a = float(input("a = "))
    b = float(input("b = "))
    c = sqrt(a ** 2 + b ** 2)
    print(f"c = {c}")

def print_hi(name: str) -> None:
    print(f'Hi, {name}!')

def print_some_data() -> None:
    name = "ivan"
    num = 6
    real_num = 6.7
    print("String:", name)
    print("Integer:", num)
    print("Float:", real_num)
    pass

if __name__ == '__main__':
    print_hi("Chavdar")
    print_some_data()
    pitagor_theorem()


