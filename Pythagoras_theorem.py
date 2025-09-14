'''
This code will calculate Pythagoras theorem example (not complex calculations for now)

Formula :- a^2 + b^2 = c^2
'''

def Calculate():
    
    while True:
        try:
            # input
            a = input("Enter a: ")
            b = input("Enter b: ")
            c = input("Enter c: ")

            if a == '?':
                b_int = int(b)  # this will convert str -> int
                c_int = int(c)  # this will convert str -> int

                if c_int <= b_int:  # some Pythagoras_theorem rules
                    print("Error: hypotenuse must be larger than the other sides!")

                else: # now it will do calculations
                    print(f'a^2 + {b}^2 = {c}^2')

                    b_square = b_int*b_int
                    c_square = c_int*c_int
                    
                    print(f'a^2 + {b_square} = {c_square}')

                    step2 = c_square - b_square

                    print(f'a^2 = {c_square} - {b_square}')  # minus
                    print(step2)

                    step3 = step2 ** 0.5  # this will calculate square root 
                    print(f'a = {step3}')

            if b == '?':
                a_int = int(a)  # this will convert str -> int
                c_int = int(c)  # this will convert str -> int

                if c_int <= a_int:  # some Pythagoras_theorem rules
                    print("Error: hypotenuse must be larger than the other sides!")

                else: # now it will do calculations
                    print(f'{a}^2 + b^2 = {c}^2')

                    a_square = a_int*a_int
                    c_square = c_int*c_int
                    
                    print(f'{a_square} + b^2 = {c_square}')

                    step2 = c_square - a_square

                    print(f'b^2 = {c_square} - {a_square}')  # minus
                    print(step2)

                    step3 = step2 ** 0.5  # this will calculate square root 
                    print(f'b = {step3}')
                    
            if c == '?':
                a_int = int(a)  # this will convert str -> int
                b_int = int(b)  # this will convert str -> int

                # now it will do calculations
                print(f'{a}^2 + {b}^2 = c^2')

                a_square = a_int*a_int
                b_square = b_int*b_int
                    
                print(f'{a_square} + {b_square} = c^2')

                step2 = a_square + b_square
                
                print(f'c^2 = {a_square} + {b_square}')  # plus
                print(step2)

                step3 = step2 ** 0.5  # this will calculate square root 
                print(f'c = {step3}')
            
        except Exception:
            print('Do it correctly')

        finally:
            end_or_no = input("Enter y to end and n to do next question: ").lower()

            if end_or_no == 'y':
                break

Calculate()
