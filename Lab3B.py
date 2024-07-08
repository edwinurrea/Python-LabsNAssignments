# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 3

# Program Lab3B.py
oneHours = int(input("Course 1 hours: "))
oneGrade = int(input("Grade for course 1: "))
twoHours = int(input("Course 2 hours: "))
twoGrade = int(input("Grade for course 2: "))
threeHours = int(input("Course 3 hours: "))
threeGrade = int(input("Grade for course 3: "))
fourHours = int(input("Course 4 hours: "))
fourGrade = int(input("Grade for course 4: "))
totalHours = oneHours + twoHours + threeHours + fourHours
totalPoints = (oneHours * oneGrade) + (twoHours * twoGrade) + \
              (threeHours * threeGrade) + (fourHours * fourGrade)
gpa = float(totalPoints / totalHours)
print("Total hours:", totalHours)
print("Total quality points:", totalPoints)
print("Your GPA for this semester is", round(gpa,2))