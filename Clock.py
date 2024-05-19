from Counters import Time

class Clock:
    """
    Our implementation of the Clock class
    """
    def getTime(self):
        return Time.getTime()

    def setTime(self, timetuple):
        Time.setTime(timetuple)

    def getHour(self):
        """ return the current hour as an int """

        timetuple = Time.getTime()
        return timetuple[3]

    def setHour(self, hour):
        """ Sets the RTC Hour to the hour parameter """
        # First get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # change the hour to the new hour
        timelist[3] = hour
        # save it back to the system
        Time.setTime(timelist)

    def getMinute(self):
        """ return the current minutes as an int """

        timetuple = Time.getTime()
        return timetuple[4]


    def setMinute(self, minute):
        """ Sets the RTC Hour to the minute parameter """
        # First get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # change the hour to the new hour
        timelist[4] = minute
        # save it back to the system
        Time.setTime(timelist)
    
    def getDate(self):
        """ return the current minutes as an int """

        timetuple = Time.getTime()
        return timetuple[2]
    
    def setDate(self, date):
        """ Sets the RTC Hour to the minute parameter """
        # First get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # change the hour to the new hour
        timelist[2] = date
        # save it back to the system
        Time.setTime(timelist)

    def getMonth(self):
        """ return the current minutes as an int """

        timetuple = Time.getTime()
        return timetuple[1]
    
    def setMonth(self, month):
        """ Sets the RTC Hour to the minute parameter """
        # First get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # change the hour to the new hour
        timelist[1] = month
        # save it back to the system
        Time.setTime(timelist)

    def getSecond(self):

        timetuple = Time.getTime()
        return timetuple[5]
        
    def setSecond(self, second):
        
        timetuple = Time.getTime()

        timelist = list(timetuple)

        timelist[5] = second

        Time.setTime(timelist)
    
    def getYear(self):
        timetuple = Time.getTime()
        return timetuple[0]

    def setYear(self, year):
        timetuple = Time.getTime()

        timelist = list(timetuple)

        timelist[0] = year

        Time.setTime(timelist)