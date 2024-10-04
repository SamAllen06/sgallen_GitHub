import json

def main():
    #Runs the main loop
    #Calls a menu
    #Sends control to other parts of the program
    #Handles invalid input from menu
    
    currentNode = "start"
    keepGoing = True
    while keepGoing:
        choice = getMenuChoice()
        if choice == "0":
            keepGoing = False
            print()
            print("See you later!")
        elif choice == "1":
            gameFile = getDefaultGame()
        elif choice == "2":
            gameFile = loadGame()
        elif choice == "3":
            saveGame(gameFile)
        elif choice == "4":
            gameFile = editNode(gameFile)
        elif choice == "5":
            playGame(gameFile, currentNode)
        else:
            print("That's not a valid option! Please try again. ")
            print()

def getMenuChoice():
    #prints a menu of user options
    #returns a menu choice
    
    print("Welcome to the game editor! What would you like to do?")
    print("0) Exit")
    print("1) Load the default game")
    print("2) Load a game file")
    print("3) Save the current game")
    print("4) Edit or add a node")
    print("5) Play the current game")
    choice = input("Enter your choice here: ")
    print()
    return choice

def playGame(gameFile, currentNode):
    #plays the game
    #keeps going until the next node is "quit"
    
    keepGoing = True
    while keepGoing:
        value = (gameFile[currentNode])
        answer = playNode(gameFile, currentNode)
        if answer == "1":
            currentNode = value[2]
        if answer == "2":
            currentNode = value[4]
        if currentNode == "quit":
            keepGoing = False
            print("Quitting game!")
            print()
        
def playNode(gameFile, currentNode):
    #given the game data and a node
    #plays out the node
    #returns the next node
    
    keepGoing = True
    while keepGoing:
        value = (gameFile[currentNode])
        print(f"{value[0]}")
        print(f"1) {value[1]}")
        print(f"2) {value[3]}")
        answer = input("Would you rather do 1 or 2? ")
        print()
        if answer in ("1", "2"):
            keepGoing = False
        else:
            print("Incorrect input, please type either a '1' or a '2'")
            print()
    return answer

def getDefaultGame():
    #creates a single-node default game
    #returns that data structure
    
    gameFile = {
    "start": ("Welcome to the game! What would you like to do? ", "Start over", "start", "Quit", "quit")
    }
    print("Loaded the default game for you!")
    print()
    return gameFile

def editNode(gameFile):
    #given the current game structure
    #lists the current game content
    #gets a node name ro edit
    #if that node exists, copy it to an empty node
    #if it doesn't, make a new node with empty data
    #use editField() to allow user to edit each node
    #return the now edited node
    
    for i in gameFile:
            print(i, gameFile[i])
    print()
    node = input("Here is your current game! What node would you like to edit or create? ")
    if node in gameFile:
        playerNodeList = (gameFile[node])
    else:
        playerNodeList = ["empty", "empty", "empty", "empty", "empty"]
    listPart = ["situation", "option 1", "option 1 pathway", "option 2", "option 2 pathway"]
    zero = node
    newNodePart = editField(playerNodeList[0], listPart[0])
    one = newNodePart
    newNodePart = editField(playerNodeList[1], listPart[1])
    two = newNodePart
    newNodePart = editField(playerNodeList[2], listPart[2])
    three = newNodePart
    newNodePart = editField(playerNodeList[3], listPart[3])
    four = newNodePart
    newNodePart = editField(playerNodeList[4], listPart[4])
    five = newNodePart
    gameFile[zero] = (one, two, three, four, five)
    print()
    for i in gameFile:
        print(i, gameFile[i])
    print()
    return gameFile
        
def editField(nodePart, nodePartName):
    #get a field name
    #print the field's current value
    #if the user presses 'enter' immediately retain the current value
    #otherwise, use the new value
    
    newNodePart = input(f"Your current {nodePartName} is \"{nodePart}\". What would you like it to be? ")
    if newNodePart == "":
        newNodePart = nodePart
    return newNodePart

def saveGame(gameFile):
    #save the game to a data file
    #preset the file name
    #print the current game dictionary in human-readable format
    #save the file in JSON format
    
    saveFile = open("gameFile.json", "w")
    json.dump(gameFile, saveFile, indent=2)
    print(json.dumps(gameFile, indent=2))
    print()
    saveFile.close()
    print("I saved your game's data to gameFile.json! Here it is (above) if you want to look at it.")
    print()
    
def loadGame():
    #assume there is a data file named gameFile.json in the current directory
    #open that file
    #load the data into the game object
    #return that game object
    loadFile = open("gameFile.json", "r")
    gameFile = json.load(loadFile)
    loadFile.close()
    print("Loaded the file in for you!")
    print()
    return gameFile

main()