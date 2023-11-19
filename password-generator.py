import random


def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_uppercase else ''
    numbers = '0123456789' if use_numbers else ''
    symbols = '!@#$%^&*()-_=' if use_symbols else ''
    
    # Combining all possible characters
    possible_characters = lowercase_letters + uppercase_letters + numbers + symbols

    # Generating the password
    password = ''.join(random.choice(possible_characters) for i in range(length))
    
    return password


# User interaction
def main():
    length = int(input("Password length: "))
    password = generate_password(length)
    print("Your new password is:", password)


if __name__ == "__main__":
    main()
