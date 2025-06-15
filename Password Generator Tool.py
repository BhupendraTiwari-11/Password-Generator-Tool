import random
import string

# ASCII art background for the app
print("""
=====================================
     PASSWORD GENERATOR TOOL
=====================================
""")

# Function to generate password
def generate_password(length, use_special, use_digits):
    # Define character sets
    characters = string.ascii_letters  # a-z, A-Z
    if use_special:
        characters += string.punctuation  # !@#$%^&*() etc.
    if use_digits:
        characters += string.digits  # 0-9
    
    # Ensure at least one of each selected type
    password = []
    if use_special:
        password.append(random.choice(string.punctuation))
    if use_digits:
        password.append(random.choice(string.digits))
    password.append(random.choice(string.ascii_letters))
    
    # Fill the rest of the password length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(characters))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

# Get user input with EOF handling
try:
    length_input = input("Enter password length (minimum 8): ") or "12"  # Default to 12 if EOF
    length = int(length_input)
    if length < 8:
        print("Password length must be at least 8 characters!")
        exit()
    
    special_input = input("Include special characters? (y/n): ") or "y"  # Default to 'y' if EOF
    if special_input.lower() not in ['y', 'n']:
        print("Respond only in y or n!")
        exit()
    use_special = special_input.lower() == 'y'
    
    digits_input = input("Include digits? (y/n): ") or "y"  # Default to 'y' if EOF
    if digits_input.lower() not in ['y', 'n']:
        print("Respond only in y or n!")
        exit()
    use_digits = digits_input.lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_special, use_digits)
    print(f"\nGenerated Password: {password}")
    
    # Option to save to file
    save_input = input("\nSave password to file? (y/n): ") or "n"  # Default to 'n' if EOF
    save_to_file = save_input.lower() == 'y'
    if save_to_file:
        with open("password.txt", "w") as f:
            f.write(password)
        print("Password saved to password.txt")
        print("Thanks for using this Password Generator Tool.")
    else:
        print("Thanks for using this Password Generator Tool.")
    
    print("\n=====================================")
except (ValueError, EOFError):
    print("Invalid input or EOF encountered! Using defaults: length=12, special chars=yes, digits=yes.")
    password = generate_password(12, True, True)
    print(f"\nGenerated Password: {password}")
    print("\n=====================================")
