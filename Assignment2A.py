# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 2

# Program Assignment2A.py
print("[Image Encoding Checker]")
width = int(input("What is the image width? "))
height = int(input("What is the image height? "))
size = int(input("What is the file size (in bytes)? "))

total = (width * height)
bPC = (size / total) * 2

if (bPC == 8) :
    print("\nThe RGBA image is encoded with 8 bits per channel.")
elif (bPC == 16) :
    print("\nThe RGBA image is encoded with 16 bits per channel.")
elif (bPC == 32) :
    print("\nThe RGBA image is encoded with 32 bits per channel.")
elif (bPC != 8, 16, 32 or bPC == -int) :
    print("\nThe information is invalid – please re-enter it.")
