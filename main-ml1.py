import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico")

from Lights import *
from Buzzer import *
from LightStrip import *
from Displays import LCDDisplay
import random

rand = random.randint(1, 100)/100

red = Light(6,"Red light")
green = Light(7,"Green light")


buzzer = PassiveBuzzer(13)
mylightstrip = LightStrip(name="My light strip", pin=2, numleds=16)
mydisplay = LCDDisplay(sda=0, scl=1,i2cid=0)

mydisplay.scroll("Allan Prieb - Florida International University",row=0, speed=100, skip=1)

for x in range(0,10):
    randBrightness = random.randint(1, 100)/100
    randRunType = random.randint(0,2)
    red.blink(delay=0.5, times=1)
    green.blink(delay=0.5, times=1)
    print("Random Brightness = " + str(randBrightness))
    print("Random Run Type = " + str(randRunType))
    mylightstrip.setBrightness(brightness=rand)
    mylightstrip.run(runtype=randRunType)
    buzzer.beep(tone=1000)


