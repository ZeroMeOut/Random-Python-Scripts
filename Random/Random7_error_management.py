# Infinite loop
while True:

    try:
        number = int(input("Enter a number: "))
        print(number)
        break  # Exit the immediate loop
    except ValueError:
        #  Response to program crashing
        print("Invalid Input -TRY AGAIN")
    #  Check the while condition if true repeat
