import json

with open('quiz.json') as f:  # this will load all questions form quiz.json
    quiz = json.load(f)

def quizs():

    guesses = 1

    for question in quiz:
        print(question['question'])
        print(question['options'])
        # this both will bring all question and options form file

        guess = input('Enter the answer you choose: ').upper()
        
        if guess == 'EXIT':
            return True
        
        else:
            if guess == question['answer']:
                print("You guessed right " + question['answer'] + " is this and you used guesses " + str(guesses))
            
            elif guess != question['answer']:
                print("Sorry answer is " + question['answer'] + "now you use " + str(guesses) + "guesses")

            guesses += 1

quizs()