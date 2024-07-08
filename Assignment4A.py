# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 4

# Program Assignment4A.py
def Average(one, grade1 = -1, grade2 = -1, grade3 = -1, grade4 = -1, grade5 = -1,
            grade6 = -1, grade7 = -1, grade8 = -1, grade9 = -1, grade10 = -1,
            grade11 = -1, grade12 = -1) :

    if (one == "Labs") :
        labAverage = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7 \
                    + grade8 + grade9 + grade10 + grade11 + grade12) / 12.0
        return labAverage

    if (one == "Assignments") :
        assignmentAverage = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7) / 7.0
        return assignmentAverage

    if (one == "Midterm") :
        midAverage = grade1 / 1.0
        return midAverage

    if (one == "Exam") :
        examAverage = grade1 / 1.0
        return examAverage

def Weighted(average, percent) :
    weight = average * percent
    return weight

print("[CSE 1321L Grade Calculator]")

print("Labs")
grade1 = float(input("Enter Grade #1: "))
grade2 = float(input("Enter Grade #2: "))
grade3 = float(input("Enter Grade #3: "))
grade4 = float(input("Enter Grade #4: "))
grade5 = float(input("Enter Grade #5: "))
grade6 = float(input("Enter Grade #6: "))
grade7 = float(input("Enter Grade #7: "))
grade8 = float(input("Enter Grade #8: "))
grade9 = float(input("Enter Grade #9: "))
grade10 = float(input("Enter Grade #10: "))
grade11 = float(input("Enter Grade #11: "))
grade12 = float(input("Enter Grade #12: "))
labAvg = Average("Labs", grade1, grade2, grade3, grade4, grade5, grade6, grade7,
                 grade8, grade9, grade10, grade11, grade12)
labWgt = Weighted(labAvg, 0.10)
print("Weighted Points: " + format(labWgt, ".2f"), "\n")

print("Assignments")
grade1 = float(input("Enter Grade #1: "))
grade2 = float(input("Enter Grade #2: "))
grade3 = float(input("Enter Grade #3: "))
grade4 = float(input("Enter Grade #4: "))
grade5 = float(input("Enter Grade #5: "))
grade6 = float(input("Enter Grade #6: "))
grade7 = float(input("Enter Grade #7: "))
assignmentsAvg = Average("Assignments", grade1, grade2, grade3, grade4, grade5, grade6, grade7)
assignmentsWgt = Weighted(assignmentsAvg, 0.40)
print("Weighted Points: " + format(assignmentsWgt, ".3f"), "\n")

print("Midterm")
grade1 = float(input("Enter Grade #1: "))
midAvg = Average("Midterm", grade1)
midWgt = Weighted(midAvg, 0.20)
print("Weighted Points: " + format(midWgt, ".1f"), "\n")

print("Exam")
grade1 = float(input("Enter Grade #1: "))
examAvg = Average("Exam", grade1)
examWgt = Weighted(examAvg, 0.30)
print("Weighted Points: " + format(examWgt, ".1f"), "\n")

final = labWgt + assignmentsWgt + midWgt + examWgt

print("Your final grade for CSE1321L is: " + format(final, ".2f"))
