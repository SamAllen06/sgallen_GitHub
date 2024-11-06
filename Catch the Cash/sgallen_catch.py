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
    def __init__(self):
        super().__init__()
        self.text = f"Score: 0"
        self.bgColor = ((200, 100, 0))
        self.center = (90, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 15"
        self.center = (550, 30)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.numMushrooms = 7
        self.ronald = Ronald(self)
        self.mushrooms = []
        for i in range(self.numMushrooms):
            self.mushrooms.append(Mushroom(self))
        self.sndMushroom = simpleGE.Sound("mushroom.wav")
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 15
        self.lblTime = LblTime()
        self.lblScore = LblScore()
        self.sprites = [self.ronald, self.mushrooms, self.lblScore, self.lblTime]
        
    def process(self):
        for mushroom in self.mushrooms:
            if mushroom.collidesWith(self.ronald):
                mushroom.reset()
                self.sndMushroom.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                self.lblScore.update()
        
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.1f}"
        if self.timer.getTimeLeft() <= 0:
            print(f"Score: {self.score}")
            self.stop()
        
class LblInstructions(simpleGE.MultiLabel):
    def __init__(self, fontName, totalTime = 10):
        super().__init__()
        self.textLines = "In this game you will play as Ronald, the", "adorable felt creature! Ronald is always", "extremely hungry and eats a rare type of", "mushroom that falls from the sky! Use the left", "and right arrow keys to catch as many", "mushrooms as you can and help Ronald survive!"
        self.bgColor = ((0, 150, 0))
        self.center = (320, 140)
        self.size = (490, 200)
        
class PlayButton(simpleGE.Button):
    def __init__(self, fontName):
        super().__init__()
        self.fgColor = (0x00, 0x00, 0x00)
        self.bgColor = (0xCC, 0xCC, 0xCC)
        self.text = "Play!"
        self.bgColor = ((250, 50, 250))
        self.center = (150, 400)
        self.size = (150, 35)

class QuitButton(simpleGE.Button):
    def __init__(self, fontName):
        super().__init__()
        self.fgColor = (0x00, 0x00, 0x00)
        self.bgColor = (0xCC, 0xCC, 0xCC)
        self.text = "Quit"
        self.bgColor = ((150, 0, 150))
        self.center = (490, 400)
        self.size = (150, 35)

class Introduction(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.lblInstructions = LblInstructions(self)
        self.playButton = PlayButton(self)
        self.quitButton = QuitButton(self)
        self.sprites = [self.lblInstructions, self.playButton, self.quitButton]
        
    def buttonChoice(self):
        nextStage = ""
        self.playButton.update()
        self.quitbutton.update()
        if self.quitButton.clicked == True:
            nextStage = "quit"
        if self.playButton.clicked == True:
            nextStage = "play"
        print (nextStage)
        self.playButton.update()
        self.quitButton.update()
        return nextStage

def main():
    keepGoing = True
    score = 0
    game = Game()
    game.start()

#     while keepGoing:
#         introduction = Introduction()
#         introduction.start()
#         nextStage = introduction.buttonChoice()
#         if nextStage == "play":
#             game = Game()
#             game.start()
#         if nextStage == "quit":
#             keepGoing = False        
            
if __name__ == "__main__":
    main()
        
        