# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Assignment: 2
# Program: Assignment2A.py
# Write a Python program to calculate the discount on an online shopping order based on the customer's total purchase amount and their membership status.
print("[Discount Calculator]")
purchase_amount = float(input("Enter your total purchase amount: $"))
membership = input("Are you a member of the shopping club (Yes or No)? ")
discount = 0
if purchase_amount < 50:
    discount = 0
elif 50 <= purchase_amount <= 200:
    if membership == "yes":
        discount = 0.10 * purchase_amount
    else:
        discount = 0.05 * purchase_amount
else:
    if membership == "yes":
        discount = 0.15 * purchase_amount
    else:
        discount = 0.10 * purchase_amount
final_price = purchase_amount - discount
print("Your discount is:", "$" + str(final_price))
print("Your total price after discount is:", "$" + str(final_price))


