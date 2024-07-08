# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 3

# Program Lab3A.py
balance = float(input("Amount owed: $"))
apr = float(input("APR: "))
monthlyRate = apr / int(12)
minimumPayment = balance * (monthlyRate/100)
print("Monthly percentage rate:", round(monthlyRate, 3))
print("Minimum payment: $" + str(round(minimumPayment, 2)))