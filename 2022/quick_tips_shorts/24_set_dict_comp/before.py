def main():
    my_set: set[int] = {i * i for i in range(10)}
    print(my_set)

    # create a dictionary of numbers
    my_dict: dict[int, int] = dict()
    for i in range(10):
        my_dict[i] = i * i
    print(my_dict)


if __name__ == "__main__":
    main()
