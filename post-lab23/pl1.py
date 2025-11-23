import re

def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, pan))

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


pan_number = input("Enter PAN card number: ")
email_id = input("Enter email ID: ")

print("\nValidation Results:\n")

if validate_pan(pan_number):
    print("Valid PAN card number.")
else:
    print("Invalid PAN card number.")

if validate_email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
