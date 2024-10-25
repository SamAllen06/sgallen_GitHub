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
    background.fill((52, 199, 3))
    
    #action
    #assign values to key variables
    clock = pygame.time.Clock()
    
    #set up main Loop
    keepGoing = True
    while keepGoing:
        
        #timer
        clock.tick(30)
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #refresh the display
        screen.blit(background, (0, 0))
        pygame.display.flip()
    
    #quit pygame after loop is finished
    pygame.quit()

#run main()
if __name__ == "__main__":
    createDisplay()