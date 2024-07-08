# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 3

# Program Lab3C.py
smallSandwiches = int(input("Enter the number of small sandwiches: "))
mediumSandwiches = int(input("Enter the number of medium sandwiches: "))
largeSandwiches = int(input("Enter the number of large sandwiches: "))
extraLargeSandwiches = int(input("Enter the number of extra-large sandwiches: "))

totalCookingTime = (smallSandwiches * 30) + (mediumSandwiches * 60) + \
                   (largeSandwiches * 75) + (extraLargeSandwiches * 135)
cookingMinutes = int(totalCookingTime / 60)
cookingSeconds = int(((totalCookingTime / 60) - cookingMinutes) * 60)

print("\nYou've entered", smallSandwiches, "small sandwiches.")
print("You've entered", mediumSandwiches, "medium sandwiches.")
print("You've entered", largeSandwiches, "large sandwiches.")
print("You've entered", extraLargeSandwiches, "extra-large sandwiches.")
print("\nTotal cooking time is", cookingMinutes, "minutes and", cookingSeconds, "seconds.")