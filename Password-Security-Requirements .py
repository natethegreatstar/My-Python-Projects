# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Assignment: 4
# Program: Assignment4B.py
# Write a Python program that checks whether a password meets security requirements.

def check_length(password):
    return len(password) >= 8

def check_upper_lower(password):
    return any(c.islower() for c in password) and any(c.isupper() for c in password)

def check_special_character(password):
    return any(c in "!@#" for c in password)
while True:
    password = input("Enter a password: ")
    errors = []

    if not check_length(password):
        errors.append("Must be at least 8 characters long.")
    if not check_upper_lower(password):
        errors.append("Must contain both uppercase and lowercase letters.")
    if not check_special_character(password):
        errors.append("Must include at least one special character (!, @, #).")

    if errors:
        print("Password does not meet the requirements:")
        for error in errors:
            print(error)
    else:
        print("Password is strong!")
        break
