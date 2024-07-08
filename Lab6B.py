# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 6

# Program Lab6B.py
from MyMath import my_min, my_max, my_avg

num_one = int(input("Enter number 1: "))
num_two = int(input("Enter number 2: "))

min = my_min(num_one, num_two)
max = my_max(num_one, num_two)
avg = my_avg(num_one, num_two)

print("Min is", min)
print("Max is", max)
print("Average is", avg)