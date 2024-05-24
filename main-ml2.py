import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ClockController import *

myclock = ClockController()

while True:
  myclock.showTime()
  time.sleep(1)