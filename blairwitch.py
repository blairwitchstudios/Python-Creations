print(" This was a creation made by BlairWitchStudios on 8/1/2022 at 3:58am")




name = input("Please enter your name:")
print("Welcome to the woods,", name, ", be careful...")



itemlist = ["flashlight", "switchblade", "compass"]
usermainitem = ("Please choose an object to help you through the forest:")



print(usermainitem)
print(itemlist)

usermainitem = input("Selected Item: ")



if usermainitem == "flashlight":
    print("Excellent choice, a flashlight to light your path!")
if usermainitem == "switchblade":
    print("Excellent choice, a switchblade to protect yourself!")
if usermainitem == "compass":
    print("Excellent choice, a compass to help guide you!")
    


path = ("left", "center", "right")

leftpath = "You decide the left path is the best option and begin walking"
centerpath = "You realize the center path is the best option and begin walking"
rightpath = "You guess the right path is the best option and begin walking"

print("It's time to enter the woods. Which path shall you take?")

print(path)

userpath = input("Seleted Path: ")

if userpath == "left":
    print(leftpath)
if userpath == "center":
    print(centerpath)
if userpath == "right":
    print(rightpath)
    
    
path = ("turn back", "investigate", "continue forward")
print("A snap of a twig makes you stop in your tracks.")
print("What do you do?", path)    
    
