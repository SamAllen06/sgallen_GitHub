import pygame, simpleGE, random

"""Catch the cash game demo"""

class Ronald(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("feltRonald.png")
        self.setSize(50, 60)
        self.position = (320, 410)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("mountainBackground.jpg")
        self.ronald = Ronald(self)
        
        self.sprites = [self.ronald]
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
        
        