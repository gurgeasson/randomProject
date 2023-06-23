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
    global reference_hit
    if (time.time() - 5) < reference_hit < time.time():
        print('random_engine starts, does not much at this point')
        # wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
        GPIO.wait_for_edge(gpio_my_pin, GPIO.RISING, timeout=3000, bouncetime=200)
        random_hit = time.time() # Store the current time stamp
        delta_time = random_hit - reference_hit # Calculate elapsed time from reference_hit to random_hit, and call taht my random number
        print (f'{delta_time} : {time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}') # prints the random number to the terminal
        time.sleep(5)
    else:
        # wait for up to 30 seconds for a rising edge (timeout is in milliseconds)
        GPIO.wait_for_edge(gpio_my_pin, GPIO.RISING, timeout=3000, bouncetime=200)
        reference_hit = time.time()
        print('set reference_hit')
# main
#
# i'm not sure if I need any of the following any more
# I need a while loop to get in a loop and run the show. It should limit the frequency a random number is generated: just use sleep.
# Call random_engine function, than go to sleep --> repeat

while True:
    random_engine()
