phrase = input("Enter sentence: ")


def translate(phrase):
    translation = ""
    for letter in phrase:  # Breaks the phrase into letters
        if letter.lower() in "aeiou":  # Converts the vowels into g
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter  # Prints letter if it is not vowel
    return translation


print(translate(phrase))
