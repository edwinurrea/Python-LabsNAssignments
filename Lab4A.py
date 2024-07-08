# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 4

# Program Lab4A.py
examScore = float(input("Enter the score of your exam: "))

if(examScore >= 97.5) :
    print("Letter grade is: A+")
elif(examScore >= 94.5) :
    print("Letter grade is: A")
elif(examScore >= 91.5) :
    print("Letter grade is: A-")
elif(examScore >= 88.5) :
    print("Letter grade is: B+")
elif(examScore >= 85.5) :
    print("Letter grade is: B")
elif(examScore >= 82.5) :
    print("Letter grade is: B-")
elif(examScore >= 79.5) :
    print("Letter grade is: C+")
elif(examScore >= 76.5) :
    print("Letter grade is: C")
elif(examScore >= 73.5) :
    print("Letter grade is: C-")
elif(examScore >= 70.5) :
    print("Letter grade is: D+")
elif(examScore >= 67.5) :
    print("Letter grade is: D")
elif(examScore >= 64.5) :
    print("Letter grade is: D-")
elif(examScore <= 0 or examScore <= 64.49) :
    print("Letter grade is: F")
