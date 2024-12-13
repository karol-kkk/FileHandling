# emails.py
import re

def email_sender(email_content):
    """Extract the sender's email address."""
    from_pattern = r"From:.*<(.+?)>"
    sender = re.search(from_pattern, email_content)
    return sender.group(1) if sender else "Sender not found"

def email_recipient(email_content):
    """Extract the recipient's email address."""
    to_pattern = r"To:.*<(.+?)>"
    recipient = re.search(to_pattern, email_content)
    return recipient.group(1) if recipient else "Recipient not found"

def email_subject(email_content):
    """Extract the subject of the email."""
    subject_pattern = r"Subject: (.+)"
    subject = re.search(subject_pattern, email_content)
    return subject.group(1) if subject else "Subject not found"

def email_body(email_content):
    """Extract the body of the email."""
    body_pattern = r"Content-Transfer-Encoding:.*\n\n([\s\S]+)"
    body = re.search(body_pattern, email_content)
    return body.group(1).strip() if body else "Body not found"
