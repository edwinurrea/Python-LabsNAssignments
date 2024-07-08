# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 6

# Program Lab6A.py
def isValid(width, height) :
    if (width + height) > 30 :
        print("This is a valid rectangle.")
        return True
    else :
        print("This is an invalid rectangle.")
        return False

def area(width, height) :
    area = width * height
    return area;

def perimeter(width, height) :
    perimeter = 2 * (width + height)
    return perimeter

# Main
while True and "y" and "Y":
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if (isValid(width, height)) :
        area1 = area(width, height)
        perimeter1 = perimeter(width, height)
        print("The area is:", area1)
        print("The perimeter is:", perimeter1)
        option = input("\nDo you want to enter another width and height (Y/N)?: ")
        if (option != "Y" and option != "y"):
            print("\nProgram Ends")
            break
    else :
        option = input("\nDo you want to enter another width and height (Y/N)?: ")
        if (option != "Y" and option != "y"):
            print("\nProgram Ends")
            break

