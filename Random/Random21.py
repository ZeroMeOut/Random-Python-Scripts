def recStrN(x):
    if x == "":
        return 0

    return 1 + recStrN(x[:-1])


def main():
    string = input("Please enter a string: ")

    s = recStrN(string)

    print(s)


if __name__ == "__main__":
    main()
