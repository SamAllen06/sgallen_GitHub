#Start with a display box using IDEA / ALTER
def createDisplay():
    #import/initialize
    import pygame
    pygame.init()
    
    #display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Welcome, friend!")
    
    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((52, 199, 200))
    #make a box
    box = pygame.Surface((30, 30))
    box = box.convert()
    box.fill((100, 100, 100))
    #set up some variables for the box
    box_x = 0
    box_y = 0
    box_y_direction = "positive"
    
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
        #change the box's variable values
        box_x += 5
        if box_x > screen.get_width():
            box_x = -29
        if box_y == 0:
            box_y_direction = "positive"
        if box_y > screen.get_height()-30:
            box_y_direction = "negative"
        if box_y_direction == "positive":
            box_y += 3
        if box_y_direction == "negative":
            box_y -= 3
                
        #refresh the display
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
    
    #quit pygame after loop is finished
    pygame.quit()

#run main()
if __name__ == "__main__":
    createDisplay()
