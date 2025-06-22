from random import randint

print("Write 'Roll' to start")

def DiceRoller():
    user_input = input(">>> ")
    if user_input.lower() == "roll":
        while True:
            roll = randint(1, 6)
            print("You rolled:", roll)

            again = input("Roll again? (y/n): ").lower()
            if again != "y":
                print("Thanks for playing!")
                break
    else:
        print("Please write 'Roll' to start.")
        

DiceRoller()