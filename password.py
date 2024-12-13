import re

# Read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# Pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'  # At least 6 lowercase letters
password_pattern = r'^[A-Za-z0-9_]{8,}$'  # At least 8 characters: letters, numbers, underscore

# Check if username and password are ok
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# Print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Invalid username or password.")