#! /usr/bin/python

from math import pow
import time
import RPi.GPIO as GPIO

gpio_my_pin = 12
reference_hit = 0
random_hit = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

while True: # While loop to keep the program running indefinitely.
	if (time.time() - 3) < reference_hit < time.time(): # If my reference_hit time is not out of range
		print('reference_hit in range')

		while True:
			do_things()

		if GPIO.input(gpio_my_pin) == True: # If the geiger counter signal is high
			random_hit = time.time() # Store the current time stamp
			delta_time = random_hit - reference_hit # Calculate elapsed time from reference_hit to random_hit, and call taht my random number
			# duration = str(duration)
			# duration = duration.replace(".","") # removes the decimal point from the value
			# duration = int(duration)
			# duration = int(pow(duration, 20)) # Performs a raise on the value by a power of 20
			print (f'{delta_time} : {time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}') # prints the random number to the terminal
			time.sleep(3) # I don't want too may numbers, wait for a min before the next one
			# reference_hit = time.time()
	else:
		if GPIO.input(gpio_my_pin) == True: # AKA If the geiger counter signal is high
			reference_hit = time.time()
			print('set reference_hit')
