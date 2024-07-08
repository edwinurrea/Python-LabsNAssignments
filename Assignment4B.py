# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 4

# Program Assignment4B.py
def validation(message, offset) :
    if (offset >= 0 and offset <= 26 and message.replace(" ", "").isalpha()) :
        return True
    else :
        return False

def encryption(message, offset) :
    encryptedMessage = ""
    for char in message :
        if char.isalpha() :
            if (char.isupper()) :
                moveBy = (ord(char) - ord('A') + offset) % 26
                moved = ord('A') + moveBy
                encryptedMessage += chr(moved)
            if (char.islower()):
                moveBy = (ord(char) - ord('a') + offset) % 26
                moved = ord('a') + moveBy
                encryptedMessage += chr(moved)
        else :
            encryptedMessage += char
    return encryptedMessage.upper()

again = "Y"

while (again == "Y" or again == "y") :
    message = input("\nEnter your message:\n")
    offset = int(input("Enter the offset value: "))

    valid = validation(message, offset)

    if (valid == False) :
        print("Sorry, we can only process messages with letters and spaces, "
              "and the offset \nmust be between 0 and 26.")
        again = input("\nDo you want to encrypt another message?: ")
    else :
        encryptedMessage = encryption(message, offset)
        print("Your secret message is...\n" + encryptedMessage)
        again = input("\nDo you want to encrypt another message?: ")

print("\nClosing out...")
