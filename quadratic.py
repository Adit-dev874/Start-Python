'''
In this project, I will solve quadratic equations using the quadratic formula method.

Quadratic formula:
    x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a)
'''

while True:
    try:

        def formula(a, b, c):
            # Variables a, b, c can be numbers or '?' (unknown).
            a = a
            b = b
            c = c

            # Case 1: If 'a' is missing, it's not a quadratic equation.
            if a == '?':
                print('This is not a quadratic equation (a cannot be missing).')

            # Case 2: If 'b' is missing, assume b = 0
            elif b == '?':
                inta = int(a)
                intb = 0  # b is assumed to be 0

                # Sub-case: If c is also missing, assume c = 0
                if c == '?':
                    intc = 0
                    
                    # Step 1
                    print(f'''step 1 =
                            a = {inta}, b = {intb}, c = {intc}''')

                    # Step 2
                    print(f'''step 2 =
                            D = b**2 - 4*a*c = {intb}^2 - 4*{inta}*{intc}''')

                    # Calculate discriminant
                    D = intb**2 - 4*inta*intc
                    print(f'D = {D}')

                    # Step 3: Apply quadratic formula
                    print('''formula =
                            x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a) ''')

                    print(f'''step 3 =
                            x = (-{intb} ± ({D}) ** 0.5) / 2*{inta}''')

                    # Simplify square root and denominator
                    Dsquare = D ** 0.5
                    denominator = 2 * inta

                    print(f' x = (-{intb} + {Dsquare}) / {denominator} or x = (-{intb} - {Dsquare}) / {denominator}')

                    # Numerators
                    bn = -intb
                    numerator1 = bn + Dsquare
                    numerator2 = bn - Dsquare

                    print(f'x = {numerator1} / {denominator} or x = {numerator2} / {denominator}')

                    # Final result
                    result = numerator1 / denominator
                    print(f'x = {result} (both roots are the same: 0)')

                # Sub-case: If only c is provided
                else:
                    intc = int(c)

                    # Step 1
                    print(f'''step 1 =
                            a = {inta}, b = {intb}, c = {intc}''')

                    # Step 2
                    print(f'''step 2 =
                            D = b**2 - 4*a*c = {intb}^2 - 4*{inta}*{intc}''')

                    # Calculate discriminant
                    D = intb**2 - 4*inta*intc
                    print(f'D = {D}')

                    # Step 3: Apply quadratic formula
                    print('''formula =
                            x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a) ''')

                    print(f'''step 3 =
                            x = (-{intb} ± ({D}) ** 0.5) / 2*{inta}''')

                    # Simplify square root and denominator
                    Dsquare = D ** 0.5
                    denominator = 2 * inta

                    print(f' x = (-{intb} + {Dsquare}) / {denominator} or x = (-{intb} - {Dsquare}) / {denominator}')

                    # Numerators
                    bn = -intb
                    numerator1 = bn + Dsquare
                    numerator2 = bn - Dsquare

                    print(f'x = {numerator1} / {denominator} or x = {numerator2} / {denominator}')

                    # Final results
                    result1 = numerator1 / denominator
                    result2 = numerator2 / denominator
                    print(f'x = {result1} or x = {result2}')

            # Case 3: If 'c' is missing, assume c = 0
            elif c == '?':
                inta = int(a)
                intb = int(b)
                intc = 0

                # Step 1
                print(f'''step 1 =
                            a = {inta}, b = {intb}, c = {intc}''')

                # Step 2
                print(f'''step 2 =
                            D = b**2 - 4*a*c = {intb}^2 - 4*{inta}*{intc}''')

                # Calculate discriminant
                D = intb**2 - 4*inta*intc
                print(f'D = {D}')

                # Step 3: Apply quadratic formula
                print('''formula =
                            x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a) ''')

                print(f'''step 3 =
                            x = (-{intb} ± ({D}) ** 0.5) / 2*{inta}''')

                # Simplify square root and denominator
                Dsquare = D ** 0.5
                denominator = 2 * inta

                print(f' x = (-{intb} + {Dsquare}) / {denominator} or x = (-{intb} - {Dsquare}) / {denominator}')

                # Numerators
                bn = -intb
                numerator1 = bn + Dsquare
                numerator2 = bn - Dsquare

                print(f'x = {numerator1} / {denominator} or x = {numerator2} / {denominator}')

                # Final results
                result1 = numerator1 / denominator
                result2 = numerator2 / denominator
                print(f'x = {result1} or x = {result2}')

    except Exception as e:
        print(e)

    finally:
        yes_or_no = input("Press y to continue or n to exit: ").lower()
        if yes_or_no == 'n':
            break

# Example run
formula(3, 5, '?')
