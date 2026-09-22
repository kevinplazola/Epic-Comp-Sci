import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED
from signal import pause

sensor = adafruit_dht.DHT11(board.D25)
red = LED(18)
blue = LED(16)
		
print("time,celsius,fahrenheit")

def to_fahrenheit(c):
	f = (c * (9/5)) + 32
	return f

while True:
	try:
		celsius = sensor.temperature
		fahrenheit = to_fahrenheit(celsius)
		current_time = datetime.now()
		print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
		if fahrenheit > 72:
			red.blink()
			time.sleep(3.0)
		if fahrenheit < 72:
			blue.blink()
			time.sleep(3.0)
		lines = ["{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit)]
		with open("temperature.csv", "a") as f:
			f.write("\n".join(lines) + "\n")
	except RuntimeError as error:
		print(error.args[0])
		time.sleep(2.0)
		continue
	except Exception as error:
		sensor.exit()
		raise error    
	