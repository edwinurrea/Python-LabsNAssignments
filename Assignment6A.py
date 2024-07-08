# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 6

# Program Assignment6A.py
import random
loops = 0
results = []

def computer() :
    randNum = random.randint(1, 3)
    if randNum == 1 :
        return "ROCK"
    elif randNum == 2 :
        return "PAPER"
    elif randNum == 3 :
        return "SCISSORS"

loop = int(input("How many games do you want to play?: "))

while loops < loop :
    loops = loops + 1
    game = input("Round " + str(loops) + ": What do you want to throw?: ").upper()
    cpu = computer()
    print("Computer threw " + cpu + "!")
    if game == cpu :
        results.append("Tied on Round " + str(loops) + " with " + game)
    elif (game == "ROCK" and cpu == "SCISSORS") or (game == "PAPER" and cpu == "ROCK") \
        or (game == "SCISSORS" and cpu == "PAPER") :
        results.append("Player won Round " + str(loops) + " with " + game)
    else :
        results.append("Computer won Round " + str(loops) + " with " + cpu)

if loops >= loop :
    print("Game Over...")
    print("\nHere's the recap: ")
    for result in results :
        print(result)