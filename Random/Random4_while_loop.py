secret_word = "giraffe"
secret_word2 = "Giraffe"
guess = ""

while guess != secret_word and guess != secret_word2:
    guess = input("Enter guess: ")

print("You win!")
