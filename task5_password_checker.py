import re

# Ask user to enter password
password = input("Enter your password: ")

# Conditions
length_check = len(password) >= 8
number_check = re.search(r"[0-9]", password)
uppercase_check = re.search(r"[A-Z]", password)
special_char_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Check password strength
if length_check and number_check and uppercase_check and special_char_check:
    print("Strong Password")
else:
    print("Weak Password")
    print("Password must contain:")
    print("- Minimum 8 characters")
    print("- At least 1 number")
    print("- At least 1 uppercase letter")
    print("- At least 1 special character")