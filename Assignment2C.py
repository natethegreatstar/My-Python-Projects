# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Assignment: 2
# Program: Assignment2C.py
# Your task is to develop a text-based Role-Playing Game (RPG) in Python. The game will allow the player to choose a character class and perform specific actions based on their selection. The program must provide clear instructions, handle input effectively, and display appropriate responses for valid and invalid choices. To complete this assignment, you must use the match statement for decision-making.
print("Welcome to the RPG Game!")
character_class = input("Choose your class (Warrior, Mage, Healer): ")
match character_class:
    case "warrior":
        print("You have chosen Warrior! You are strong and brave.")
        print("Choose your action: \n1. Attack with your sword\n2. Defend with your shield")
        action = input("Enter your choice (1 or 2): ")
        match action:
            case "1":
                print("You swing your sword and defeat the enemy!")
            case "2":
                print("You raise your shield and block the enemy's attack!")
            case _:
                print("Invalid action choice.")

    case "mage":
        print("You have chosen Mage! You wield powerful magic.")
        print("Choose your action: \n1. Cast a fireball\n2. Cast a healing spell")
        action = input("Enter your choice (1 or 2): ")
        match action:
            case "1":
                print("You cast a fireball and scorch the enemy!")
            case "2":
                print("You cast a healing spell and restore your energy.")
            case _:
                print("Invalid action choice.")

    case "healer":
        print("You have chosen Healer! You are kind and supportive.")
        print("Choose your action: \n1. Heal your ally\n2. Attack with your staff")
        action = input("Enter your choice (1 or 2): ")
        match action:
            case "1":
                print("You heal your ally and boost their morale!")
            case "2":
                print("You swing your staff and knock out the enemy!")
            case _:
                print("Invalid action choice.")

    case _:
        print("Invalid class choice. The game ends.")

print("Thank you for playing!")
