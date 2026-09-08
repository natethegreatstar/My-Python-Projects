# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Assignment: 2
# Program: Assignment2B.py
# Write a Python program that accepts three inputs from the user:o Age (integer)o Income (integer)o Credit Score (integer between 300 and 850)Based on the inputs, determine whether the user qualifies for a loan and what type of loan they qualify for. Use nested if-elif-else statements and the program must use a match statement to classify the person's credit score into categories.
print("[Loan Qualification Checker]")
age = int(input("Enter your age: "))
income = int(input("Enter your annual income: $"))
credit_score = int(input("Enter your credit score (300-850): "))
if credit_score < 300 or credit_score > 850:
    print("Invalid credit score. It must be between 300 and 850.")
else:
    
    if age < 18:
        print("You do not qualify for a loan due to age.")
    else:

        match credit_score:
            case score if 700 <= score <= 850:
                credit_category = "Good"
            case score if 600 <= score <= 699:
                credit_category = "Fair"
            case score if 300 <= score <= 599:
                credit_category = "Poor"


        if credit_category == "Poor":
            print("You do not qualify for a loan due to poor credit.")
        else:
            if income >= 100000 and credit_category == "Good":
                print("You qualify for a Premium Loan.")
            elif 50000 <= income < 100000 and (credit_category == "Good" or credit_category == "Fair"):
                print("You qualify for a Standard Loan.")
            elif income < 50000 and credit_category == "Fair":
                print("You qualify for a Basic Loan.")
            else:
                print("Your income is too low for a loan.")
