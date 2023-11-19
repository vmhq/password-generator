'''Password Generator'''

import secrets


def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
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

    password = ''.join(secrets.choice(possible_characters) for i in range(length))
    return password


def user_pass():
    while True:
        try:
            length = int(input("Password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    use_uppercase = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("Your new password is:", password)


def main():
    user_pass()

if __name__ == "__main__":
    main()
