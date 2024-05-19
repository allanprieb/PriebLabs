from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """

    def __init__(self):
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(17, 'blue', buttonhandler=self),
                            Button(16, 'red', buttonhandler=self),
                            Button(15, 'yellow', buttonhandler=self),
                            Button(14, 'white', buttonhandler=self)]

    def showTime(self):
        """" Show the time on the display """

        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
        self._display.showText(f'{month}/{date} - {hour}:{minute}:{sec} ')
        
    def buttonPressed(self, name):
        if name == 'red':
            # get the current hour
            hour = self._clock.getHour()
            # set the hour to 1 + the current hour
            if hour == 23:
                self._clock.setHour(0)
            else:
                self._clock.setHour(hour + 1)
        if name == 'blue':
            # get the current hour
            minute = self._clock.getMinute()
            #set minute back to 
            if minute == 59:
                self._clock.setMinute(0)
                self._clock.setSecond(0)
            # set the hour to 1 + the current hour
            else:
                self._clock.setMinute(minute + 1)
                self._clock.setSecond(0)
        if name == 'white':
            # get the current month
            month = self._clock.getMonth()
            # set month back to 1 when it reaches 12
            if second == 12:
                self._clock.setMonth(1)
            # set the hour to 1 + the current month
             else:
                self._clock.setSecond(month + 1)
        if name == 'green':
            date = self._clock.setDate()
            month = self._clock.getMonth()
            if month == 2 and date == 28:
                self._clock.setMonth(1)
            elif (month == 4 or month == 6 or month == 9 or month == 11) and date == 30:
                self._clock.setMonth(1)
            elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and date == 31:
                self._clock.setMonth(1)
            else:
                self._clock.setMonth(date + 1)
            

    def buttonReleased(self, name):
        pass

