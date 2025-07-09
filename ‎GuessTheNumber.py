from random import randint

def GuessTheNumberLogic():
    number = randint(1, 100)
    while (guess := int(input("Guess a number (1-100): "))) != number:
        print("Too low!" if guess < number else "Too high!")
    print("You guessed it!")

GuessTheNumberLogic()