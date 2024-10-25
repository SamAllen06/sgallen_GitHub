#Start with a display box using IDEA / ALTER
def createDisplay():
    #import/initialize
    import pygame
    import random
#     import spriteClass
    pygame.init()
    
    #display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Welcome, friend! Want a high five?")
    
    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    colorOne = colorTwo = colorThree = 0
    background.fill((colorOne, colorTwo, colorThree))

#     #instantiate the sprite
#     sam = spriteClass.Sprite()
#     allSprites = pygame.sprite.Group(sam)

    #make a box
    box = pygame.image.load("hand.JPG")
    box = box.convert_alpha()
    box = pygame.transform.scale(box, (250, 250))
    #set up some variables for the box
    box_x = 0
    box_y = 0
    box_x_direction = "positive"
    box_y_direction = "positive"
    change_x = random.randint(1, 8)
    change_y = random.randint(1, 8)
    

    #action
    #assign values to key variables
    clock = pygame.time.Clock()
    
    #set up main Loop
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #change the background's variables
        if colorOne <= 0:
            colorOneChange = "positive"
        if colorOneChange == "positive":
            colorOne += 1
        if colorOne >= 255:
            colorOneChange = "negative"
        if colorOneChange == "negative":
            colorOne -= 3
        if colorTwo <= 0:
            colorTwoChange = "positive"
        if colorTwoChange == "positive":
            colorTwo += 2
        if colorTwo >= 255:
            colorTwoChange = "negative"
        if colorTwoChange == "negative":
            colorTwo -= 2
        if colorThree <= 0:
            colorThreeChange = "positive"
        if colorThreeChange == "positive":
            colorThree += 3
        if colorThree >= 255:
            colorThreeChange = "negative"
        if colorThreeChange == "negative":
            colorThree -= 1
        if colorOne <= 0:
            colorOne = 0
        if colorOne >= 255:
            colorOne = 255
        if colorTwo <= 0:
            colorTwo = 0
        if colorTwo >= 255:
            colorTwo = 255
        if colorThree <= 0:
            colorThree = 0
        if colorThree >= 255:
            colorThree = 255
        background.fill((colorOne, colorTwo, colorThree))

        #change the box's variable values
        if box_x < 0:
            change_x = random.randint(1, 8)
            box_x_direction = "positive"
        if box_x > 390:
            change_x = random.randint(1, 8)
            box_x_direction = "negative"
        if box_x_direction == "positive":
            box_x += change_x
        if box_x_direction == "negative":
            box_x -= change_x
        if box_y < 0:
            box_y_direction = "positive"
            change_y = random.randint(1, 8)
        if box_y > 230:
            box_y_direction = "negative"
            change_y = random.randint(1, 8)
        if box_y_direction == "positive":
            box_y += change_y
        if box_y_direction == "negative":
            box_y -= change_y
        
#         #update the sprite
#         spriteClass.update()
        
        #refresh the display
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
    
    #quit pygame after loop is finished
    pygame.quit()

#run main()
if __name__ == "__main__":
    createDisplay()

