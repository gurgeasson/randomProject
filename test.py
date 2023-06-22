from math import pow
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN) # This is connected to the pin on the Geiger counter which outputs 3v when it blips.
firstBlip = 0
secondBlip = 0
while True: # While loop to keep the program running indefinitely.
	if GPIO.input(12) == True: # AKA If the geiger counter blips
		secondBlip = time.time() # Record the time of the blip into the variable called secondBlip
		duration = secondBlip - firstBlip #stores the elapsed time between blips into the duration variable
		# duration = str(duration)
		# duration = duration.replace(".","") # removes the decimal point from the value
		# duration = int(duration)
		# duration = int(pow(duration, 20)) # Performs a raise on the value by a power of 20
		print (duration) # prints the large number to the terminal
		secondBlip = 0
		firstBlip = time.time()
