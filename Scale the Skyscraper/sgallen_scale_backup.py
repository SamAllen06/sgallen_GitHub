import pygame, simpleGE, random

TOWER_HEIGHT = 1280
prevProgress = 640
response = "instructions"
originalX = 320
"""for testing purposes"""

def determineProgress(prevProgress):
    """will determine where the character is placed relative to the slider bar, 160 is its width"""
    """prevProgress is determined by the y value of the bottom of the ground sprite"""
    sliderBarProgress = (prevProgress-640)/TOWER_HEIGHT*260
#         print(sliderBarProgress)
    return sliderBarProgress

class LblInstructions(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = ["You are playing as Samm, the heroic ", 
                          "skyscraper union member. You are ",
                          "trying to climb the tower to defeat ",
                          "the evil CEO! Use W, A, D to move ",
                          "and jump, left shift to sprint, and ",
                          "the trackpad to control the mouse. "]
        self.center = (320, 200)
        self.size = (370, 220)
        self.bgColor = (50, 150, 50)
        """colors are subject to change"""
        
class BtnPlay(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Play!"
        self.size = (90, 30)
        self.center = (100, 400)
        self.bgColor = (255, 100, 0)

class BtnQuit(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Quit"
        self.size = (90, 30)
        self.center = (540, 400)
        self.bgColor = (255, 100, 0)

class Victory(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Congratulations, you won!"
        self.size = (300, 30)
        self.center = (320, 400)
        self.bgColor = (100, 0, 100)


class SliderBar(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        if response == "instructions":
            self.setImage("sliderBar.png")
            self.setSize(260, 50)
            self.position = (320, 400)
        if response == "play":
            self.setImage("sliderBarSideways.png")
            self.setSize(50, 260)
            self.position = (590, 240)

class Character(simpleGE.Sprite):
    def __init__(self, scene, response):
        super().__init__(scene)
        self.setImage("sammFront.png")
        self.setSize(40, 120)
        
        self.walkAnim = simpleGE.SpriteSheet("characterWalk.png", (64, 64), 4, 3, 0.2)
        self.walkAnim.startCol = 1
        self.animRow = 1
        self.moveSpeed = 5
        if response == "instructions":
            self.setSize(35, 105)
        if response == "begin":
            self.position = (30, 420)
        if response == "play":
            self.position = (240, 180)

    def process(self):
        if response != "instructions":
            self.inAir = False
            self.walking = False
            if self.isKeyPressed(pygame.K_a):
                self.animRow = 0
                self.x -= self.moveSpeed
                walking = True
            if self.isKeyPressed(pygame.K_d):
                self.animRow = 1
                self.x += self.moveSpeed
                self.walking = True
            if self.walking:
              self.copyImage(self.walkAnim.getNext(self.animRow))
            else:
              self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
            if self.isKeyPressed(pygame.K_w):
                if response == "begin" or response == "bossFight":
                    if self.inAir == False:
                        self.inAir == True
                        self.dy = -50
                        self.addForce(5, 270)
            if response == "begin":
                self.setBoundAction(self.STOP)
#             if response == "play" or response == "bossFight":
            else:
                if self.x >= 590:
                    self.dx = 0
                if self.x <= 50:
                    self.dx = 0            
        
class Instructions(simpleGE.Scene):
    def __init__(self, response):
        super().__init__()
        response = "instructions"
        pygame.display.set_caption(response)
        self.setImage("outsideBackground.png")
        
        self.lblInstructions = LblInstructions()
        self.btnPlay = BtnPlay()
        self.btnQuit = BtnQuit()
        self.sliderBar = SliderBar(self)
        self.victory = Victory()
        self.sammLabel = Character(self, response)
        print(self.sammLabel.position)
#         prevProgress = "win"
        try:
            sliderBarProgress = determineProgress(prevProgress)
            self.samm.position = (sliderBarProgress+190, 400)
            print(self.samm.position)
            self.sprites = [self.lblInstructions, self.btnPlay, self.btnQuit, self.sliderBar, self.sammLabel]
        except:
            if prevProgress == "win":
                self.sprites = [self.lblInstructions, self.btnPlay, self.btnQuit, self.victory]

    def process(self):
        if self.btnQuit.clicked:
            self.response = "quit"
            print(self.response)
            self.stop()
        if self.btnPlay.clicked:
            self.response = "begin"
            print(self.response)
            self.stop()

class Cloud(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.moveSpeed = 2
        self.setImage("cloud.png")
        self.setSize(214, 100)
        self.position = (107, 60)
        
    def process(self):
        self.setBoundAction(self.CONTINUE)
        if self.rect.left >= 640:
            self.x = -107
        if self.mouseOver:
            self.dx = 0
        else:
            self.dx = self.moveSpeed

class Begin(simpleGE.Scene):
    def __init__(self, response):
        super().__init__()
        print(response)
        response = "begin"
        pygame.display.set_caption(response)
        self.setImage("outsideBackground.png")
        self.samm = Character(self, response)
        self.cloud = Cloud(self)
        self.door = Platform(self)
        self.door.setImage("door.png")
        self.door.setSize(50, 100)
        self.door.position = (425, 430)
        self.sprites = [self.samm, self.cloud, self.door]
        print(response)

    def process(self):
        if self.samm.collidesWith(self.door):
            response = "play"
            self.stop()
            
class Enemy(simpleGE.Sprite):
    def __init__(self):
        super().__init__()
        self.setSize(50, 64)
        self.position = (320, 290)
        self.moveSpeed = 5
        
    def process(self):
        self.dx = moveSpeed
        if self.mouseOver:
            self.dx = 0
        elif self.x >= originalX+64:
            self.moveSpeed = -self.moveSpeed
        elif self.x <= originalX-64:
            self.moveSpeed = -self.moveSpeed
    
class Platform(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("platform.png")
        self.setSize(128, 25)
        self.inAir = False
        
    def process(self):
        self.setBoundAction(self.CONTINUE)
        if self.isKeyPressed(pygame.K_w):
            if self.inAir == False:
                self.inAir = True
                self.dy = 20
        if self.inAir:
            self.addForce(1, 90)

class Play(simpleGE.Scene):
    def __init__(self, prevProgress):
        super().__init__()
        response = "play"
        pygame.display.set_caption(response)
        self.setImage("insideBackground.png")
        
        self.sndDies = simpleGE.Sound("dies.wav")
        
        self.sliderBar = SliderBar(self)
        self.ground = Platform(self)
        self.ground.setImage("ground.png")
        self.ground.setSize(650, 240)
        self.ground.position = (320, 360)
        self.samm = Character(self, response)
        self.door = Platform(self)
        self.door.setImage("door.png")
        self.door.setSize(50, 100)
        self.door.position = (320, -600)
        
        self.sammSlider = Character(self, response)
        self.sammSlider.setSize(35, 105)
        self.sammSlider.position = (590, 110)
        print(self.sammSlider.position)
        self.sprites = [self.sliderBar, self.ground, self.sammSlider, self.samm, self.door]
        
        platform_dict = {}
        for i in range(240, TOWER_HEIGHT+1):
            if i%260 == 0:
                self.platform = i/260
                platform_dict[self.platform] = Platform(self)
                if random.randint(1, 10) >= 4:
                    platform_dict[self.platform].position = (184, i-10)
                else:
                    platform_dict[self.platform].position = (420, i-10)
                self.sprites.append(platform_dict[self.platform])
        for i in range(240, TOWER_HEIGHT+1):
            if (i+130)%260 == 0:
                self.platform = (i+130)/260
                platform_dict[self.platform] = Platform(self)
                platform_dict[self.platform].position = (320, i-10)
                self.sprites.append(platform_dict[self.platform])

def process(self):
        sliderBarProgress = determineProgress(prevProgress)
        self.sammSlider.position = (590, sliderBarProgress+110)
        
        if self.samm.collidesWith(self.ground):
            self.ground.inAir = False
            print("collides")
            self.ground.dy = 0
        if self.samm.collidesWith(platform_dict[self.platform]):
            platform_dict[self.platform].inAir = False
        if self.samm.collidesWith(self.door):
            response = "bossFight"
            self.stop()
        if self.samm.collidesWith(self.enemy):
            self.sndDies.play()
            response = "instructions"
            self.stop()

# instructions = Instructions(response)
# instructions.start()
# 
# begin = Begin(response)
# begin.start()
# 
play = Play(response)
play.start()

