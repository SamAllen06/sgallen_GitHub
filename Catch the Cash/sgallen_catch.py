import pygame, simpleGE, random

"""Catch the cash game demo"""

class Mushroom(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("feltMushroom.png")
        self.setSize(44, 56)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of the screen
        self.y = random.randint(-200, -100)
        
        #x is random from 22 to screen width minus 22
        self.x = random.randint(22, self.screenWidth-22)
        
        #dy is a random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.top > self.screenHeight:
            self.reset()

class Ronald(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("feltRonald.png")
        self.setSize(50, 60)
        self.position = (320, 410)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.x > 25:
                self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.x < self.screenWidth-25:
                self.x += self.moveSpeed

class LblScore(simpleGE.Label):
    def __init__(self, fontName, score = 0):
        super().__init__()
        self.text = f"Score: {score}"
        self.bgColor = ((200, 100, 0))
        self.center = (90, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self, fontName, totalTime = 10):
        #elapsedTime = simpleGE.Timer.getTimeLeft
        #totalTime = elapsedTime
        super().__init__()
        self.text = f"Time Left: {totalTime}"
        self.bgColor = ((200, 0, 150))
        self.center = (550, 30)
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.numMushrooms = 5
        self.ronald = Ronald(self)
        self.mushrooms = []
        for i in range(self.numMushrooms):
            self.mushrooms.append(Mushroom(self))
        self.sndMushroom = simpleGE.Sound("mushroom.wav")
        self.lblScore = LblScore(self)
        self.lblTime = LblTime(self)
        self.sprites = [self.ronald, self.mushrooms, self.lblScore, self.lblTime]
        
    def process(self):
        for mushroom in self.mushrooms:
            if mushroom.collidesWith(self.ronald):
                mushroom.reset()
                self.sndMushroom.play()
                #score +=1
                #simpleGE.LblScore.update(self)

class LblInstructions(simpleGE.Label):
    def __init__(self, fontName, totalTime = 10):
        super().__init__()
        self.text = f"In this game you will play as Ronald, the adorable felt creature! Ronald is always extremely hungry and eats a rare type of mushroom that falls from the sky! Use the left and right arrow keys to catch as many mushrooms as you can and help Ronald survive!"
        self.bgColor = ((200, 0, 150))
        self.center = (320, 240)
        self.size = (200, 100)

# class Instructions(simpleGE.Sprite):
#      def __init__(self, scene):
#          super().__init__(scene)
#          self.setImage("mountainBackground.jpg")

         

def main():
    keepGoing = True
    score = 0
    while keepGoing:
#         instructions = Instructions(score)
        game = Game()
        game.start()

if __name__ == "__main__":
    main()
        
        