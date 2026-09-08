# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Lab: 9
# Program Lab9B.py
# Build a program that authenticates the user login by asking the user for a username and a password.
def register():
    print("[Register]")
    username = input("Username: ")
    password = input("Password: ")
    users[username] = password
    print("User successfully added!")


def login():
    print("[Login]")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print("Success!")
        user_menu(username)
    else:
        print("Incorrect username/password!")


def user_menu(username):
    while True:
        print("Choose an option")
        print("3 - Change Password")
        print("4 - Logout")
        print("E - Exit")
        option = input()

        if option == "3":
            print("[Changing password]")
            new_password = input("Password: ")
            users[username] = new_password
        elif option == "4":
            print("Logging Out...")
            break
        elif option.upper() == "E":
            print("Terminating...")
            exit()
while True:
    print("Choose an option")
    print("1 - Login")
    print("2 - Register")
    print("E - Exit")
    option = input()

    if option == "1":
        login()
    elif option == "2":
        register()
    elif option.upper() == "E":
        print("Terminating...")
        break
