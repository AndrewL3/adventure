import random as ry
import sys
choice1 = ""
pathway = None
counter = 0
count = 0

def leftPrint():
    print("There is a corridor to the left.")

def rightPrint():
    print("There is a corridor to the right.")

def upPrint():
    print("There are stairs going up.")

unexplored = {"leftcorridor": leftPrint, "rightcorridor": rightPrint,
              "upstairs": upPrint}



def intro():
    global currentRoom
    global count
    global direction
    currentRoom = "lobby"
    direction = {"left": left,"right": right, "up": up}
    print("You wake up and you open your eyes.") 
    print("You find yourself in a dark empty house.")
    print("You are scared and you want to go outside.")
    for i in unexplored:
        unexplored[i]()
    print("Behind you is the front door.")
    print("Which way do you want to go?")

    choice()
    
def lobby():
    global currentRoom
    global count
    global direction
    currentRoom = "lobby"
    direction = {"left": left,"right": right, "up": up}
    for i in unexplored:
        unexplored[i]()
    print("Behind you is the front door.")
    print("Which way do you want to go?")

    choice()


def choice():
    global choice1
    global direction
    while True: 
        choice1 = input()
        choice1.lower()
        if choice1 not in direction:
            print("That's invalid")
        else:
            direction[choice1]()
            if choice1 in direction:
                del direction[choice1]
            break


def death():
    deathMessage = ["A deadly scorpion springs out and catches you by surprise! There's nothing you can do as it's tail whips towards you and stings you. You die shortly after from the venom.", 
                    "An arrow comes flying out of nowhere and pierces your skull. You die.", "You look up and see a huge boulder falling down. There's no time to escape and you are crushed to death.", 
                    "A toxic gas fills the air and enters into your lungs. You cough for a few minutes before you die.", 
                    "There's a swishing sound as you see an axe on a rope swinging towards you. You are sliced in half and you die."]
    deathChoice = ry.randint(0,4)
    print(deathMessage[deathChoice])
    sys.exit()
                    
def nothing():
    nothingMessage = ["There is a table. You lie there for a bit and continue your way", "There is a flower pot. But there is no flower. You continue your way",
                    "There is a chair. You rest for a second and continue your way.", "You find a chocolate bar. You eat it as you continue your way.", "There is a water fountain. You take a sip and you continue your way."]
    nothingChoice = ry.randint(0,4)
    print(nothingMessage[nothingChoice])
def win():
    winMessage = ["You see an exit and you walk through. You did it!", "You see an open door to the outside world. You did it!", "You see a window. You climb through to escape. You did it!" , 
                  "You see a trap door that leads to an underground tunnel. The tunnel leads you outside. You did it!", "You see a glass door. It's locked but you break it to escape. You did it!"]
    winChoice = ry.randint(0,4)
    print(winMessage[winChoice])
    print("Bye")
    sys.exit()

#backwords is there to prevent player from going forwards after leaving lobby
backwords = "You cannot go this way."
#lobby = ["leftcorridor","rightcorridor","staircase","frontdoor"]
#leftCorridorMap = ["leftdoor","rightdoor", backwords, "lobby"]
#rightCorridorMap = ["leftdoor","rightdoor", backwords, "lobby"]
#upstairsMap = ["leftdoor","rightdoor", backwords, "lobby"]

events = [death, death, death, nothing, nothing, win]

def left():
    global pathway
    global counter
    global currentRoom
    global direction
    if currentRoom != "lobby":
      option = ry.randint(0,((len(events) - 1)))
      events[option]()
      del events[option]
      pathway = True
      counter +=1
    else: 
      leftDescription()

    
def right():
    global pathway
    global counter
    global currentRoom
    global direction
    if currentRoom != "lobby":
      option = ry.randint(0,((len(events) - 1)))
      events[option]()
      del events[option]
      pathway = False
      counter +=1
    else: 
      rightDescription()

def up():
    global pathway
    global counter
    global currentRoom
    global direction
    if currentRoom == "lobby":
      upstairsDescription()
    else: 
      print("You can't go up here!")
      choice()
    
                  
# def forward():
  
# def back():

def leftDescription():
    global currentRoom
    global counter
    global pathway
    global direction
    direction = {"left": left,"right": right, "up": up}
    currentRoom = "leftcorridor"
    while counter != 2:
        if pathway == None:
            print("There's a left door and a right door.")
            print("Which way do you go?")
        elif pathway == True:
            print("There is a door on the right.")
        elif pathway == False:
            print("There is a door on the left.")
        choice()
    del unexplored["leftcorridor"]
    pathway = None
    counter = 0
    lobby()

def rightDescription():
    global currentRoom
    global counter
    global pathway
    global direction
    direction = {"left": left,"right": right, "up": up}
    currentRoom = "rightcorridor"
    while counter != 2:
        if pathway == None:
            print("You see cool stuff")
            print("There's a left door and a right door.")
            print("Which way do you go?")
        elif pathway == True:
            print("There is a door on the right.")
        elif pathway == False:
            print("There is a door on the left.")
        choice()
    del unexplored["rightcorridor"]
    pathway = None
    counter = 0   
    lobby()
    
def upstairsDescription():
    global currentRoom
    global counter
    global pathway
    global direction
    direction = {"left": left,"right": right, "up": up}
    currentRoom = "upstairs"
    while counter != 2:
        if pathway == None:
            print("You see cool stuff")
            print("There's a left door and a right door.")
            print("Which way do you go?")
        elif pathway == True:
            print("There is a door on the right.")
        elif pathway == False:
            print("There is a door on the left.")
        choice()
    del unexplored["upstairs"]
    pathway = None
    counter = 0    
    lobby()
	    #  0             1                2                3
guidance = {"left": left,"right": right, "up": up}
direction = {"left": left,"right": right, "up": up} #"forward": forward,"back": back}

intro()

