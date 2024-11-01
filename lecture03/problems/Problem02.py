def solution() -> None:
    num = 1235.1234687
    print("%.3f" % num)
    print("%.2f" % num)
    print("{:.2f}".format(num))
    print(f"{num:.2f}")
    print(f"{num:.3f}")


if __name__ == '__main__':
    solution()
