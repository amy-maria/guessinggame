import sys

from random import randint

# generate number 1-10
random_number = randint(1, 10)
print(random_number)


# input from user

while True:
    try:
        guess = int(input("Guess a number 1-10:  "))
        # check input is a number
        # check if number is correct guess or guess again
        if int(guess) > 0 and int(guess) < 11:
            if guess == random_number:
                print("You're a genius! You guessed correctly")
                break
        else:
            print("Number out of Range. Enter a number between 1-10.")
            continue
    except ValueError:
        print("Please enter a number")
        continue
