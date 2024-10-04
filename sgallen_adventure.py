def main():
    # runs the game until it's finished
    currentNode = "start"
    keepGoing = True
    while keepGoing:
        dictionary = getGame()
        currentNode = playNode(dictionary, currentNode)
        if currentNode == "quit":
            keepGoing = False
            print("Thanks for playing!")
    
def getGame():
    # returns a dictionary containing the game object
    dictionary = {
    "start": ["Hello and welcome to Sam's game! Choose an option. ", "Play! ", "choice", "Quit. ", "quit"], 
    "choice": ["You see two games on the floor in front of you. Choose which one you would like to play.", "Minecraft. ", "minecraft", "Monopoly. ", "monopoly"], 
    "monopoly": ["You excitedly start a game of Monopoly. An hour passes. A day passes. A week passes. This game is going nowhere, everyone is too rich. You give up. ", "Start over. ", "start", "Quit. ", "quit"], 
    "minecraft": ["You reach for minecraft but as soon as you touch it, you get sucked inside! Out in the distance you can see a village. You could run there or start mining a nearby tree. ", "Run to the village. ", "village", "Mine a tree. ", "tree"], 
    "village": ["You run. And run. And run. Did I mention that it was really far away? Well, you run out of hunger and die. ", "Start over. ", "start", "Quit. ", "quit"], 
    "tree": ["As any good beginner does, you start to mine a tree. You can now make a tool. What will you make?", "Pickaxe. ", "pickaxe", "Axe. ", "axe"], 
    "pickaxe": ["You make a pickaxe and start to dig down. Straight down. Didn't anyone teach you not to do that? You fall into a cave and get killed by zombies. ", "Start over. ", "start", "Quit. ", "quit"], 
    "axe": ["You make an axe and now can mine even more wood. What will you do next?", "Make a pickaxe. ", "pickaxe", "Make a sword. ", "sword"], 
    "sword": ["Now that you have a sword, you kill some animals and eat some food to replenish your hunger. Where will you go from here?", "A nearby ravine. ", "ravine", "The village from earlier. ", "villageTwo"], 
    "villageTwo": ["It was further than you thought. You make it... but barely. You're out of food and weak. Suddenly you see Jack Black! He says 'I... am Steve' with his usual gumption and signature eyebrow raise. This was too much for you, you pass out and die. ", "Start over. ", "start", "Quit. ", "quit"], 
    "ravine": ["You start to explore a ravine but it just keeps getting deeper and darker. You have to make a choice!", "Leave!", "leave", "Forge ahead!", "keep"], 
    "leave": ["Wow, you're a scaredy pants. A bat quickly flies in front of your face and you pass out due to fear. ", "Start over. ", "start", "Quit. ", "quit"], 
    "keep": ["Just what I like to see. After some more exploration, you find an Ancient City. If I'm being honest, I'd leave. This place is too dangerous. But what will you do? ", "Explore it!", "explore", "Leave!", "leave"], 
    "explore": ["Hmmmm, interesting. You find a chest and open it, finding full, enchanted diamond armor! And.. an egg? Well, you take it all when suddenly you hear a Warden pulling itself out of the ground right next to you! What do you do?!", "Run!!!!", "run", "Throw the egg. ", "egg"], 
    "run": ["You sprint off but your loud footsteps attract the attention of the Warden! It starts to speed up, catching up with you, and flings you into the ceiling. Simply put, you fall and die. ", "Start over. ", "start", "Quit. ", "quit"], 
    "egg": ["Interesting strategy. You stay perfectly still and throw the egg. By some miracle, it spawns a baby chicken! Terrified by the dark, the baby chicken runs around screaming and draws the Warden away from you! You manage to escape, trying to forget the morally questionable sacrifice you just made. The tales of your impressive feats spread from village to village and everyone is in awe of you! You win! Just don't tell them about the baby chicken...", "Play again!", "start", "Quit. ", "quit"], 
    }
    return dictionary
    
def playNode(dictionary, currentNode):
    # takes in a node string, processes the player input, and returns the next node
    keepGoing = True 
    value = (dictionary[currentNode])
    while keepGoing:
        print(f"{value[0]}")
        print(f"1) {value[1]}")
        print(f"2) {value[3]}")
        answer = input("Type 1 or 2: ")
        print()
        if answer in ("1", "2"):
            keepGoing = False
        else:
            print("Incorrect input, please type either a '1' or a '2'")
            print()
    if answer == "1":
        currentNode = value[2]
    if answer == "2":
        currentNode = value[4]
    return currentNode

main()