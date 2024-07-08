# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 10

# Program Lab10A.py
mylist = []
selection = 0

def checkList(delete, mylist) :
    if delete in mylist :
        mylist.remove(delete)
        return True
    else :
        return False

print("[Mailing List]")

while selection != 4 :
    selection = int(input("\n1 - Add email\n"
                      "2 - Delete email\n"
                      "3 - List all emails\n"
                      "4 - Quit\n"
                      "Make your selection: "))

    if selection == 1 :
        new = input("\nEnter the email to be added: ")
        mylist.append(new)
        print("Email added to mailing list.")

    if selection == 2 :
        delete = input("\nEnter the email to be removed: ")
        if (checkList(delete, mylist) == True) :
            print(delete + " has been removed from the mailing list.")
        else :
            print("No such email in mailing list: " + delete)

    if selection == 3 :
        print(*mylist, sep = "\n")

    if selection == 4 :
        print("\nShutting down...")