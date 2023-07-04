#! /usr/bin/python

###   Description   ###
# This program interfaces with a radiation counter and generates random numbers from the detected signal.
# I'm connecting to the INT pin on the radiation conunter. It's normaly HIGH.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

# The raw random number (float) is the elapsed time between radiation events in seconds.
# I convert this to a intiger from 1 to 6 to represent 6 sided dice rolls.
# I have plans to generate these numbers for a couble of days, and than analise the randomness of the rolls.

###   Import Modules and .py Scripts   ###
import time # needed for sleep and for timestamp
import math
import RPi.GPIO as GPIO # needed to access the GPIO pins

###   Global Variables   ###
gpio_my_pin = 12 # the GPIO pin I'm connecting to the counter
time_reference = time.time()
hit_time_reference = 0
dice_roll = 0

###   set up GPIO pins   ###
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

# while the timer() runs, a callback function takes care of listening to gpio_my_pin and updating the count variable
def hit_callback(channel):
    global time_reference
    if hit_time_reference != 0:
        delta_time = time.time() - time_reference # Calculate elapsed time from reference_hit to now, and call that my random number
        conversion_factor = 100 / 6
        dice_roll = math.ceil(((delta_time ** 9) % 1 * 100) / conversion_factor)
        print (f'{dice_roll}, {time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}') # prints the random number to the terminal
    else:
        hit_time_reference = time.time()

GPIO.add_event_detect(gpio_my_pin, GPIO.RISING, callback=hit_callback)  # add rising edge detection.

###   Function Definitions   ####
def write_to_file(): # write my date into the list.html file
    global dice_roll
    human_current_time = time.strftime("%Y %b %d %H:%M:%S", time.localtime()) # generate time
    file = open('/var/www/html/randomProject/list.html', 'at') # open list.html, 'at' - Append and Text mode
    file.write(f'{dice_roll}, {human_current_time} </br>') # append random number and time it was created
    file.close()

def timer(): # timer() function keeps track of time and triggers some events every 60 seconds.
        global time_reference
        if (time_reference + 60) <= time.time(): # if 60 seconds passed
            write_to_file()
            time_reference += 60

###   Main Loop   ###
while True:
    try:
        timer() # call function
    except KeyboardInterrupt:
        print('keyboard interrupt while running timer()')
        GPIO.cleanup() # clean up GPIO on CTRL+C exit
        exit()

# GPIO.cleanup() # clean up GPIO on normal exit
