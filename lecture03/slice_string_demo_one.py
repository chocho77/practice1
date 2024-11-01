def slice_string_demo_one() -> None:
    name = "Chavdar Vensislavov Momchilov"
    print(name)
    print(name[0:7])
    print(name[7:19])
    print(name[19:29])
    first_name = name[0:6]
    middle_name = name[7:18]
    last_name = name[19:29]
    print(len(name))
    full_name = f"{first_name} {middle_name} {last_name}"
    print(len(full_name))


if __name__ == '__main__':
    slice_string_demo_one()
