# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Lab: 4
# Program Lab4C.py
# In this lab, you are going to create a program that prompts the user for the three sides of a triangle and then determines what type of triangle the user has.

first_side = int(input("Enter the first side of the triangle: "))
second_side = int(input("Enter the second side of the triangle: "))
third_side = int(input("Enter the third side of the triangle: "))

if first_side > 0 and second_side > 0 and third_side > 0:
    if first_side + second_side > third_side and second_side + third_side > first_side and third_side + first_side > second_side:
        if first_side == second_side == third_side:
            print("The triangle is an equilateral triangle.")
        elif first_side == second_side or second_side == third_side  or third_side == first_side:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")
    else: print("The sides do not form a valid triangle.")
else:
    print("Invalid input. All sides must be greater than 0.")

