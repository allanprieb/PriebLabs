from Sensors import *
from Motors import *

class Gate:
    """...."""

    def __init__(self, servoPin=20, pirpin=8, proxpin=21):
        self._servo = Servo(pin=servoPin, name="Gate 1")
        self._pir = DigitalSensor(pin=pirpin, lowactive=False)
        self._prox = DigitalSensor(pin=proxpin)

    def open(self):
        self._servo.setAngle(90)

    def close(self):
        self._servo.setAngle(180)

    def motionDetected(self):
        return self._pir.tripped()

    def vehiclePresent(self):
        return self._prox.tripped()
        