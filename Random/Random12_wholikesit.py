def likes(names):
    # your code here

    textToReturn = ""

    if len(names) == 0:
        textToReturn = "no one likes this"
    elif len(names) == 1:
        textToReturn = str(names[0]) + " likes this"
    elif 1 < len(names) < 4:
        for name in range(0, len(names) - 1):  # For names[0],names[1] and names[2]
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            textToReturn = textToReturn + names[name] + ", "
        textToReturn = textToReturn[:-2]
        textToReturn = textToReturn + " and " + str(len(names) - 2) + " others like this"
    return textToReturn


print(likes(["David", "John", "Peter"]))
