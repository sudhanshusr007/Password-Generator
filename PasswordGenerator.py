import random
import string

# This function generates a random password based on user inputs
def generate_password(min_length, numbers=True, special_characters=True):
    # Define strings of letters, digits, and special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Concatenate the strings based on user inputs
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Initialize variables for criteria checking
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    # Generate new passwords until criteria is met
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # Check if generated password contains at least one number and one special character
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True

        if numbers and not has_number:
            meet_criteria = False
        if special_characters and not has_special:
            meet_criteria = False

        # Truncate the password to exactly min_length characters
        if len(pwd) == min_length and meet_criteria:
            break

    return pwd 

# Prompt the user to input password length and criteria
min_length = int(input("Enter the length of your password: "))
has_number = input("Do you want to include numbers (y/n)? : ").lower() == "y"
has_special = input("Do you want to include special characters (y/n)? : ").lower() == "y"

# Generate and print the password based on user inputs
pwd = generate_password(min_length, has_number, has_special)
print(pwd)