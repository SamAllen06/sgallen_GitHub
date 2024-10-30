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
        self.y = -150
        
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
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.ronald = Ronald(self)
        self.mushroom = Mushroom(self)
        self.sndMushroom = simpleGE.Sound("mushroom.wav")
        
        self.sprites = [self.ronald, self.mushroom]
        
    def process(self):
        if self.mushroom.collidesWith(self.ronald):
            self.mushroom.reset()
            self.sndMushroom.play()
            
        
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
        
        