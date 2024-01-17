import secrets
import string

def generate_password(length=12, include_numbers=True, include_symbols=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter password length: "))
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, include_numbers, include_symbols

if __name__ == "__main__":
    print("=== Password Generator ===")
    length, include_numbers, include_symbols = get_user_input()
    password = generate_password(length, include_numbers, include_symbols)
    print("\nGenerated Password:", password)
