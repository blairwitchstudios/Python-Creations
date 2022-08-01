import time
import sys

print(" This was a creation made by BlairWitchStudios on 8/1/2022 at 3:58am")
time.sleep(2)


name = input("Please enter your name:")
print("Welcome to the woods,", name, ", be careful...")



itemlist = ["flashlight", "switchblade", "compass"]
usermainitem = ("Please choose an object to help you through the forest:")
time.sleep(2)


print(usermainitem)
time.sleep(2)
print(itemlist)

usermainitem = input("Selected Item: ")



if usermainitem == "flashlight":
    print("Excellent choice, a flashlight to light your path!")
if usermainitem == "switchblade":
    print("Excellent choice, a switchblade to protect yourself!")
if usermainitem == "compass":
    print("Excellent choice, a compass to help guide you!")
    


path = ("left", "center", "right")

leftpath = "You decide the left path is the best option and begin walking."
centerpath = "You realize the center path is the best option and begin walking."
rightpath = "You guess that the right path is the best option and begin walking."

time.sleep(2)
print("It's time to enter the woods. Which path shall you take?")
time.sleep(2)
print(path)

userpath = input("Seleted Path: ")

if userpath == "left":
    print(leftpath)
if userpath == "center":
    print(centerpath)
if userpath == "right":
    print(rightpath)
    
time.sleep(2)    
userpath = ("turn back", "investigate", "continue forward")
print("A snap of a twig makes you stop in your tracks.")
time.sleep(2)
print("What do you do?")
print(userpath)
userpath = input("Selected option:")

if userpath == "continue forward":
    print("You decide it's more of a danger to turn back now. You continue forward...")
    
else:
    
    sys.exit()


