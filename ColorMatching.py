import time
import random
from LightStrip import LightStrip, BLUE, RED, YELLOW, WHITE, BLACK
from Button import Button
from Displays import LCDDisplay
from StateModel import StateModel, BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS, TIMEOUT
from Counters import SoftwareTimer
from Melody import *
from Buzzer import PassiveBuzzer

buzzer_pin = 17  # Adjust the pin as needed


class GameField:
    def __init__(self, color=None):
        if color:
            self._color = color
        else:
            c = random.randint(1, 4)
            self._color = RED if c == 1 else YELLOW if c == 2 else BLUE if c == 3 else WHITE
        print(f"Initialized GameField with color: {self._color}")

    def getColor(self):
        return self._color

class Matching:
    def __init__(self, size=8):
        self._size = size
        self._field = [GameField() for _ in range(size)]
        self._lights = LightStrip(pin=20, numleds=size, brightness=1)
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [
            Button(22, 'white', buttonhandler=None),
            Button(14, 'red', buttonhandler=None),
            Button(16, 'yellow', buttonhandler=None),
            Button(13, 'blue', buttonhandler=None)
        ]
        self._playing = False
        self._score = 0
        self._melody = Melody(buzzer_pin)
        self._buz = PassiveBuzzer(buzzer_pin)

        # Initialize the state model
        self._model = StateModel(4, self, debug=True)
        for button in self._buttons:
            self._model.addButton(button)
        self._timer = SoftwareTimer(None)
        self._model.addTimer(self._timer)

        # Define transitions
        self._model.addTransition(0, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 1)
        self._model.addTransition(1, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 2)
        self._model.addTransition(2, [TIMEOUT], 1)
        self._model.addTransition(1, [TIMEOUT], 3)
        self._model.addTransition(3, [BTN1_PRESS, BTN2_PRESS, BTN3_PRESS, BTN4_PRESS], 0)

        # Run the state model
        self._model.run()

    def reset_game_field(self):
        self._field = [GameField() for _ in range(self._size)]
        self._score = 0

    def stateDo(self, state):
        print(f"Executing stateDo for state {state}")
        if state == 0:
            self._melody.play_melody(zelda_melody)
        elif state == 3:
            self._melody.play_melody(zeldas_lullaby)

    def stateEntered(self, state, event):
        print(f"Entering state {state} due to event {event}")
        if state == 0:
            self._display.showText(" Color Matching ", 0, 0)
            self._display.showText("Press any button", 1, 0)
        elif state == 1:
            self.refresh()
            self._display.showText(' ' * 16, 1, 0)  # Clear display
            self._playing = True
            self.check_game_over()  # Check if the game is over when entering state 1
        elif state == 2:
            self.check_match(event)
            self._model.gotoState(1)  # Return to game play state after checking match
        elif state == 3:
            self._playing = False
            self._display.showText('   GAME OVER!   ', 1, 0)
            time.sleep(3)
            self._lights.run(2)  # Run light animation

    def stateLeft(self, state, event):
        print(f"Exiting state {state} due to event {event}")
        if state == 0:
            self._melody.stop()  # Stop the melody if the state is exited
        elif state == 3:
            self._melody.stop()
            self.reset_game_field()
            self._lights.off()

    def check_match(self, event):
        color = None
        if event == BTN1_PRESS:
            color = WHITE
        elif event == BTN2_PRESS:
            color = RED
        elif event == BTN3_PRESS:
            color = YELLOW
        elif event == BTN4_PRESS:
            color = BLUE

        print(f"Checking for match with color: {color}")
        field_colors = [base.getColor() for base in self._field]
        print(f"Field colors: {field_colors}")

        matched_indices = []
        for i in range(len(field_colors) - 1):
            if field_colors[i] == color and field_colors[i + 1] == color:
                matched_indices.append(i)
                matched_indices.append(i + 1)

        if field_colors[0] == color and field_colors[-1] == color:
            matched_indices.append(0)
            matched_indices.append(len(field_colors) - 1)

        matched_indices = sorted(set(matched_indices))  # Remove duplicates and sort
        print(f"Matched indices: {matched_indices}")

        if matched_indices:
            for index in matched_indices:
                self._lights.setPixel(index, color)
                time.sleep(0.05)
                self._lights.setPixel(index, BLACK)
            self._buz.play(200)
            for index in reversed(matched_indices):
                self._field.pop(index)
                self._field.insert(0, GameField())
            time.sleep(0.2)
            self._buz.stop()
            self._score += 1
            self._display.showText(f'   Score: {self._score:02d}    ', 0, 0)
            print(f"Match found. Score: {self._score}")
            self.refresh()
        else:
            self._buz.play(600)
            time.sleep(0.2)
            self._buz.stop()
            print("No match found.")

    def check_game_over(self):
        field_colors = [base.getColor() for base in self._field]
        print(f"Checking game over with field colors: {field_colors}")
        possible_matches = False

        for i in range(len(field_colors) - 1):
            if field_colors[i] == field_colors[i + 1]:
                possible_matches = True
                break

        if field_colors[0] == field_colors[-1]:
            possible_matches = True

        if not possible_matches:
            print("No possible matches. Game over!")
            self._model.gotoState(3)
        else:
            print("Possible matches remain. Game continues.")

    def refresh(self):
        print("Refreshing the display.")
        for x in range(len(self._field)):
            base = self._field[x]
            if base is not None:
                self._lights.setPixel(x, base.getColor(), show=False)
        self._lights.show()
        print("Display refreshed.")

if __name__ == '__main__':
    game = Matching()
    game.refresh()
    while True:
        time.sleep(0.1)
        game._model.run()

