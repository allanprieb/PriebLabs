import time
from MusicController import *

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

MusicController().run()