def recExpoN(x, n):
    if n == 1:
        return x

    return x * recExpoN(x, n - 1)


def main():
    num = int(input("Please enter a non-negative integer: "))
    expo = int(input("Please enter a non-negative integer: "))

    s = recExpoN(num, expo)

    print(str(s))


if __name__ == "__main__":
    main()
