# Test.py
"""
Title: Test file
Author: Zac Waskowic
Date-Created: 2023-06-20
"""
import pygame
from window import Window

class Engine:
    def __init__(self):
        self.__WINDOW = Window("test")
        pass

    def run(self):
        # pygame.mixer_music.play()
        # -- MUSIC LOOP -- #
        # self.playMusic()
        while True:
            # - INPUTS - #
            # allow the x in the title bar to work
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()




            # - OUTPUTS - #
            self.__WINDOW.clearScreen()


            self.__WINDOW.updateFrame()




if __name__ == "__main__":
    pygame.init()

    GAME = Engine()
    GAME.run()