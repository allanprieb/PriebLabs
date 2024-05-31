import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ColorMatching import *

mygame = Matching()

while True:
  mygame.matches()
  time.sleep(1)