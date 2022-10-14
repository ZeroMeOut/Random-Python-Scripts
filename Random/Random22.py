def count(x):
    if x == "":
        return 0
    return 1 + count(x[:-1])


def swap(x):
    lenStr = count(x)
    if lenStr == 0:
        return " "
    return x[1] + x[0] + swap(x[2:])


def main():
    string = input("Please enter a string: ")
    s = swap(string)
    print(s)


if __name__ == "__main__":
    main()
