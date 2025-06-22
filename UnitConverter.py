print('''Tell me which unit you want convert by our our app can convert 
kilometer into miles, celsius into fahrenheit, 
meter into feet 
and use KM for kilomerter, C for celsius
M for meter''')

def convert(a):
    try:
        if len(a) > 0 and a.lower().startswith("km"):
            z = float(input("Enter value in kilometer: "))
            answer = z * 0.621371
            print(f"This is your answer {answer} miles")

        elif len(a) > 0 and a.lower().startswith("c"):
            z = float(input("Enter value in Celsius: "))
            answer = z * 9/5 + 32
            print(f"This is your answer {answer} in Fahrenheit")
        
        elif len(a) > 0 and a.lower().startswith("m"):
            z = float(input("Enter value in meter: "))
            answer = z * 3.28084
            print(f"This is your answer {answer} in feet")
    except Exception:
        print("write it correctly")

# calling the function with input
while True:
    user_input = input("What do you want: ")
    convert(user_input)

# you want to add exit so please add that in future
