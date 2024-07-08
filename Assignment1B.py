# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 1

# Program Assignment1B.py
import math

print("First color")
r1 = float(input("R: "))
g1 = float(input("G: "))
b1 = float(input("B: "))

print("Second color")
r2 = float(input("R: "))
g2 = float(input("G: "))
b2 = float(input("B: "))

red = (r2 - r1)**2
green = (g2 - g1)**2
blue = (b2 - b1)**2

distance = math.sqrt(red + green + blue)

print("Color Distance:", round(distance, 4))