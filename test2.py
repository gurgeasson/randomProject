#! /usr/bin/python

# in previous attampts it proved that I can connect to the radiation counter
# I also proved that I can generate random numbers
# now I want to see it I can do it with GPIO.wait_for_edge

# I'm connecting to the INT2 pin on the radiation conunter.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

import time
import RPi.GPIO as GPIO

gpio_my_pin = 12
reference_hit = 0
random_hit = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

# random_engine function
# I need a function to generate the random numbers

def random_engine():
    print('random_engine starts, does not much at this point')
    GPIO.wait_for_edge(gpio_my_pin, GPIO.RISING)
    print('waiting for edge seem to work')

# main
# I need a while loop to get in a loop and run the show. It should limit the frequency a random number is generated: just use sleep.
# Call random_engine function, than go to sleep --> repeat

while True:
    random_engine()
    time.sleep(5)