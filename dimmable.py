from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)

led = PWMLED(18)

while True:
	brightness = (rotor.steps / 180) ** 2 
	led.value = brightness
	print(brightness)
