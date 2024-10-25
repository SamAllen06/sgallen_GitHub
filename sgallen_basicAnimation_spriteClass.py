import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        #set up the image
        self.image = pygame.image.load("samDrawing.jpg")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 35))
    
        #create corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 635
        self.rect.centery = 343
        
        #create ability to move
        self.dx = 3
        self.dy = 5
        
def update(self):
    self.rect.centerx += self.dx
    self.rect.centery += self.dy
        
    #check the bounds
    if self.rect.right > screen.get_width():
        self.rect.left = 0
    if self.rect.bottom > screen.get_height():
        self.rect.top = 0
            
    #clear and draw the sprite
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)