# Class: CSE 1321L
# Section: 52 python
# Term: Spring
# Instructor: Roshni Satish
# Name: Nathaniel Neal
# Lab: 8
# Program Lab8A.py
# You might have been enrolled into a mailing list at some point in your life. While some mailing lists are very helpful with the emails they send, some are simply used to send ads or spam. We’ll code a very simple mailing list which allows the adding or removal of emails to it.

mylist = []
print("[Mailing List]")
while choice != 4:
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    choice = int(input("Make your selection:"))
    if choice == 1:
        added_email = input("Enter the email to be added:")
        mylist.append(added_email)
        print("Email added to mailing list.")
    if choice == 2:
        remove_email = input("Enter the email to be removed:")
        mylist.remove(remove_email)
        print(remove_email, " has been removed from the mailing list.")
    else:
        print("No such email in mailing list:", remove_email)
    if choice == 3:
        for i in mylist:
            print(i)
    if choice == 4:
        print("Shutting down...")
        break








