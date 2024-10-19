import tbcModule
def main():
    c1 = tbcModule.Character()
    c1.name = input("What would you like to name your character? ")
    c1.health = tbcModule.testInt(c1.name, "health", "hitPoints", 1, 100)
    c1.maxDamage = tbcModule.testInt(c1.name, "strength", "maxDamage", 0, 100)
    c1.hitChance = tbcModule.testInt(c1.name, "success rate", "hitChance", 0, 100)
    c1.armor = tbcModule.testInt(c1.name, "armor absorption", "armor", 0, 100)
    c2 = tbcModule.Character()
    c2.name = "The Monster"
    c2.health = tbcModule.testInt("the monster", "health", "hitpoints", 1, 100)
    c2.maxDamage = tbcModule.testInt("the monster", "strength", "maxDamage", 0, 100)
    c2.hitChance = tbcModule.testInt("the monster", "success rate", "hitChance", 0, 100)
    c2.armor = tbcModule.testInt("the monster", "armor absorption", "armor", 0, 100)
    print(f"{c1.name}'s Stats")
    print("====================")
    print(f"Health: {c1.health:14}")
    print(f"Strength: {c1.maxDamage:12}")
    print(f"Success Rate: {c1.hitChance:8}")
    print(f"Armor Absorption: {c1.armor:4}")
    print()
    print(f"The Monster's Stats")
    print("====================")
    print(f"Health: {c2.health:14}")
    print(f"Strength: {c2.maxDamage:12}")
    print(f"Success Rate: {c2.hitChance:8}")
    print(f"Armor Absorption: {c2.armor:4}")
    print()
    
    keepGoing = True
    while keepGoing:
        nextRound = input("Proceed in the fight? (Y/N) ")
        print()
        if nextRound.upper() == "N":
            print("Now exiting the combat game. ")
            keepGoing = False
        elif nextRound.upper() == "Y":
            c2.health = tbcModule.doFight(c1, c2)
            c1.health = tbcModule.doFight(c2, c1)
        else:
            print("Sorry, that's not a valid response. Please try again")
        if c1.health <= 0:
            if c2.health <= 0:
                print("It's a tie! No one wins.")
                keepGoing = False
            else:
                print(f"Sorry {c1.name}, you lose.")
                keepGoing = False
        elif c2.health <= 0:
            print(f"Congratulations {c1.name}! You win!")
            keepGoing = False

if __name__ == "__main__":
    main()