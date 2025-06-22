from datetime import datetime

def AgeCalculator():
    birth_date_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

    today = datetime.now()

    age_years = today.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    print(f"You are {age_years} years old.")

AgeCalculator()