# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 3

# Program Assignment3B.py
print("[Epic Quest Simulator]")
answer = int(input("Hello stranger! Do you have time to hear my tale?"
                   "\n1) Yes"
                   "\n2) No\n"))
if answer == 2 :
    print("Ah, then goodbye...")
else :
    answer = int(input("Thank you! I come from the land of Pax Bisonica. Our country has been "
                       "\ntaken over by a cruel tyrant!"
                       "\n1) That's awful!"
                       "\n2) What can I do?\n"))
    if answer == 1 :
        print("Alas, it is truly terrible...")
        answer = int(input("Please, you must journey to Pax Bisonica and free our country!."
                           "\n1) Okay"
                           "\n2) No\n"))
        if answer == 2 :
            print("Then all is lost...")
        else :
            print("Hooray!!")
    else :
        answer = int(input("Please, you must journey to Pax Bisonica and free our country!."
                           "\n1) Okay"
                           "\n2) No\n"))
        if answer == 2 :
            print("Then all is lost...")
        else :
            print("Hooray!!")
