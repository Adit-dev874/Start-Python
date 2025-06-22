# Secret_Code_Translator this will creat 

from code_ import code

def encode(text):
    result = ""
    for char in text:  # ✅ no parentheses needed
        result += code.get(char, char)
    return result

reverse_code = {v: k for k, v in code.items()}

def decode(secret):
    result = ""
    i = 0
    while i < len(secret):
        match_found = False
        # Try the longest possible key first
        for length in range(min(100, len(secret) - i), 0, -1):  # Try chunk sizes
            chunk = secret[i:i+length]
            if chunk in reverse_code:
                result += reverse_code[chunk]
                i += length
                match_found = True
                break
        if not match_found:
            result += secret[i]
            i += 1
    return result


while True:
    choice = input("\n1. Encode\n2. Decode\n0. Exit\nChoose an option: ")

    if choice == '1':
        text = input("Enter message to encode: ")
        print("Encoded:", encode(text))

    elif choice == '2':
        secret = input("Enter secret code to decode: ")
        print("Decoded:", decode(secret))

    elif choice == '0':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
