# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 11

# Program Lab11B.py
def letterPositions(str1, str2) :
    str1 = str1.lower()
    str2 = str2.lower()
    pos = []

    for i, char in enumerate(str1) :
        if char == str2 :
            pos.append(i)

    return tuple(pos)

while True :
    str1 = input("\nEnter your phrase: ")
    str2 = input("Enter a letter: ")
    pos = letterPositions(str1, str2)
    print(str2 + " appears inside your phrase in the following positions: " + str(pos))