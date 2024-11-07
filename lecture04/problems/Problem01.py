def solution() -> None:
    width = 60
    print(width * '*')
    print("Text".center(width))
    print("Text".rjust(width + 2 - (width//2)))


if __name__ == '__main__':
    solution()

