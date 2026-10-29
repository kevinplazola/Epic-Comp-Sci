from gpiozero import Button
from gpiozero import LED
from signal import pause
import tm1637
import random
import time

green = LED(18)
button = Button(4)
display = tm1637.TM1637(clk=5, dio=6)

class SlotMachine:
    def __init__(self, display, led, button):
        self.display = display
        self.led = led
        self.button = button
        self.button.when_pressed = self.play_game
        self.button.when_held = self.rigged_spin
        self.button.hold_time = 2.0
        self.is_playing = False

        self.is_rigged = False
        self.win_chance = 0.9
        self.jackpots = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]

    def rigged_spin(self):
        self.is_rigged = not self.is_rigged
        print("Slot Machine is rigged")

    def play_game(self):
        if self.is_playing:
            return

        self.is_playing = True
        self.display.scroll("Ready to play  ", delay=250)
        time.sleep(0.5)

        winning_numbers = self.determine_outcome()

        self.display.show(f"{winning_numbers:04d}")
        time.sleep(0.5)
        
        self.check_winner(winning_numbers)
        self.is_playing = False
    
    def determine_outcome(self):
        roll = random.random()
        if self.is_rigged and roll < self.win_chance:
            return random.choice(self.jackpots)
        elif not self.is_rigged and roll < 0.1:
            return random.choice(self.jackpots)
        else:
            number = random.randint(1111, 9999)
            while number in self.jackpots:
                number = random.randint(1111, 9999)
            return number
    def check_winner(self, winning_numbers):
        if winning_numbers in self.jackpots:
            self.display.scroll("WINNER  ", delay=250)
            self.led.blink(on_time=0.5, off_time=0.5, n=5, background=False)
        else:
            self.display.show("LOSE")
            time.sleep(1.0)

machine = SlotMachine(display, green, button)

pause()