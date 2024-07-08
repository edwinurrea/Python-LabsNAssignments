# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 5

# Program Lab5A.py
print("\nPlease enter 10 numbers and this program will display the largest.")

largest = 0

for i in range (1, 11, 1) :
    number = int(input("Please enter number " + str(i) + ": "))
    if (number > largest) :
        largest = number

print("\nThe largest number was", largest)
