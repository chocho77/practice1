def str_index_one() -> None:
    name = "chavdar"
    index_one = name[0]
    index_two = name[-1]
    index_minus_two = name[-2]
    print(index_one)
    print(index_two)
    print(index_minus_two)
    print(name.__len__())
    print(len(name))



if __name__ == '__main__':
    str_index_one()
