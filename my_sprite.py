# my_sprite.py in d_inheritance
"""
Title: Abstract Sprite Class
Author: zac waskowic
date-created: 2023-04-14
"""
import pygame
class mySprite:
    """
    many of the common attributes and methods for sprites in pygame
    """

    def __init__(self, WIDTH=0, HEIGHT=0, X=0, Y=0, SPD=1, COLOR=(255,255,255)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR  # White
        self.__DIR_X = 1
        self.__DIR_Y = 1

    # Modifier Methods
    ### Movement Methods
    def marqueeX(self, MAX_WIDTH, MIN_WIDTH=0):
        self.__X += self.__SPD
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()
        self.__POS = (self.__X, self.__Y)

    def moveWASD(self, KEYS_PRESSED):
        """
        move sprite with wasd
        :param KEYS_PRESSED: list
        :return: None
        """
        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD
        if KEYS_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD

        if KEYS_PRESSED[pygame.K_w]:
            self.__Y -= self.__SPD
        if KEYS_PRESSED[pygame.K_s]:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)

    def checkBoudaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        # Check boundaries
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X

        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y

        self.__POS = (self.__X, self.__Y)

    ### Properties Methods
    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setDIM(self, TUPLE):
        self._DIM = TUPLE

    def setPOS(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        self._COLOR = TUPLE

    def setSPD(self, SPD):
        self.__SPD = SPD

    # Accessor Methods
    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getDIM(self):
        return (self._SURFACE.get_width(), self._SURFACE.get_height())

    def getPOS(self):
        return self.__POS

    def getSurface(self):
        return self._SURFACE

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def isSpriteColliding(self, POSITION, DIMENSION):
        """
        Check if a sprite is colliding with the current sprite
        :param POSITION: tuple
        :param DIMENSION: tuple
        :return: bool
        """
        SPRITE_X = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]

        if SPRITE_X >= self.__X - SPRITE_W and SPRITE_X <= self.__X + self.getWidth():
            if SPRITE_Y >= self.__Y - SPRITE_H and SPRITE_Y <= self.__Y + self.getHeight():
                return True
        return False