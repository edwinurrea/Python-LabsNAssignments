# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 3

# Program Assignment3C.py
while True :
    squareSize = int(input("Enter the size of the square: "))
    if squareSize > 0 :
        break
    else :
        print("Invalid input!")
while True :
    borderSize = int(input("Enter the size of the border: "))
    if borderSize > 0 :
        break
    else :
        print("Invalid input!")
while True :
    squareColor = int(input("Enter the color of the square: "))
    if squareColor == 0 or squareColor == 1:
        break
    else :
        print("Invalid input!")
while True :
    borderColor = int(input("Enter the color of the border: "))
    if borderColor == 0 or borderColor == 1 :
        break
    else :
        print("Invalid input!")

print("PBM File Contents:"
      "\nP1")
total = squareSize + (2 * borderSize)
print((total),(total))

for i in range(total) :
    row = " "
    for j in range(total) :
        if (i < borderSize or i >= total - borderSize or
            j < borderSize or j >= total - borderSize) :
            row += str(borderColor) + " "
        else :
            row += str(squareColor) + " "
    print(row.strip())

