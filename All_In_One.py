from GuessTheNumberLogic import GuessTheNumberLogic
from DiceRoller import DiceRoller
from PasswordGenerator import PasswordGenerator
from AgeCalculator import AgeCalculator

def All_in_ONE():
    print("""
Welcome to the All-in-ONE Tool!

Choose one of the following:
- number game
- dice roller
- password generator
- age calculator
- exit
""")

    while True:
        choice = input("What do you want to do: ").strip().lower()

        if choice == "number game":
            game = GuessTheNumberLogic()
            game.play()
        elif choice == "dice roller":
            dice = DiceRoller()
            dice.roll()
        elif choice == "password generator":
            generator = PasswordGenerator()
            generator.generate()
        elif choice == "age calculator":
            calc = AgeCalculator()
            calc.calculate()
        elif choice == "exit":
            print("Thanks for using All-in-ONE. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

All_in_ONE()

