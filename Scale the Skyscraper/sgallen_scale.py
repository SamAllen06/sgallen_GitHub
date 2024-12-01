import pygame, simpleGE

"""to fix:
change button, door, victory to correct ones
sound doesn't happen if you hit the door from the wrong side
sound doesn't always happen if an enemy kills you"""

def determinePlatformEdges(platform):
    oddPlatforms = [256, 384]
    secondPlatform = [80, 208]
    restEvenPlatforms = [432, 560]
    if platform == "odd":
        groundList = oddPlatforms
    if platform == "platform2":
        groundList = secondPlatform
    if platform == "restEven":
        groundList = restEvenPlatforms
    return groundList
        
def determineProgressX(prevProgress, towerHeight):
    """will determine where the character is placed relative to the slider bar, 160 is its width"""
    """prevProgress is determined by the y value of the bottom of the ground sprite"""
    sliderBarProgress = (prevProgress-600)/towerHeight*260
    return sliderBarProgress

def determineProgressY(prevProgress, towerHeight):
    """will determine where the character is placed relative to the slider bar, 160 is its width"""
    """prevProgress is determined by the y value of the bottom of the ground sprite"""
    sliderBarProgress = (640-prevProgress)/towerHeight*260
    return sliderBarProgress

class LblInstructions(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = ["You are playing as Samm, the heroic ", 
                          "skyscraper union member. You are ",
                          "trying to climb the tower to defeat ",
                          "the evil CEO! Use W, A, D to move ",
                          "and jump, left shift to sprint, and ",
                          "the trackpad to control the mouse. If ",
                          "you hover the mouse over the enemies, ",
                          "they will stop. However, the boss will ",
                          "just slow down. Also make sure to not ",
                          "touch the enemies! They'll kill you!"]
        self.center = (320, 175)
        self.size = (390, 340)
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
    def __init__(self, scene, response):
        super().__init__(scene)
        if response == "instructions":
            self.setImage("sliderBar.png")
            self.setSize(260, 50)
            self.position = (320, 400)
        if response == "play":
            self.setImage("sliderBarSideways.png")
            self.setSize(50, 260)
            self.position = (614, 130)
            
class CharacterSlider(simpleGE.Sprite):
    def __init__(self, scene, response):
        super().__init__(scene)
        self.response = response
        self.setImage("sammFront.png")
        self.setSize(35, 105)
        
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"
    
    def process(self):
        if self.y <5:
            self.y = 5
        if self.response == "instructions":
            if self.x > 450:
                self.x = 450

class Character(simpleGE.Sprite):
    def __init__(self, scene, response):
        super().__init__(scene)
        self.response = response
        self.setImage("sammFront.png")
        self.setSize(42, 128)
        self.overrideControls = False
        
        self.walkAnim = simpleGE.SpriteSheet("characterWalk.png", (64, 128), 4, 3, 0.2)
        self.walkAnim.startCol = 1
        self.animRow = 1
        self.moveSpeed = 5
        if self.response == "begin":
            self.position = (30, 415)
        if self.response == "play":
            self.position = (200, 195)
        if self.response == "bossFight":
            self.position = (100, 310)
        self.inAir = False
        self.walking = False
    
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"

    def process(self):
        if self.overrideControls != True:
            if self.dx == 0:
                self.walking = False
            if self.isKeyPressed(pygame.K_a):
                self.animRow = 0
                if self.isKeyPressed(pygame.K_LSHIFT):
                    self.dx = -2*self.moveSpeed
                else:
                    self.dx = -self.moveSpeed
                self.walking = True
            if self.isKeyPressed(pygame.K_a) == False:
                self.dx = 0
            if self.isKeyPressed(pygame.K_d):
                self.animRow = 1
                if self.isKeyPressed(pygame.K_LSHIFT):
                    self.dx = 2*self.moveSpeed
                else:
                    self.dx = self.moveSpeed
                self.walking = True
            if self.inAir:
                self.walking = False
            if self.walking:
                self.copyImage(self.walkAnim.getNext(self.animRow))
            else:
              self.copyImage(self.walkAnim.getCellImage(0, self.animRow))
            if self.inAir == True:
                if self.dx < 0:
                    self.copyImage(self.walkAnim.getCellImage(0, 2))
                if self.dx > 0:
                    self.copyImage(self.walkAnim.getCellImage(0, 3))
            if self.response == "begin" or self.response == "bossFight":
                if self.isKeyPressed(pygame.K_w):
                    if self.inAir == False:
                        self.inAir = True
                        if self.response == "begin":
                            self.dy = -20
                        if self.response == "bossFight":
                            self.dy = -21
                if self.response == "begin":
                    if self.y < 420:
                        if self.inAir:
                            self.addForce(1, 270)
                if self.response == "bossFight":
                    if self.y < 384:
                        self.addForce(1, 270)
                    if self.bottom > 384:
                        self.bottom = 384
                        self.dy = 0
                        self.inAir = False
                        self.walking = False
            if self.response == "play":
                if self.x >= 552:
                    self.x = 552
                if self.x <= 88:
                    self.x = 88
                
            if self.response == "bossFight":
                if self.x >= 600:
                    self.x = 600
                if self.x <= 40:
                    self.x = 40
        
            if self.response == "begin":
                if self.x <= 15:
                    self.x = 15
                if self.x >= 632:
                    self.x = 632
                
class Instructions(simpleGE.Scene):
    def __init__(self, response, prevProgress, towerHeight):
        super().__init__()
        self.prevProgress = prevProgress
        self.response = response
        pygame.display.set_caption(self.response)
        self.setImage("outsideBackground.png")
        
        self.lblInstructions = LblInstructions()
        self.btnPlay = BtnPlay()
        self.btnQuit = BtnQuit()
        self.sliderBar = SliderBar(self, response)
        self.victory = Victory()
        self.sammSlider = CharacterSlider(self, response)
        try:
            sliderBarProgress = determineProgressX(prevProgress, towerHeight)
            self.sammSlider.position = (sliderBarProgress+200, 400)
            self.sprites = [self.lblInstructions, self.btnPlay, self.btnQuit, self.sliderBar, self.sammSlider]
        except:
            if self.prevProgress == "win":
                self.prevProgress = 640
                self.sprites = [self.lblInstructions, self.btnPlay, self.btnQuit, self.victory]

    def process(self):
        if self.btnQuit.clicked:
            self.response = "quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "begin"
            self.stop()

class Cloud(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.moveSpeed = 2
        self.setImage("cloud.png")
        self.setSize(214, 100)
        self.position = (107, 60)
        self.sndStop = simpleGE.Sound("stop.wav")
        self.playSound = False
        
    def process(self):
        self.setBoundAction(self.CONTINUE)
        if self.rect.left >= 640:
            self.x = -107
        if self.mouseOver == False:
            self.playSound = True
        if self.mouseOver:
            if self.playSound == True:
                self.sndStop.play()
            self.playSound = False
            self.dx = 0
        else:
            self.dx = self.moveSpeed

class Begin(simpleGE.Scene):
    def __init__(self, response):
        super().__init__()
        self.response = response
        pygame.display.set_caption(self.response)
        self.setImage("outsideBackground.png")
        self.timer = simpleGE.Timer()
#         sndDoor = simpleGE.Sound("door.wav")
        self.sndDoor = simpleGE.Sound("dies.wav")
        
        self.samm = Character(self, response)
        
        self.cloud = Cloud(self)
        
        self.ground = Platform(self, response)
        self.ground.setSize(640, 100)
        self.ground.position = (320, 530)
        
        self.door = Platform(self, response)
        self.door.setImage("door.png")
        self.door.setSize(50, 100)
        self.door.position = (425, 430)
        
        
        self.sprites = [self.samm, self.cloud, self.door]

    def process(self):
        if self.samm.overrideControls != True:
            if self.samm.collidesWith(self.door):
                self.samm.overrideControls = True
                self.response = "play"
                self.timer.totalTime = 2
                self.samm.x -= self.samm.dx
                self.samm.y -= self.samm.dy
                self.samm.dx = 0
                self.samm.dy = 0
                self.sndDoor.play()
            if self.samm.collidesWith(self.ground):
                self.samm.y -= self.samm.dy
                self.samm.inAir = False
                self.samm.dy = 0
        if self.timer.getTimeLeft() <= 0:
            self.stop()
            
class Enemy(simpleGE.Sprite):
    def __init__(self, scene, originalX):
        super().__init__(scene)
        self.originalX = originalX
        self.inAir = False
        self.setSize(40, 64)
        self.moveSpeed = 3
        self.dx = self.moveSpeed
        self.walkDirection = self.dx
        self.sndStop = simpleGE.Sound("stop.wav")
        self.playSound = False
        
        self.walkAnim = simpleGE.SpriteSheet("enemyWalk.png", (64, 64), 4, 9, 0.06)
        self.walkAnim.startCol = 1
        self.animRow1 = 1
        self.animRow3 = 3
    
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"
        
    def process(self):
        self.dx = self.walkDirection
        self.setBoundAction(self.CONTINUE)
        if self.dx < 0:
            self.copyImage(self.walkAnim.getNext(self.animRow1))
        if self.dx > 0:
            self.copyImage(self.walkAnim.getNext(self.animRow3))
        self.platformBuffer = 64
        
        if self.mouseOver == False:
            self.playSound = True
        if self.mouseOver:
            if self.playSound == True:
                self.sndStop.play()
            self.playSound = False
            self.dx = 0
            self.copyImage(self.walkAnim.getCellImage(0, 2))
        if self.type == 1:
            self.originalX = 144
            if self.x >= self.originalX+self.platformBuffer:
                self.dx = -self.moveSpeed
                self.walkDirection = self.dx
            if self.x <= self.originalX-self.platformBuffer:
                self.dx = self.moveSpeed
                self.walkDirection = self.dx
        if self.type == 2:
            self.originalX = 500
            if self.x >= self.originalX+self.platformBuffer:
                self.dx = -self.moveSpeed
                self.walkDirection = self.dx
            if self.x <= self.originalX-self.platformBuffer:
                self.dx = self.moveSpeed
                self.walkDirection = self.dx
        if self.type == 3:
            self.originalX = 320
            if self.x >= self.originalX+self.platformBuffer:
                self.dx = -self.moveSpeed
                self.walkDirection = self.dx
            if self.x <= self.originalX-self.platformBuffer:
                self.dx = self.moveSpeed
                self.walkDirection = self.dx
                
        if self.isKeyPressed(pygame.K_w):
            if self.inAir == False:
                self.inAir = True
                self.dy = 20
        if self.inAir:
            self.addForce(1, 90)
            
class Platform(simpleGE.Sprite):
    def __init__(self, scene, response):
        super().__init__(scene)
        self.response = response
        self.setImage("platform.png")
        self.setSize(128, 25)
        self.inAir = False
        
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"
        
    def process(self):
        if self.response == "play":
            self.setBoundAction(self.CONTINUE)
            if self.isKeyPressed(pygame.K_w):
                if self.inAir == False:
                    self.inAir = True
                    self.dy = 20
            if self.inAir:
                self.addForce(1, 90)

class Tower(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("insideBackground.png")
        self.setSize(545, 480)
        self.position = (320, 240)

class Play(simpleGE.Scene):
    def __init__(self, response, originalX, groundList, towerHeight):
        super().__init__()
        self.response = response
        self.groundList = groundList
        self.prevProgress = 640
        pygame.display.set_caption(self.response)
        self.background.fill((120, 180, 255))
        self.timer = simpleGE.Timer()
        self.towerHeight = towerHeight
        
        self.sndDoor = simpleGE.Sound("dies.wav")
#         self.sndDoor = simpleGE.Sound("door.wav")
        self.sndDies = simpleGE.Sound("dies.wav")
        
        self.sliderBar = SliderBar(self, response)
        
        self.tower = Tower(self)
        
        self.ground = Platform(self, response)
        self.ground.setImage("ground.png")
        self.ground.setSize(650, 260)
        self.ground.position = (320, 390)
        
        self.samm = Character(self, response)
        
        self.tower = Tower(self)
        
        self.door = Platform(self, response)
        self.door.setImage("door.png")
        self.door.setSize(50, 100)
        self.door.position = (93, -1130)

        self.platform1 = Platform(self, response)
        self.platform1.position = (320, 90)

        self.enemy1 = Enemy(self, originalX)
        self.enemy1.position = (320, 54)
        self.enemy1.type = 3
        
        self.platform2 = Platform(self, response)
        self.platform2.position = (144, -100)
        
        self.enemy2 = Enemy(self, originalX)
        self.enemy2.position = (144, -136)
        self.enemy2.type = 1
        
        self.platform3 = Platform(self, response)
        self.platform3.position = (320, -290)
        
        self.enemy3 = Enemy(self, originalX)
        self.enemy3.position = (320, -326)
        self.enemy3.type = 3
        
        self.platform4 = Platform(self, response)
        self.platform4.position = (496, -480)
        
        self.enemy4 = Enemy(self, originalX)
        self.enemy4.position = (496, -516)
        self.enemy4.type = 2
        
        self.platform5 = Platform(self, response)
        self.platform5.position = (320, -670)
        
        self.enemy5 = Enemy(self, originalX)
        self.enemy5.position = (320, -706)
        self.enemy5.type = 3
        
        self.platform6 = Platform(self, response)
        self.platform6.position = (496, -890)
        
        self.enemy6 = Enemy(self, originalX)
        self.enemy6.position = (496, -926)
        self.enemy6.type = 2
        
        self.platform7 = Platform(self, response)
        self.platform7.position = (320, -1080)
        self.platform7.setSize(530, 25)

        self.sammSlider = CharacterSlider(self, response)
        
        self.sprites = [self.tower, self.ground, self.sliderBar, self.sammSlider, self.door, self.platform1, self.platform2, self.platform3, self.platform4, self.platform5, self.platform6, self.platform7, self.enemy1, self.enemy2, self.enemy3, self.enemy4, self.enemy5, self.enemy6, self.samm]
    
#     def subtract(self, minuends, subtrahend):
#         subtractionResults = []
#         for i in minuends:
#             print(subtrahend)
#             print(i)
#             minuends[int(i)] -= subtrahend
#             subtractionResults.append(i)
#         return subtractionResults
#     
#     def bounceOff(self, platform):
#         if self.samm.bottom < platform.bottom:
#             self.ground.inAir = self.platform1.inAir = self.platform2.inAir = self.platform3.inAir = self.platform4.inAir = self.platform5.inAir = self.platform6.inAir = self.samm.inAir = self.enemy1.inAir = self.enemy2.inAir = self.enemy3.inAir = self.enemy4.inAir = self.enemy5.inAir = self.enemy6.inAir = self.platform7.inAir = self.door.inAir = False
#             self.ground.dy = self.platform1.dy = self.platform2.dy = self.platform3.dy = self.platform4.dy = self.platform5.dy = self.platform6.dy = self.platform7.dy = self.door.dy = self.enemy1.dy = self.enemy2.dy = self.enemy3.dy = self.enemy4.dy = self.enemy5.dy = self.enemy6.dy = 0
#             if self.ground.dy < -21:
#                 minuends = [self.ground.y, self.platform1.y, self.platform2.y, self.platform3.y, self.platform4.y, self.platform5.y, self.platform6.y, self.platform7.y, self.ground.y, self.enemy1.y, self.enemy2.y, self.enemy3.y, self.enemy4.y, self.enemy5.y, self.enemy6]
#                 subtrahend = self.ground.dy
#                 subtractionResults = self.subtract(minuends, subtrahend)
#                 for i in minuends:
#                     i = subtractionResults[1]
#             if self.ground.dy >= -21:
#                 minuends = [self.ground.y, self.platform1.y, self.platform2.y, self.platform3.y, self.platform4.y, self.platform5.y, self.platform6.y, self.platform7.y, self.ground.y, self.enemy1.y, self.enemy2.y, self.enemy3.y, self.enemy4.y, self.enemy5.y, self.enemy6]
#                 subtrahend = -21
#                 subtractionResults = self.subtract(minuends, subtrahend)
#                 for i in minuends:
#                     i = subtractionResults[1]
#     
    def bounceOff(self, platform):
        if self.samm.bottom < platform.bottom:
            self.ground.inAir = self.platform1.inAir = self.platform2.inAir = self.platform3.inAir = self.platform4.inAir = self.platform5.inAir = self.platform6.inAir = self.samm.inAir = self.enemy1.inAir = self.enemy2.inAir = self.enemy3.inAir = self.enemy4.inAir = self.enemy5.inAir = self.enemy6.inAir = self.platform7.inAir = self.door.inAir = False
            self.ground.dy = self.platform1.dy = self.platform2.dy = self.platform3.dy = self.platform4.dy = self.platform5.dy = self.platform6.dy = self.platform7.dy = self.door.dy = self.enemy1.dy = self.enemy2.dy = self.enemy3.dy = self.enemy4.dy = self.enemy5.dy = self.enemy6.dy = 0
            if self.ground.dy < -21:
                self.ground.y -= self.ground.dy
                self.platform1.y -= self.ground.dy
                self.platform2.y -= self.ground.dy
                self.platform3.y -= self.ground.dy
                self.platform4.y -= self.ground.dy
                self.platform5.y -= self.ground.dy
                self.platform6.y -= self.ground.dy
                self.platform7.y -= self.ground.dy
                self.door.y -= self.ground.dy
                self.enemy1.y -= self.ground.dy
                self.enemy2.y -= self.ground.dy
                self.enemy3.y -= self.ground.dy
                self.enemy4.y -= self.ground.dy
                self.enemy5.y -= self.ground.dy
                self.enemy6.y -= self.ground.dy
            if self.ground.dy >= -21:
                self.ground.y += 21
                self.platform1.y += 21
                self.platform2.y += 21
                self.platform3.y += 21
                self.platform4.y += 21
                self.platform5.y += 21
                self.platform6.y += 21
                self.platform7.y += 21
                self.door.y += 21
                self.enemy1.y += 21
                self.enemy2.y += 21
                self.enemy3.y += 21
                self.enemy4.y += 21
                self.enemy5.y += 21
                self.enemy6.y += 21
        else:
            if platform != self.platform7:
                self.ground.y += self.ground.dy
                self.platform1.y += self.ground.dy
                self.platform2.y += self.ground.dy
                self.platform3.y += self.ground.dy
                self.platform4.y += self.ground.dy
                self.platform5.y += self.ground.dy
                self.platform6.y += self.ground.dy
                self.platform7.y += self.ground.dy
                self.door.y += self.ground.dy
                self.enemy1.y += self.ground.dy
                self.enemy2.y += self.ground.dy
                self.enemy3.y += self.ground.dy
                self.enemy4.y += self.ground.dy
                self.enemy5.y += self.ground.dy
                self.enemy6.y += self.ground.dy
                self.ground.dy = self.platform1.dy = self.platform2.dy = self.platform3.dy = self.platform4.dy = self.platform5.dy = self.platform6.dy = self.platform7.dy = self.door.dy = self.enemy1.dy = self.enemy2.dy = self.enemy3.dy = self.enemy4.dy = self.enemy5.dy = self.enemy6.dy = -5

    def process(self):
        self.prevProgress = self.ground.bottom
        sliderBarProgress = determineProgressY(self.prevProgress, self.towerHeight)
        self.sammSlider.position = (615, sliderBarProgress+240)
        
        groundList = self.groundList
        if self.samm.collidesWith(self.platform1):
            if self.samm.bottom < self.platform1.bottom:
                groundList = determinePlatformEdges("odd")
                self.groundList = groundList
        if self.samm.collidesWith(self.platform3):
            if self.samm.bottom < self.platform3.bottom:
                groundList = determinePlatformEdges("odd")
                self.groundList = groundList
        if self.samm.collidesWith(self.platform5):
            if self.samm.bottom < self.platform5.bottom:
                groundList = determinePlatformEdges("odd")
                self.groundList = groundList
        if self.samm.collidesWith(self.platform2):
            if self.samm.bottom < self.platform2.bottom:
                groundList = determinePlatformEdges("platform2")
                self.groundList = groundList
        if self.samm.collidesWith(self.platform4):
            if self.samm.bottom < self.platform4.bottom:
                groundList = determinePlatformEdges("restEven")
                self.groundList = groundList
        if self.samm.collidesWith(self.platform6):
            if self.samm.bottom < self.platform6.bottom:
                groundList = determinePlatformEdges("restEven")
                self.groundList = groundList
        if self.samm.collidesWith(self.ground):
                groundList = [0, 640]
                self.groundList = groundList
        if self.samm.collidesWith(self.platform7):
            groundList = [0, 640]
            self.groundList = groundList
            
        if self.samm.left > groundList[1]:
            self.ground.inAir = self.platform1.inAir = self.platform2.inAir = self.platform3.inAir = self.platform4.inAir = self.platform5.inAir = self.platform6.inAir = self.samm.inAir = self.enemy1.inAir = self.enemy2.inAir = self.enemy3.inAir = self.enemy4.inAir = self.enemy5.inAir = self.enemy6.inAir = self.platform7.inAir = self.door.inAir = True
        if self.samm.right < groundList[0]:
            self.ground.inAir = self.platform1.inAir = self.platform2.inAir = self.platform3.inAir = self.platform4.inAir = self.platform5.inAir = self.platform6.inAir = self.samm.inAir = self.enemy1.inAir = self.enemy2.inAir = self.enemy3.inAir = self.enemy4.inAir = self.enemy5.inAir = self.enemy6.inAir = self.platform7.inAir = self.door.inAir = True
        
        if self.samm.collidesWith(self.ground):
            self.bounceOff(self.ground)
        if self.samm.collidesWith(self.platform1):
            self.bounceOff(self.platform1)
        if self.samm.collidesWith(self.platform2):
            self.bounceOff(self.platform2)
        if self.samm.collidesWith(self.platform3):
            self.bounceOff(self.platform3)
        if self.samm.collidesWith(self.platform4):
            self.bounceOff(self.platform4)
        if self.samm.collidesWith(self.platform5):
            self.bounceOff(self.platform5)
        if self.samm.collidesWith(self.platform6):
            self.bounceOff(self.platform6)
        if self.samm.collidesWith(self.platform7):
            self.bounceOff(self.platform7)

        if self.samm.collidesWith(self.door):
            self.response = "bossFight"
            self.timer.totalTime = 2
            self.samm.overrideControls = True
            self.samm.x -= self.samm.dx
            self.samm.y -= self.samm.dy
            self.samm.dx = 0
            self.samm.dy = 0
            self.sndDoor.play()
        if self.timer.getTimeLeft() <= 0:
            self.stop()
        if self.samm.collidesWith(self.enemy1) or self.samm.collidesWith(self.enemy2) or self.samm.collidesWith(self.enemy3) or self.samm.collidesWith(self.enemy4) or self.samm.collidesWith(self.enemy5) or self.samm.collidesWith(self.enemy6):
            self.response = "instructions"
            self.sndDies.play()
            self.samm.overrideControls = True
            self.samm.y = 10000
            self.ground.dy = self.enemy1.dy = self.enemy2.dy = self.enemy3.dy = self.enemy4.dy = self.enemy5.dy = self.enemy6.dy = self.platform1.dy = self.platform2.dy = self.platform3.dy = self.platform4.dy = self.platform5.dy = self.platform6.dy = self.platform7.dy = 0
            self.timer.totalTime = 2.5
        if self.timer.getTimeLeft() <= 0:
            self.stop()
        if self.ground.dy == 0 or self.platform1.dy == 0 or self.platform2.dy == 0 or self.platform3.dy == 0 or self.platform4.dy == 0 or self.platform5.dy == 0 or self.platform6.dy == 0 or self.platform7.dy == 0:
            self.ground.dy = self.enemy1.dy = self.enemy2.dy = self.enemy3.dy = self.enemy4.dy = self.enemy5.dy = self.enemy6.dy = self.platform1.dy = self.platform2.dy = self.platform3.dy = self.platform4.dy = self.platform5.dy = self.platform6.dy = self.platform7.dy = 0
        if self.ground.dy != 0:
            self.samm.inAir = True
            
class Boss(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setSize(128, 128)
        self.position = (320, 350)
        self.dx = 10
        self.inAir = False
        
        self.walkAnim = simpleGE.SpriteSheet("bossWalk.png", (128, 128), 4, 9, 0.06)
        self.walkAnim.startCol = 1
        self.animRow1 = 1
        self.animRow3 = 3
    
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"

    def process(self):
        if self.x > 100:
            if self.x < 120:
                if self.inAir == False:
                    self.inAir = True
                    self.dy = -15
        if self.x > 540:
            if self.x < 560:
                if self.inAir == False:
                    self.inAir = True
                    self.dy = -15
        if self.bottom < 384:
            self.addForce(2, 270)
        if self.bottom > 384:
            self.bottom = 384
            self.dy = 0
            self.inAir = False
                                
        if self.dx < 0:
            self.copyImage(self.walkAnim.getNext(self.animRow1))
        if self.dx > 0:
            self.copyImage(self.walkAnim.getNext(self.animRow3))
                
        if self.x >= 600:
            self.x = 600
            self.dx = 0
        if self.x <= 40:
            self.x = 40
            self.dx = 0
    
class Button(simpleGE.Sprite):
    def __init__(self, scene, pressed, type):
        super().__init__(scene)
        self.pressed = pressed
        if type == 1:
            self.setImage("buttonLeft.png")
        if type == 2:
            self.setImage("button.png")
        if type == 3:
            self.setImage("buttonRight.png")
        if type == 4:
            self.setImage("buttonTop.png")
        self.setSize(30, 30)
    
    def hide(self):
        self.position = (320, -100)
        
    def checkBounds(self):
        checkbounds = "overwriting checkbounds"
        
class ButtonPressed(simpleGE.Sprite):
    def __init__(self, scene, pressed, type):
        super().__init__(scene)
        self.pressed = pressed
        if type == 1:
            self.setImage("buttonPressedLeft.png")
            self.setSize(20, 30)
        if type == 2:
            self.setImage("buttonPressed.png")
            self.setSize(30, 20)
        if type == 3:
            self.setImage("buttonPressedRight.png")
            self.setSize(20, 30)
        if type == 4:
            self.setImage("buttonPressedTop.png")
            self.setSize(30, 20)
    
    def process(self):
        if self.pressed == "yes":
            self.setImage("buttonPressed.png")
    
class BossFight(simpleGE.Scene):
    def __init__(self, response, prevProgress):
        super().__init__()
        self.setImage("bossRoom.png")
        self.playSound = False
        pressed = "no"
        
        self.sndSlows = simpleGE.Sound("slows.wav")
        self.sndDoor = simpleGE.Sound("dies.wav")
#         self.sndDoor = siimpleGE.Sound("door.wav")
        self.sndDies = simpleGE.Sound("dies.wav")
        self.sndButton = simpleGE.Sound("dies.wav")
#         self.sndButton = simpleGE.Sound("button.wav")
        self.sndVictory = simpleGE.Sound("dies.wav")
#         self.sndVictory = simpleGE.Sound("victory.wav")
        
        self.samm = Character(self, response)
        
        self.button1 = Button(self, pressed, 1)
        self.button1.position = (40, 160)
        self.button2 = Button(self, pressed, 1)
        self.button2.position = (40, 320)
        self.button3 = Button(self, pressed, 2)
        self.button3.position = (214, 360)
        self.button4 = Button(self, pressed, 2)
        self.button4.position = (426, 360)
        self.button5 = Button(self, pressed, 3)
        self.button5.position = (600, 160)
        self.button6 = Button(self, pressed, 3)
        self.button6.position = (600, 320)
        self.button7 = Button(self, pressed, 4)
        self.button7.position = (214, 55)
        self.button8 = Button(self, pressed, 4)
        self.button8.position = (426, 55)
        
        self.buttonPressed1 = ButtonPressed(self, pressed, 1)
        self.buttonPressed1.position = (35, 160)
        self.buttonPressed2 = ButtonPressed(self, pressed, 1)
        self.buttonPressed2.position = (35, 320)
        self.buttonPressed3 = ButtonPressed(self, pressed, 2)
        self.buttonPressed3.position = (214, 365)
        self.buttonPressed4 = ButtonPressed(self, pressed, 2)
        self.buttonPressed4.position = (426, 365)
        self.buttonPressed5 = ButtonPressed(self, pressed, 3)
        self.buttonPressed5.position = (605, 160)
        self.buttonPressed6 = ButtonPressed(self, pressed, 3)
        self.buttonPressed6.position = (605, 320)
        self.buttonPressed7 = ButtonPressed(self, pressed, 4)
        self.buttonPressed7.position = (214, 50)
        self.buttonPressed8 = ButtonPressed(self, pressed, 4)
        self.buttonPressed8.position = (426, 50)
        
        self.boss = Boss(self)
        
        self.sprites = [self.buttonPressed1, self.buttonPressed2, self.buttonPressed3, self.buttonPressed4, self.buttonPressed5, self.buttonPressed6, self.buttonPressed7, self.buttonPressed8,  self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.boss, self.samm]
    
        self.buttonPushes = 0
        
    def buttonPushing(self, button):
        if button.pressed == "no":
            button.pressed = "yes"
            button.hide()
            self.sndButton.play()
            self.buttonPushes +=1
    
    def process(self):
        if self.boss.mouseOver == False:
            self.playSound = True

        if self.samm.x < self.boss.x:
            if self.boss.mouseOver == False:
                self.boss.addForce(0.4, 180)
            if self.boss.mouseOver:
                if self.playSound == True:
                    self.sndSlows.play()
                    self.playSound = False
                self.boss.addForce(0.1, 180)
        if self.samm.x > self.boss.x:
            if self.boss.mouseOver == False:
                if self.playSound == True:
                    self.sndSlows.play()
                    self.playSound = False
                self.boss.addForce(0.4, 0)
            if self.boss.mouseOver:
                self.boss.addForce(0.1, 0)
        if self.samm.collidesWith(self.boss):
            self.sndDies.play()
            self.response = "instructions"
            self.stop()
        if self.samm.collidesWith(self.button1):
            self.buttonPushing(self.button1)
        if self.samm.collidesWith(self.button2):
            self.buttonPushing(self.button2)
        if self.samm.collidesWith(self.button3):
            self.buttonPushing(self.button3)
        if self.samm.collidesWith(self.button4):
            self.buttonPushing(self.button4)
        if self.samm.collidesWith(self.button5):
            self.buttonPushing(self.button5)
        if self.samm.collidesWith(self.button6):
            self.buttonPushing(self.button6)
        if self.samm.collidesWith(self.button7):
            self.buttonPushing(self.button7)
        if self.samm.collidesWith(self.button8):
            self.buttonPushing(self.button8)
        if self.buttonPushes == 8:
            self.sndVictory.play()
            self.response = "instructions"
            self.win = "win"
            self.stop()

def main():
    keepGoing = True
    response = "instructions"
    prevProgress = 640
    originalX = 320
    groundList = [0, 640]
    towerHeight = 1150
    while keepGoing:
        instructions = Instructions(response, prevProgress, towerHeight)
        instructions.start()
        if instructions.response == "begin":
            response = instructions.response
            prevProgress = instructions.prevProgress
            begin = Begin(response)
            begin.start()
        if instructions.response == "quit":
            keepGoing = False
        if begin.response == "play":
            response = begin.response
            play = Play(response, originalX, groundList, towerHeight)
            play.start()
        if play.response == "instructions":
            response = play.response
            prevProgress = play.prevProgress
        if play.response == "bossFight":
            response = play.response
            bossFight = BossFight(response, prevProgress)
            bossFight.start()
        try:
            if bossFight.response == "instructions":
                response = bossFight.response
                if bossFight.win == "win":
                    prevProgress = bossFight.win
                    bossFight.win = "not yet"
        except:
            prevProgress = play.prevProgress            
            
if __name__ == "__main__":
    main()



