def recFacN(n):
    if n != 0:
        if n == 1:
            return n

        return n * recFacN(n - 1)
    return 1


def main():
    num = int(input("Please enter a non-negative integer: "))

    s = recFacN(num)

    print(str(s))


if __name__ == "__main__":
    main()
