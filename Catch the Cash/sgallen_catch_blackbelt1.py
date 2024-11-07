import pygame, simpleGE, random

"""Catch the cash game demo, set number of enemies"""

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
        
class GreenMushroom(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("greenMushroom.png")
        self.setSize(44, 58)
        self.minSpeedY = 4
        self.minSpeedX = -10
        self.maxSpeed = 10
        self.reset()
        
    def reset(self):
        #move to top of the screen
        self.y = random.randint(-200, -100)
        
        #dy is a random minSpeed to maxSpeed
        self.dy = random.randint(self.minSpeedY, self.maxSpeed)
        self.dx = random.randint(self.minSpeedX, self.maxSpeed)
        
        #determine where it spawns
        if self.dx > 0:
            self.x = random.randint(-320, 320)
        if self.dx == 0:
            self.x = random.randint(0, 640)
        else:
            self.x = random.randint(320, 960)
    
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
        self.text = "Time left: 20"
        self.center = (550, 30)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.numMushrooms = 8
        self.numGreenMushrooms = 20
        self.ronald = Ronald(self)
        self.mushrooms = []
        for i in range(self.numMushrooms):
            self.mushrooms.append(Mushroom(self))
        self.greenMushrooms = []
        for i in range(self.numGreenMushrooms):
            self.greenMushrooms.append(GreenMushroom(self))
        self.sndMushroom = simpleGE.Sound("mushroom.wav")
        self.sndGreenMushroom = simpleGE.Sound("greenMushroom.wav")
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 20
        self.lblTime = LblTime()
        self.lblScore = LblScore()
        self.sprites = [self.ronald, self.mushrooms, self.lblScore, self.lblTime, self.greenMushrooms]
        
    def process(self):
        for mushroom in self.mushrooms:
            if mushroom.collidesWith(self.ronald):
                mushroom.reset()
                self.sndMushroom.play()
                self.score += 1
                self.timer.totalTime += 1
                self.lblScore.text = f"Score: {self.score}"
                self.lblScore.update()
                
        for greenMushroom in self.greenMushrooms:
            if greenMushroom.collidesWith(self.ronald):
                greenMushroom.reset()
                self.sndGreenMushroom.play()
                self.timer.totalTime -= 3
    
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.0f}"
        if self.timer.getTimeLeft() <= 0:
            self.stop()
                    
class LblInstructions(simpleGE.MultiLabel):
    def __init__(self, fontName, totalTime = 10):
        super().__init__()
        self.textLines = [
        "In this game you will play as Ronald, the",
        "adorable felt creature! Ronald is always",
        "extremely hungry and eats a rare type of",
        "red mushroom that falls from the sky! Use the",
        "left and right arrow keys to catch as many red",
        "mushrooms as you can and extend Ronald's life!",
        "But make sure to dodge the poisonous, green",
        "mushrooms that shorten his life! But every good",
        "mushroom you eat spawns a new poisonous one!"]
        self.bgColor = ((0, 150, 0))
        self.center = (320, 150)
        self.size = (500, 280)
        
class PlayButton(simpleGE.Button):
    def __init__(self, fontName):
        super().__init__()
        self.text = "Play!"
        self.bgColor = ((250, 50, 250))
        self.center = (150, 400)
        self.size = (150, 35)

class QuitButton(simpleGE.Button):
    def __init__(self, fontName):
        super().__init__()
        self.text = "Quit"
        self.bgColor = ((150, 0, 150))
        self.center = (490, 400)
        self.size = (150, 35)

class IntroScore(simpleGE.MultiLabel):
    def __init__(self, fontName):
        super().__init__()
        self.lastScore = 0
        self.highScore = 0
        self.textLines = [
            f"Last score: {self.lastScore}",
            f"High score: {self.highScore}"]
        self.bgColor = ((100, 100, 100))
        self.center = (320, 350)
        self.size = (150, 90)

class Introduction(simpleGE.Scene):
    def __init__(self, lastScore, highScore):
        super().__init__()
        self.lastScore = lastScore
        self.highScore = highScore
        self.setImage("mountainBackground.jpg")
        self.lblInstructions = LblInstructions(self)
        self.playButton = PlayButton(self)
        self.quitButton = QuitButton(self)
        self.introScore = IntroScore(self)
        self.introScore.textLines = [
            f"Last score: {self.lastScore}",
            f"High score: {self.highScore}"]
        self.sprites = [self.lblInstructions, self.playButton, self.quitButton, self.introScore]
        
    def process(self):
        self.response = "play"
        if self.quitButton.clicked:
            self.response = "quit"
            self.stop()
        if self.playButton.clicked:
            self.response = "play"
            self.stop()

def main():
    keepGoing = True
    lastScore = 0
    highScore = 0
    while keepGoing:
        introduction = Introduction(lastScore, highScore)
        introduction.start()
        if introduction.response == "play":
            game = Game()
            game.start()
            lastScore = game.score
            if lastScore > highScore:
                 highScore = lastScore
        else:
            keepGoing = False
            
if __name__ == "__main__":
    main()
        
        
