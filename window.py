# window.py in d_inheritance
"""
Title: Window class in inheritance
Author: zac waskowic
date-created: 2023-04-14
"""
import pygame

class Window:
    """
    Create the window that will load the game
    :return: None
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE  # text that appears in the title bar
        self.__FPS = FPS  # the frames/second the window will refresh
        self.__WIDTH = WIDTH  # width of the window
        self.__HEIGHT = HEIGHT  # height of the window
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)  # screen dimensions
        self.__BG_COLOUR = (50, 50, 50)  # uses the format (R, G, B)
        self.__FRAME = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)  # Surface object in pygame. Every item in your program with overlay on top of a Surface object
        self.__SURFACE.fill(self.__BG_COLOUR)
        pygame.display.set_caption(self.__TITLE)  # updates the title of the Window to the title text

    # MODIFIER METHODS
    def updateFrame(self):
        """
        Updates the Window object based on FPS
        :return:
        """
        self.__FRAME.tick(self.__FPS)  # Waits for the appropriate time based on the set FPS
        pygame.display.flip()  # Updates the window with the new frame.

    def clearScreen(self):
        """
        Fill the screen with the background colour
        :return:
        """
        self.__SURFACE.fill(self.__BG_COLOUR)

    # ACCESSOR METHOD
    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()
