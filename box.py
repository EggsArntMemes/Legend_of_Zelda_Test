# box.py in d_inheritance
"""
Title: Box subclass in inheritance example
Author: Zac Waskowic
Date-Created: 2023-04-17
"""
import pygame
from my_sprite import mySprite

class Box(mySprite):

    def __init__(self, WIDTH=1, HEIGHT=1):
        mySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setColor(self, TUPLE):
        # Polymorphs the setColor method from mySprite
        mySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)

    def setDIM(self, TUPLE):
        # Polymorphs the setDIM method from mySprite
        mySprite.setDIM(self, TUPLE)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setTransperancy(self, VALUE):
        self._SURFACE.set_alpha(VALUE)


if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Box Test")
    BOX = Box(50, 50)
    BOX.setSPD(10)
    BOX.setColor((0,255,0))

    COLLIDE_BOX = Box(300, 150)

    COLLIDE_BOX.setPOS((500,400))

    while True:
        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        PRESSED_KEYS = pygame.key.get_pressed()

        # processing
        if BOX.isSpriteColliding(COLLIDE_BOX.getPOS(), COLLIDE_BOX.getDIM()):
            COLLIDE_BOX.setColor((255, 0, 0))
            print("bein, smackeds")
        else:
            COLLIDE_BOX.setColor((255, 255, 255))

        BOX.moveWASD(PRESSED_KEYS)
        #BOX.marqueeX(WINDOW.getWidth())


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(COLLIDE_BOX.getSurface(), COLLIDE_BOX.getPOS())
        WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPOS())
        WINDOW.updateFrame()