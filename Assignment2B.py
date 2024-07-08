# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 2

# Program Assignment2B.py
char = input("Enter a character to use: ")
width = int(input("Enter the diamond's width: "))

if (width < 3) :
    width = int(input("Please enter a width of at least 3.\n"
                      "Enter the diamond's width: "))
while (width >= 3) :
    if (width % 2 != 0) :
        pass
        for i in range(1, width + 1, 2) :
            spaces = (width - i) // 2
            print(" " * spaces + char * i)
        for i in range(width - 2, 0, -2) :
            spaces = (width - i) // 2
            print(" " * spaces + char * i)
        break
    else :
        new = width + 1
        print("To make a diamond, we'll use", new, "as the width instead.")
        for i in range(1, new + 1, 2) :
            spaces = (new - i) // 2
            print(" " * spaces + char * i)
        for i in range(new - 2, 0, -2) :
            spaces = (new - i) // 2
            print(" " * spaces + char * i)
        break