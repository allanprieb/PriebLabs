"""
A basic template file for using the Model class in PicoLibrary
This will allow you to implement simple Statemodels with some basic
event-based transitions.

Currently supports only 4 buttons (hardcoded to BTN1 through BTN4)
and a TIMEOUT event for internal tranisitions.

For processing your own events such as sensors, you can implement
those in your run method for transitions based on sensor events.
"""

# Import whatever Library classes you need - Model is obviously needed
import time
import random
from StateModel import *
from Button import *
from Counters import *
from Log import *
from Buzzer import *
from Instruments import *
from LightStrip import *
from Displays import LCDDisplay

"""
This is the template Model Runner - you should rename this class to something
that is supported by your class diagram. This should associate with your other
classes, and any PicoLibrary classes. If you are using Buttons, you will implement
buttonPressed and buttonReleased.

To implement the model, you will need to implement 3 methods to support entry actions,
exit actions, and state actions.

This template currently implements a very simple state model that uses a button to
transition from state 0 to state 1 then a 5 second timer to go back to state 0.
"""

class MusicController:

    def __init__(self):
        
        # Instantiate whatever classes from your own model that you need to control
        # Handlers can now be set to None - we will add them to the model and it will
        # do the handling
        self._button1 = Button(15, "white", buttonhandler=None)
        self._button2 = Button(14, "red", buttonhandler=None)
        self._button3 = Button(16, "yellow", buttonhandler=None)
        self._button4 = Button(17, "blue", buttonhandler=None)
        self._button5 = Button(18, "black", buttonhandler=None)

        self._buzzer = PassiveBuzzer(13)
        self._instrument = Organ() 
        self._instrumentno = 0

        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._lights = LightStrip(pin=20, numleds=8, brightness=1) 

        self.PINK = (255, 192, 203) #	r: 255, g: 192, b: 203

        self.instruments= ["Violin", " Bass ", "Organ!"]

        # self._timer = SoftwareTimer(None)
        
        # Instantiate a Model. Needs to have the number of states, self as the handler
        # You can also say debug=True to see some of the transitions on the screen
        # Here is a sample for a model with 4 states
        self._model = StateModel(10, self, debug=True)
        
        # Up to 5 buttons and a timer can be added to the model for use in transitions
        # Buttons must be added in the sequence you want them used. The first button
        # added will respond to BTN1_PRESS and BTN1_RELEASE, for example
        self._model.addButton(self._button1)
        self._model.addButton(self._button2)        
        self._model.addButton(self._button3)        
        self._model.addButton(self._button4)
        self._model.addButton(self._button5)
        # add other buttons (up to 3 more) if needed
        
        # Add any timer you have.
        # self._model.addTimer(self._timer)
        
        # Now add all the transitions that are supported by my Model
        # obvously you only have BTN1_PRESS through BTN4_PRESS
        # BTN1_RELEASE through BTN4_RELEASE
        # and TIMEOUT
        
        # some examples:
        self._model.addTransition(0, [BTN1_PRESS], 1)
        self._model.addTransition(1, [BTN1_RELEASE], 0)

        self._model.addTransition(0, [BTN5_PRESS], 9)
        self._model.addTransition(9, [NO_EVENT], 0)

        self._model.addTransition(0, [BTN2_PRESS], 2)
        self._model.addTransition(2, [BTN2_RELEASE], 0)

        self._model.addTransition(0, [BTN3_PRESS], 3)
        self._model.addTransition(3, [BTN3_RELEASE], 0)

        self._model.addTransition(0, [BTN4_PRESS], 4)
        self._model.addTransition(4, [BTN4_RELEASE], 0)

        self._model.addTransition(1, [BTN2_PRESS], 5)
        self._model.addTransition(5, [BTN2_RELEASE], 1)

        self._model.addTransition(2, [BTN1_PRESS], 5)
        self._model.addTransition(5, [BTN1_RELEASE], 2)

        self._model.addTransition(2, [BTN3_PRESS], 6)
        self._model.addTransition(6, [BTN3_RELEASE], 2)

        self._model.addTransition(3, [BTN2_PRESS], 6)
        self._model.addTransition(6, [BTN2_RELEASE], 3)

        self._model.addTransition(3, [BTN4_PRESS], 7)
        self._model.addTransition(6, [BTN4_RELEASE], 7)

        self._model.addTransition(4, [BTN3_PRESS], 7)
        self._model.addTransition(7, [BTN3_RELEASE], 4)

        self._model.addTransition(1, [BTN4_PRESS], 8)
        self._model.addTransition(8, [BTN4_RELEASE], 1)

        self._model.addTransition(4, [BTN1_PRESS], 8)
        self._model.addTransition(8, [BTN1_RELEASE], 4)


        # etc.

    def changeInstrument(self):
        if self._instrumentno == 0:
            Log.d('Violin Playing')
            instrumentName = self.instruments[self._instrumentno]
            self._display.showText(f"{instrumentName}", 0, 5)
            self._instrument = Violin()
            self._instrumentno = 1
        elif self._instrumentno == 1:
            Log.d('Bass Playing')
            instrumentName = self.instruments[self._instrumentno]
            self._display.showText(f"{instrumentName}", 0, 5)
            self._instrument = Bass()
            self._instrumentno = 2
        else:
            Log.d('Organ Playing')
            instrumentName = self.instruments[self._instrumentno]
            self._display.showText(f"{instrumentName}", 0, 5)
            self._instrument = Organ()
            self._instrumentno = 0


    """
    Create a run() method - you can call it anything you want really, but
    this is what you will need to call from main.py or someplace to start
    the state model.
    """

    def run(self):
        # The run method should simply do any initializations (if needed)
        # and then call the model's run method.
        # You can send a delay as a parameter if you want something other
        # than the default 0.1s. e.g.,  self._model.run(0.25)
        self._model.run()

    """
    stateDo - the method that handles the do/actions for each state
    """
    def stateDo(self, state):
        # Now if you want to do different things for each state you can do it:
        pass

    """
    stateEntered - is the handler for performing entry/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    """
    def stateEntered(self, state, event):
        # Again if statements to do whatever entry/actions you need
        Log.d(f'State {state} entered')
        if state == 0:
            # entry actions for state 0q
            pass
        
        elif state == 1:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(0))
            self._display.showText('DO ', 1, 7)
            self._lights.setColor(WHITE, 8)
        elif state == 2:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(1))
            self._display.showText('RE ', 1, 7)
            self._lights.setColor(RED, 8)
        elif state == 3:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(2))
            self._display.showText('MI ', 1, 7)
            self._lights.setColor(YELLOW, 8)
        elif state == 4:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(3))
            self._display.showText('FA ', 1, 7)
            self._lights.setColor(BLUE, 8)
        elif state == 5:
            # entry actions for state 1
            self._lights.off()
            self._buzzer.play(self._instrument.getNote(4))
            self._display.showText('SO ', 1, 7)
            self._lights.setColor(self.PINK, 8)

        elif state == 6:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(5))
            self._display.showText('LA ', 1, 7)
            self._lights.setColor(ORANGE, 8)
        elif state == 7:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(6))
            self._display.showText('TI ', 1, 7)
            self._lights.setColor(GREEN, 8)
        elif state == 8:
            # entry actions for state 1
            self._buzzer.play(self._instrument.getNote(7))
            self._display.showText('DO2', 1, 7)
            self._lights.setColor(CYAN, 8)
        elif state == 9:
            self.changeInstrument()
            
    """
    stateLeft - is the handler for performing exit/actions
    You get the state number of the state that just entered
    Make sure actions here are quick
    
    This is just like stateEntered, perform only exit/actions here
    """

    def stateLeft(self, state, event):
        Log.d(f'State {state} exited')
        if state >=1 and state <=8:
            # exit actions for state 0
            self._buzzer.stop()
            self._display.showText(' '* 16, 1, 0)
            self._lights.off()
        # etc.
    
