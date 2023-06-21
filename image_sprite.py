# image_sprite.py in e_bunny directory
"""
title: Image Sprite
author: zac waskowic
date-created: 2023-04-19
"""

import pygame
from my_sprite import mySprite

class ImageSprite(mySprite):
    """
    Load and manipulate images
    """

    def __init__(self, IMAGE_FILE):
        mySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__X_FLIP = False

    # Modifier methods
    ### Movement
    def moveWASD(self, KEYS_PRESSED):
        mySprite.moveWASD(self, KEYS_PRESSED)
        if KEYS_PRESSED[pygame.K_d]:
            if not self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = True
        if KEYS_PRESSED[pygame.K_a]:
            if self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = False

    ### Properties
    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        resize the image based on a factor
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth() * SCALE_X, self.getHeight() * SCALE_Y))

    def setFlipX(self):
        """
        Flip the image on the Y-axis
        :return: None
        """
        self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)


    def setTransperancy(self, VALUE):
        self._SURFACE.set_alpha(VALUE)


if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Image Sprite Test")
    BUNNY = ImageSprite("images/breademy.png")
    BUNNY.setScale(0.5)
    BUNNY.setTransperancy(10)
    BUNNY.setSPD(15)
    BUNNY.setFlipX()

    while True:
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        KEYS_PRESSED = pygame.key.get_pressed()
        # processing
        BUNNY.moveWASD(KEYS_PRESSED)




        # output
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BUNNY.getSurface(), BUNNY.getPOS())
        WINDOW.updateFrame()