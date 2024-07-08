# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 4

# Program Lab4C.py
print("Welcome!")
balance = 1000
menu = "Y"
print("You have $" + str(balance), "in your account.")

while (menu == "Y" or menu == "y") :
    selection = int(input("\nMenu\n"
                      "0 – Make a deposit\n"
                      "1 – Make a withdrawal\n"
                      "2 – Display account value\n\n"
                      "Please make a selection: "))

    match selection :
        case 0 :
            deposit = float(input("How much would you like to deposit?: "))
            balance = balance + deposit
            print("Your current balance is $" + str(balance))
            menu = input("Would you like to return to the main menu (Y/N)?: ")
        case 1 :
            withdrawn = float(input("How much would you like to withdraw?: "))
            if (withdrawn <= balance) :
                pass
                balance = balance - withdrawn
                print("Your current balance is $" + str(balance))
                menu = input("Would you like to return to the main menu (Y/N)?: ")
            else :
                print("Not enough balance. Withdrawal cancelled.")
                menu = input("Would you like to return to the main menu (Y/N)?: ")
        case 2 :
            print("Your current balance is $" + str(balance))
            menu = input("Would you like to return to the main menu (Y/N)?: ")
        case _ :
            print("Invalid entry, please try again.")
            menu = input("Would you like to return to the main menu (Y/N)?: ")

print("\nThank you for banking with us!")