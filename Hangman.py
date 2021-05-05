# Importing the Random Module
import random

numbers = "1234567890"
spc_chr = '''-_=+`~!@#$%^&*(){}[]''"";:,./?><'''


# The Start
print("Hi Welcome To the Terminal Hangman!!")
print("Guess The Word!!")
print("Let's Begin!")
print(" ")

allowed_errors = 7

guesses = []
done = False
has_broken = False




# Opening and reading a txt file
with open("Word.Txt") as f:
    words = f.readlines()

# Getting a random word from the txt file using the random module
word = random.choice(words)[:-1]


# The game
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors = {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())


    if guess.lower() not in word.lower():
        allowed_errors -= 1

    if guess == " ":
        print("You can't type spaces here!!")

    if guess == "":
        print("You can't leave it blank, Type a letter!!")
        allowed_errors -= 1

    if len(guess.lower()) > 1:
        allowed_errors -= len(guess.lower()) - 1
        print(f"You typed more than 1 letter!!, You typed {len(guess)} letters, Therefore we are counting it as {len(guess)} Errors :-)")

    if guess in numbers and not guess == "":
        print("You can't enter numbers here!!")


    if guess not in numbers:
        if guess in spc_chr:
            print("You can't type special characters here!!")

    if allowed_errors <= 0:
        break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False


# The end
if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over! The word was {word}!")
