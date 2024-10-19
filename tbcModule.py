import random
class Character():
    def __init__(self):
        super().__init__()
        self.name = "unnamed"
        self.hitPoints = 0
        self.hitChance = 0
        self.maxDamage = 0
        self.armor = 0
    
    def propertyMaker(self, value, trait):
        @property
        def trait(self):
            return self.__trait
        
        @trait.setter
        def trait(self, value):
            self.__trait = value

def testInt(character, traitName, trait, minimum, maximum):
    keepGoing = True
    while keepGoing:
        traitResponse = input(f"What would you like {character}'s {traitName} to be? ")
        try:
            traitResponse = int(traitResponse)
            if traitResponse <= int(maximum):
                if traitResponse >= int(minimum):
                    trait = traitResponse
                    keepGoing = False
                else:
                    print(f"Sorry, that's smaller than the excepted minimum: {minimum}. Please try again. ")
            else:
                print(f"Sorry, that's larger than the excepted maximum: {maximum}. Please try again. ")
        except:
            print(f"Sorry, {traitResponse} is not an integer. Please try again. ")
    return trait

def printStats(character, traitName, trait):
    print(f"{character}'s {traitName} is {trait}.")

def statValueGetter(playerStat):
    randomStat = random.randint(1, playerStat)
    return randomStat
    

def doFight(personOne, personTwo):
    damageDealt = statValueGetter(personOne.maxDamage)
    print(f"{personOne.name} attacked {personTwo.name} for {damageDealt} points!")
    successAnswer = statValueGetter(100)
    if successAnswer > personOne.hitChance:
        damageDealt = 0
        print(f"But {personOne.name}'s attack missed.")
    else:
        armorBlocked = statValueGetter(personTwo.armor)
        print(f"{personTwo.name}'s armor blocked {armorBlocked} points!")
        if armorBlocked <= damageDealt:
            totalDamage = damageDealt - armorBlocked
            personTwo.health = personTwo.health - totalDamage
        print(f"{personTwo.name} now has {personTwo.health} health left!")
    return personTwo.health

