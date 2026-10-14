
import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    a = int(input("Guess the number (between 1 and 100): "))
    guesses += 1

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print(f"You guessed it right in {guesses} guesses!")

