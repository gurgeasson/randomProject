#! /usr/bin/python

from math import pow
import time
import RPi.GPIO as GPIO

gpio_my_pin = 4
reference_hit = None
random_hit = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

while True: # While loop to keep the program running indefinitely.
	if  reference_hit < (time.time - 60): # If my reference_hit time is not out of range
		if GPIO.input(gpio_my_pin) == True: # If the geiger counter signal is high
			random_hit = time.time() # Store the current time stamp
			delta_time = random_hit - reference_hit # Calculate elapsed time from reference_hit to random_hit, and call taht my random number
			# duration = str(duration)
			# duration = duration.replace(".","") # removes the decimal point from the value
			# duration = int(duration)
			# duration = int(pow(duration, 20)) # Performs a raise on the value by a power of 20
			print (delta_time) # prints the random number to the terminal
			# reference_hit = time.time()
			time.sleep(60) # I don't want too may numbers, wait for a min before the next one
	else:
		if GPIO.input(gpio_my_pin) == True: # AKA If the geiger counter signal is high
			reference_hit = time.time()