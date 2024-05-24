import random
from LightStrip import *
from Buzzer import *
from Button import *
from Displays import LCDDisplay

class Player:
    def __init__(self):
        self._score = 0

class GameField:
    def __init__(self, color=None):
        pass

class Matching:
    def __init__(self, size=8):
        self._playing = False
        self._score = 0
        self._size = size
        self._lights = LightStrip(pin=20, numleds=size, brightness=1) 
        self._buz = PassiveBuzzer(13)
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(17, 'blue', buttonhandler=self),
                         Button(16, 'red', buttonhandler=self),
                         Button(15, 'yellow', buttonhandler=self),
                         Button(14, 'white', buttonhandler=self)]  
        # for testing purposes only
        self._prevColor = " "
        
    
    # check if the button pressed is a valid match
    def matches(self, color=None):
        # temporary testing code
        self._display.showText(f"Score: {self._score}", 0, 3)
        self._lights.show()

    def buttonPressed(self, name):
        
        
        if not self._playing:
            self._score = 0
            self._playing = True
            self._buz.play(500)
            time.sleep(0.2)
            self._buz.stop()
            self._display.showText(' ' * 16, 1, 0) # for testing only'
        
        # if statement for testing only
        elif name == self._prevColor:
            self._display.showText("Game Over", 1, 3)
            self._playing = False


        elif name == 'blue':
            self._buz.play(150)
            self._score += 1
            self._lights.setColor(BLUE, 8)
            time.sleep(0.2)
            self._buz.stop()

            self._prevColor = 'blue' # for testing only

            print(_prevColor)

        elif name == 'red':
            self._buz.play(150)
            self._score += 1
            self._lights.setColor(RED, 8)
            time.sleep(0.2)
            self._buz.stop()

            self._prevColor = 'red' # for testing only
            print(_prevColor)

        
        elif name == 'yellow':
            self._buz.play(150)
            self._score += 1
            self._lights.setColor(YELLOW, 8)
            time.sleep(0.2)
            self._buz.stop()

            self._prevColor = 'yellow' # for testing only
            print(_prevColor)

        else:
            self._buz.play(150)
            self._score += 1
            self._lights.setColor(WHITE, 8)
            time.sleep(0.2)
            self._buz.stop()

            self._prevColor = 'white' # for testing only
            print(_prevColor)

    def buttonReleased(self, name):
        pass

    def newColor(self):
        pass

    def refresh(self):
        pass