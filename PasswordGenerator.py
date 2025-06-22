# main.py
import pas

def PasswordGenerator():
    password = pas.generate_password(12)
    print("Your password:", password)

PasswordGenerator()