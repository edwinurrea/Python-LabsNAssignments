# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 5

# Program Lab5B.py
value = int(input("Please enter a value for the size: "))

print("This is the requested " + str(value) + "x" + str(value) + " box:")
for i in range (1, value + 1, 1) :
    print("*" * value)

print("This is the requested right-facing " + str(value) + "x" + str(value) + " right-triangle:")
for i in range (1, value + 1, 1) :
    spaces = (value - i) // 2
    print("*" * i + " " * spaces)

print("This is the requested left-facing " + str(value) + "x" + str(value) + " right-triangle:")
for i in range (1, value + 1) :
    spaces = (value - i)
    print(" " * spaces + "*" * i)
