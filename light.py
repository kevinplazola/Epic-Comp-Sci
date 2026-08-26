from gpiozero import LED
from signal import pause

yellow = LED(18)

yellow.blink()

pause()
