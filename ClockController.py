from Displays import LCDDisplay
from Button import *
from Clock import *
from Buzzer import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """

    def __init__(self):
        self._buzzer = PassiveBuzzer(13)
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(17, 'blue', buttonhandler=self),
                         Button(16, 'red', buttonhandler=self),
                         Button(15, 'yellow', buttonhandler=self),
                         Button(14, 'white', buttonhandler=self),
                         Button(11, 'green', buttonhandler=self)]
        

    def showTime(self):
        """" Show the time on the display """

        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
        
        self._display.showText(f'{hour:02d}:{minute:02d}:{sec:02d} ',0,4)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday", "Sunday"]
        day = days[wd - 1]
        
        display_width = 16  
        start_pos = (display_width - len(day)) // 2

        self._display.showText(f"{day[:3]} - {month:02d}/{date:02d}/{year:04d} ", 1, 0)


        if minute % 30 == 0 and sec < 15:
            self.play_song()
        else: 
            self._buzzer.stop()

        
        


    def buttonPressed(self, name):

        
        if name == 'red':
            
            hour = self._clock.getHour()
            
            self._clock.setHour(0 if hour == 23 else hour + 1)
            
        if name == 'blue':

            minute = self._clock.getMinute()
            
            self._clock.setMinute(0 if minute == 59 else minute + 1)
            self._clock.setSecond(0)
       
        if name == 'white':

            month = self._clock.getMonth()
            date = self._clock.getDate()
            
            if (month == 12):
                self._clock.setMonth(1)     
            elif month == 1 and date > 28:
                self._clock.setDate(28)
                self._clock.setMonth(month + 1)
            elif month in (3,5,8,10) and date > 30:
                self._clock.setDate(30)
                self._clock.setMonth(month + 1)
            else:  
                self._clock.setMonth(month + 1)     

        if name == 'yellow':
           
            date = self._clock.getDate()
            month = self._clock.getMonth()
            
            if month == 2 and date == 28:
                self._clock.setDate(1)
            elif month in (4, 6, 9, 11) and date == 30:
                self._clock.setDate(1)
            elif month in (1,3,5,7,8,10,12) and date == 31:
                self._clock.setDate(1)
            else:
                self._clock.setDate(date + 1)

            date = self._clock.getDate()
        """ Remove Year change feuture due to complexity of implementation with the available hardware
        if name == 'green':
            year = self._clock.getYear()

            if year == 2050:
                self._clock.setYear(2020)
            else:
                self._clock.setYear(year + 1) """
        
            
    def buttonReleased(self, name):
        pass

    def play_song(self):
        song = [
            (tones['A#3'], 0.5), (tones['A3'], 0.5), (tones['G3'], 0.5), (tones['F3'], 0.5),
            (tones['G3'], 0.5), (tones['A#3'], 0.5), (tones['F3'], 0.5), (tones['A#3'], 0.5),
            (tones['A3'], 0.5), (tones['G3'], 0.5), (tones['F3'], 0.5), (tones['G3'], 0.5)
        ]
        start_time = time.time()
        for tone, duration in song:
            if time.time() - start_time > 20:
                break
            self._buzzer.play(tone)
            time.sleep(duration)
            self._buzzer.stop()
            time.sleep(0.1)

