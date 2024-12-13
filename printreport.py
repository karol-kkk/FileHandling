import re

# File name with shopping report
email_file = 'report.txt'

# Read the content of the email with proper encoding
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# Regular expression pattern to match amounts (e.g., \u20ac is the Unicode for the Euro sign)
pattern = r'\u20ac(\d+)'  # Matches numbers preceded by the Euro symbol

# Extract numbers from the email
amounts = re.findall(pattern, email)

# Convert extracted amounts to integers and calculate the total
total_spent = sum(int(amount) for amount in amounts)

# Print result
print(f"Total money spent: €{total_spent}")
