"""
In this project, I will solve quadratic equations using the quadratic formula method.

Quadratic formula:
    x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a)
"""

import cmath   # cmath is used so complex roots also work


def formula(a, b, c):
    # Convert "?" to defaults
    if a == "?":
        print("This is not a quadratic equation (a cannot be missing).")
        return

    # Convert values to numbers or defaults
    a = int(a)
    b = 0 if b == "?" else int(b)
    c = 0 if c == "?" else int(c)

    # Step 1
    print(f"step 1 =\n    a = {a}, b = {b}, c = {c}")

    # Step 2 (discriminant)
    print(f"step 2 =\n    D = b**2 - 4*a*c = {b}^2 - 4*{a}*{c}")
    D = b**2 - 4*a*c
    print(f"D = {D}")

    # Step 3 (quadratic formula)
    print("formula =\n    x = (-b ± (b**2 - 4*a*c)**0.5) / (2*a)")
    print(f"step 3 =\n    x = (-{b} ± ({D}) ** 0.5) / (2*{a})")

    # Use cmath for both real and complex roots
    Dsquare = cmath.sqrt(D)
    denominator = 2 * a

    print(f"x = (-{b} + {Dsquare:.2f}) / {denominator} or x = (-{b} - {Dsquare:.2f}) / {denominator}")

    # Numerators
    numerator1 = -b + Dsquare
    numerator2 = -b - Dsquare

    print(f"x = {numerator1:.2f} / {denominator} or x = {numerator2:.2f} / {denominator}")

    # Final results
    result1 = numerator1 / denominator
    result2 = numerator2 / denominator
    print(f"Final roots: x = {result1:.2f} or x = {result2:.2f}")


# Loop for repeated solving
while True:
    try:
        a = input("Enter value of a (or ?): ").strip()
        b = input("Enter value of b (or ?): ").strip()
        c = input("Enter value of c (or ?): ").strip()

        formula(a, b, c)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        yes_or_no = input("Press y to continue or n to exit: ").lower()
        if yes_or_no == 'n':
            break
