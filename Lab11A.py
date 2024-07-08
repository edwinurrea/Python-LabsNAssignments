# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 11

# Program Lab11A.py
def allMath(num1, num2) :
    add = num1 + num2
    subt = num1 - num2
    mult = num1 * num2
    if num2 == 0 :
        div = "None"
        fldiv = "None"
        modu = "None"
    else :
        div = num1 / num2
        fldiv = num1 // num2
        modu = num1 % num2
    power = num1 ** num2
    return add, subt, mult, div, fldiv, modu, power

while True :
    num1 = int(input("\nEnter your first number: "))
    num2 = int(input("Enter your second number: "))
    add, subt, mult, div, fldiv, modu, power = allMath(num1, num2)
    print("Your resulting tuple is (" + str(add) + ", " + str(subt)  + ", "
          + str(mult)  + ", " + str(div)  + ", " + str(fldiv)  + ", "
          + str(modu)  + ", " + str(power) + ")")