# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 10

# Program Lab10B.py
mylist = []
selection = 0

def makeTuple(name, age) :
    mytuple = ("Name: " + name, "Age: " + str(age))
    return mytuple

print("[Friend List]")

while selection != 3 :
    selection = int(input("\n1 - Add friend\n"
                      "2 - List friends\n"
                      "3 - Quit\n"
                      "Make your selection: "))

    if selection == 1 :
        name = input("\nEnter your friend's name: ")
        age = int(input("Enter your friend's age: "))
        friend = makeTuple(name, age)
        mylist.append(friend)
        print("Friend added")

    if selection == 2 :
        for friend in mylist :
            name = friend[0]
            age = friend[1]
            print(f"{name}, {age}",)

    if selection == 3 :
        print("\nShutting down...")