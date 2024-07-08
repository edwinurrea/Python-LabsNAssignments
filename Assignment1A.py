# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 1

# Program Assignment1A.py
print("[Let's make a website (URL)!\n")

scheme = input("Scheme: ")
subDomain = input("Subdomain: ")
secondLevel = input("Second-level domain: ")
topLevel = input("Top-level domain: ")
subdirectory = input("Subdirectory: ")

print("\nYour URL is: \n" +
      scheme + "://" + subDomain + "." + secondLevel + "." + topLevel + "/" + subdirectory)
