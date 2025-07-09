import json
import random

with open('quiz.json') as f:  # this will load all questions form quiz.json
    quiz = json.load(f)

def quizs():
    try:

        guesses = 1
        points = 0

        random.shuffle(quiz)  # this will randomize the question order

        for question in quiz:
            print(question['question'])
            print(question['options'])
            # this both will bring all question and options form file

            guess = input('Enter the answer you choose: ').upper()
            
            if guess == 'EXIT':
                print(f'Your guesses {guesses}')
                print(f'Your points {points}')
                return True
            
            else:
                if guess == question['answer']:
                    points += 1
                    print("You guessed right " + question['answer'] + " is this and you used guesses " + str(guesses) + "\n Your points " + str(points))
                
                elif guess != question['answer']:
                    print("Sorry answer is " + question['answer'] + " now you use " + str(guesses) + " guesses" + "\n Your points " + str(points))

                guesses += 1
    
    except ValueError as v:
        print(f'Give valid value {v}')

quizs()