# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 3

# Program Assignment3A.py
import random

def randomGen() :
    num1 = random.randint(-255, 255)
    num2 = random.randint(-255, 255)
    correct = str(num1 * num2)
    return correct, num1, num2

print("[Mathletes Game]")
mode = input("Choose a game mode (0=Easy, 1=Hard): ")

if (mode != "0") :
    print("So, you want a challenge? Okay!")
    correct, num1, num2 = randomGen()
    answer = input("Q1. " + str(num1) + " * " + str(num2) + " = ?\n")
    if answer == correct :
        print("Correct!")
        correct, num1, num2 = randomGen()
        answer = input("Q2. " + str(num1) + " * " + str(num2) + " = ?\n")
        if answer == correct :
            print("Correct!")
            correct, num1, num2 = randomGen()
            answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
            if answer == correct :
                print("Correct!")
                correct, num1, num2 = randomGen()
                answer = input("Q4. " + str(num1) + " * " + str(num2) + " = ?\n")
                if answer == correct:
                    print("Correct!")
                    correct, num1, num2 = randomGen()
                    answer = input("Q5. " + str(num1) + " * " + str(num2) + " = ?\n")
                    if answer == correct:
                        print("Correct!")
                        correct, num1, num2 = randomGen()
                        answer = input("Q6. " + str(num1) + " * " + str(num2) + " = ?\n")
                        if answer == correct:
                            print("Correct!\nYou win!")
                        else :
                            print("Incorrect!\nGame over...")
                    else:
                        print("Incorrect!\nGame over...")
                else:
                    print("Incorrect!\nGame over...")
            else:
                print("Incorrect!\nGame over...")
        else:
            print("Incorrect!\nGame over...")
    else:
        print("Incorrect!\nGame over...")
else :
    print("Playing on easy mode, huh? Okay!")
    correct, num1, num2 = randomGen()
    answer = input("Q1. " + str(num1) + " * " + str(num2) + " = ?\n")
    if answer == correct :
        print("Correct!")
        correct, num1, num2 = randomGen()
        answer = input("Q2. " + str(num1) + " * " + str(num2) + " = ?\n")
        if answer == correct :
            print("Correct!")
            correct, num1, num2 = randomGen()
            answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
            if answer == correct :
                print("Correct!\nYou win!")
            else :
                again = input("Incorrect! Try again.\n")
                if again == correct :
                    print("Correct!\nYou win!")
                else :
                    again = input("Incorrect! Try again.\n")
                    if again == correct :
                        print("Correct!\nYou win!")
                    else :
                        print("Incorrect!\nGame over...")
        else :
            again = input("Incorrect! Try again.\n")
            if again == correct :
                print("Correct!")
                correct, num1, num2 = randomGen()
                answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                if answer == correct :
                    print("Correct!\nYou win!")
                else :
                    again = input("Incorrect! Try again.\n")
                    if again == correct :
                        print("Correct!\nYou win!")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct :
                            print("Correct!\nYou win!")
                        else :
                            print("Incorrect!\nGame over...")
            else :
                again = input("Incorrect! Try again.\n")
                if again == correct :
                    print("Correct!")
                    correct, num1, num2 = randomGen()
                    answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                    if answer == correct :
                        print("Correct!\nYou win!")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct :
                            print("Correct!\nYou win!")
                        else :
                            again = input("Incorrect! Try again.\n")
                            if again == correct :
                                print("Correct!\nYou win!")
                            else :
                                print("Incorrect!\nGame over...")
                else :
                    print("Incorrect!\nGame over...")
    else :
        again = input("Incorrect! Try again.\n")
        if again == correct :
            print("Correct!")
            correct, num1, num2 = randomGen()
            answer = input("Q2. " + str(num1) + " * " + str(num2) + " = ?\n")
            if answer == correct :
                print("Correct!")
                correct, num1, num2 = randomGen()
                answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                if answer == correct :
                    print("Correct!\nYou win!")
                else :
                    again = input("Incorrect! Try again.\n")
                    if again == correct :
                        print("Correct!\nYou win!")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct :
                            print("Correct!\nYou win!")
                        else :
                            print("Incorrect!\nGame over...")
            else :
                again = input("Incorrect! Try again.\n")
                if again == correct :
                    print("Correct!")
                    correct, num1, num2 = randomGen()
                    answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                    if answer == correct :
                        print("Correct!\nYou win!")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct :
                            print("Correct!\nYou win!")
                        else :
                            again = input("Incorrect! Try again.\n")
                            if again == correct :
                                print("Correct!\nYou win!")
                            else :
                                print("Incorrect!\nGame over...")
                else :
                    again = input("Incorrect! Try again.\n")
                    if again == correct :
                        print("Correct!")
                        correct, num1, num2 = randomGen()
                        answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                        if answer == correct :
                            print("Correct!\nYou win!")
                        else :
                            again = input("Incorrect! Try again.\n")
                            if again == correct :
                                print("Correct!\nYou win!")
                            else :
                                again = input("Incorrect! Try again.\n")
                                if again == correct :
                                    print("Correct!\nYou win!")
                                else :
                                    print("Incorrect!\nGame over...")
                    else :
                        print("Incorrect!\nGame over...")
        else :
            again = input("Incorrect! Try again.\n")
            if again == correct :
                print("Correct!")
                correct, num1, num2 = randomGen()
                answer = input("Q2. " + str(num1) + " * " + str(num2) + " = ?\n")
                if answer == correct :
                    print("Correct!")
                    correct, num1, num2 = randomGen()
                    answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                    if answer == correct :
                        print("Correct!\nYou win!")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct:
                            print("Correct!\nYou win!")
                        else :
                            again = input("Incorrect! Try again.\n")
                            if again == correct:
                                print("Correct!\nYou win!")
                            else :
                                print("Incorrect!\nGame over...")
                else :
                    again = input("Incorrect! Try again.\n")
                    if again == correct :
                        print("Correct!")
                        correct, num1, num2 = randomGen()
                        answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                        if answer == correct :
                            print("Correct!\nYou win!")
                        else :
                            again = input("Incorrect! Try again.\n")
                            if again == correct :
                                print("Correct!\nYou win!")
                            else :
                                again = input("Incorrect! Try again.\n")
                                if again == correct :
                                    print("Correct!\nYou win!")
                                else :
                                    print("Incorrect!\nGame over...")
                    else :
                        again = input("Incorrect! Try again.\n")
                        if again == correct :
                            print("Correct!")
                            correct, num1, num2 = randomGen()
                            answer = input("Q3. " + str(num1) + " * " + str(num2) + " = ?\n")
                            if answer == correct :
                                print("Correct!\nYou win!")
                            else :
                                again = input("Incorrect! Try again.\n")
                                if again == correct :
                                    print("Correct!\nYou win!")
                                else :
                                    again = input("Incorrect! Try again.\n")
                                    if again == correct :
                                        print("Correct!\nYou win!")
                                    else :
                                        print("Incorrect!\nGame over...")
                        else :
                            print("Incorrect!\nGame over...")
            else :
                print("Incorrect!\nGame over...")
