'''I am writing this code because I created everything else, but not this.'''

def Calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator between +, -, *, /: ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                print(num1 + num2)
            elif operator == '-':
                print(num1 - num2)
            elif operator == '*':
                print(num1 * num2)
            elif operator == '/':
                if num2 == 0:
                    print("Our code cannot divide by zero")    
                else:
                    print(num1 / num2)
            elif operator == 'exit':
                print("Thanks for using")
                break
        except ValueError as v:
            print(v)
        except Exception as e:
            print(e)

Calculator()
