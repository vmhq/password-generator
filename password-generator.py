'''Password Generator'''

import secrets
import os


def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Password Generator"""
    lowercase_letters = 'abcdefghijkmnopqrstuvwxyz'  # excluding 'l'
    uppercase_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # excluding 'I' and 'O'
    numbers = '23456789'  # excluding '0' and '1'
    symbols = '!@#$%^&*()-_='
    possible_characters = lowercase_letters
    if use_uppercase:
        possible_characters += uppercase_letters
    if use_numbers:
        possible_characters += numbers
    if use_symbols:
        possible_characters += symbols

    password = ''.join(secrets.choice(possible_characters)
                    for i in range(length))
    return password


def clean_screen():
    """Clean Screen"""
    os.system('clear') if os.name == 'posix' else os.system('cls')


def user_pass():
    """User Interaction"""
    while True:
        try:
            length = int(input("Password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            clean_screen()
            print("Please enter a positive integer.")

    use_uppercase = input(
        "Do you want to include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input(
        "Do you want to include numbers? (y/n): ").lower() == 'y'
    use_symbols = input(
        "Do you want to include symbols? (y/n): ").lower() == 'y'

    password = generate_password(
        length, use_uppercase, use_numbers, use_symbols)
    clean_screen()
    print("Your new password is:", password)


def main():
    """Main"""
    user_pass()


if __name__ == "__main__":
    main()
