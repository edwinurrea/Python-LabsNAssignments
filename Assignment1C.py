# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 1

# Program Assignment1C.py
print("[How far your donation goes]\n")

soups = input("How many cans of soups? ")
rice = input("How many bags of rice? ")
veggies = input("How many cans of vegetables? ")
pb = input("How many cans of peanut butter? ")

totalSoup = int(soups) * 2
totalRice = int(rice) * 4
totalVeggies = float(veggies) * 3.5
totalPB = int(pb) * 7

total = totalSoup + totalRice + totalVeggies + totalPB

print("\nYour donation will help feed", total, "people!")
print(totalSoup, "people with the", soups, "can(s) of soup")
print(totalRice, "people with the", rice, "bag(s) of rice")
print(totalVeggies, "people with the", veggies, "can(s) of vegetables")
print(totalPB, "people with the", pb, "can(s) of peanut butter")