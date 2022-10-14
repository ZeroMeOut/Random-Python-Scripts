name = input("Enter your name: ")
age = int(input("Enter your age: "))


def person(name, age):
    print("\nThis is " + name + "\n" + "You are " + str(age) + " years old.")
    if age > 20:
        print("Bruv you are old")
    return


person(name, age)
