# main.py
import emails

# Read the raw email content from the file
with open("email.txt", "r") as file:
    email_content = file.read()

# Extract and print the required information
sender = emails.email_sender(email_content)
recipient = emails.email_recipient(email_content)
subject = emails.email_subject(email_content)
body = emails.email_body(email_content)

# Print the extracted values
print(f"Sender: {sender}")
print(f"Recipient: {recipient}")
print(f"Subject: {subject}")
print(f"Body: \n{body}")
