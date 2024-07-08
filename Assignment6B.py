# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 6

# Program Assignment6B.py
def clearLevel(level, width, height) :
    for i in range(height) :
        level[i] = ["_" for _ in range(width)]

def addPlatform(level, x, y, length, width, height) :
    if (x < 0) or (x >= width) or (y < 0) or (y >= height) :
        print("The starting point is not a valid location!")
        return

    if x + length > width :
        print("This platform won't fit in the level!")
        return

    for i in range(length) :
        level[y][x + i] = "="

def addItems(level, x, y, width, height) :
    if (x < 0) or (x >= width) or (y < 0) or (y >= height) :
        print("This is not a valid location!")
        return
    level[y][x] = "P"

def showMap(level) :
    for row in level :
        print("".join(row))

print("[FYE Level Map Creator]")
width = int(input("Enter a level map width: "))
height = int(input("Enter a level map height: "))

level = [["_"] * width for _ in range(height)]
showMap(level)

while True :
    print("Options"
          "\n1. Clear Level"
          "\n2. Add Platform"
          "\n3. Add Items"
          "\n4. Quit")
    choice = int(input("Enter a choice: "))

    if choice == 1 :
        print("\n[Clear Level]")
        clearLevel(level, width, height)
        showMap(level)
    elif choice == 2 :
        print("\n[Add Platform]")
        x = int(input("Enter X Coordinate: "))
        y = int(input("Enter Y Coordinate: "))
        length = int(input("Enter Length: "))
        addPlatform(level, x, y, length, width, height)
        showMap(level)
    elif choice == 3 :
        print("\n[Add Item]")
        x = int(input("Enter X Coordinate: "))
        y = int(input("Enter Y Coordinate: "))
        addItems(level, x, y, width, height)
        showMap(level)
    elif choice == 4 :
        showMap(level)
        print("\nGoodbye!")
        break