# text.py in d_inheritance
"""
Title: Text class
Author: zac waskowic
date-created: 2023-04-14
"""
import pygame

from my_sprite import mySprite

class Text(mySprite):
    """
    concrete text sprite
    """

    def __init__(self, TEXT, SIZE=42, TYPEFACE="font_test/Angel Eyes.ttf"):
        mySprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_SIZE = SIZE
        self.__TYPEFACE = TYPEFACE
        self.__FONT = pygame.font.Font(self.__TYPEFACE, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    # MODIFIER METHODS
    def setColor(self, TUPLE):
        # Polymorphs the setColor method from mySprite
        mySprite.setColor(self, TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setFontSize(self, SIZE, TYPEFACE="font_test/Angel Eyes.ttf"):
        self.__FONT_SIZE = SIZE
        self.__TYPEFACE = TYPEFACE
        self.__FONT = pygame.font.SysFont(self.__TYPEFACE, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def UpdateText(self, TEXT):
        """
        sets the text
        :param TEXT: str
        :return: None
        """
        self.__TEXT = TEXT
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setTypeface(self, NEW_TYPEFACE):
        self.__TYPEFACE = NEW_TYPEFACE
        self.__FONT = pygame.font.SysFont(self.__TYPEFACE, self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setTransperancy(self, VALUE):
        self._SURFACE.set_alpha(VALUE)

if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Text Title")

    TEXT = Text("Hello World!")
    TEXT.setColor((255,0,0))
    TEXT.setSPD(10)
    TEXT.UpdateText("BANANA")
    TEXT.setFontSize(120)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # processing

        TEXT.marqueeX(WINDOW.getWidth())
        TEXT.UpdateText("test?")
        TEXT.setTransperancy(100)

        # outputs
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()




