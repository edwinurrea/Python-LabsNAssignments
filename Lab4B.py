# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 4

# Program Lab4B.py
print("Welcome!")
number = float(input("Please input a number: "))

options = int(input("What would you like to do to this number:\n"
      "0) Get the additive inverse of the number\n"
      "1) Get the reciprocal of the number\n"
      "2) Square the number\n"
      "3) Cube the number\n"
      "4) Exit the program\n"))

match options :
      case 0 :
            print("The additive inverse of", number, "is -" + str(number))
      case 1 :
            if number != 0 :
                  pass
                  reciprocal = 1 / number
                  print("The reciprocal of", number, "is", reciprocal)
            else :
                  print("Cannot divide by 0!")
      case 2 :
            square = number ** 2
            print("The square of", number, "is", square)
      case 3 :
            cube = number ** 3
            print("The cube of", number, "is", cube)
      case 4 :
            print("Thank you, goodbye!")
      case _ :
            print("Invalid input, please try again!")