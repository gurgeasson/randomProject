#! /usr/bin/python

# This program interfaces with a radiation counter and generates random numbers from the detected signal.
# I'm connecting to the INT2 pin on the radiation conunter. It's normaly low.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

# For now the random number is the elapsed time as a float between radiation hits in seconds
# In future I would like to refine that

import time # needed for sleep and for timestamp
import RPi.GPIO as GPIO # needed to access the GPIO pins

gpio_my_pin = 12 # the GPIO pin I'm connecting to the counter
# initialising wariables
reference_hit = 0
random_hit = 0

# set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

# random_engine function --> generating true random numbers
# checks if the reference_hit time stamp is within 5 seconds, mostly to keep the first generated number value within reason
def random_engine():
    global reference_hit
    if (time.time() - 5) < reference_hit < time.time():
        # print('random_engine starts, does not much at this point')
        # wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
        GPIO.wait_for_edge(gpio_my_pin, GPIO.RISING, timeout=3000, bouncetime=200)
        random_hit = time.time() # Store the current time stamp
        delta_time = random_hit - reference_hit # Calculate elapsed time from reference_hit to random_hit, and call taht my random number
        # print (f'{delta_time} : {time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}') # prints the random number to the terminal
        current_time = time.strftime("%H:%M:%S", time.localtime()) # generate time
        file = open('/var/www/html/randomProject/list.html', 'at') # open list.html, 'at' - Append and Text mode
        file.write(f'{delta_time} {current_time} </br>') # append random number and time it was created
        file.close()
        time.sleep(3600) # wait for an hour. It will yield about 24 numbers a day.
    else:
        # wait for up to 30 seconds for a rising edge (timeout is in milliseconds)
        GPIO.wait_for_edge(gpio_my_pin, GPIO.RISING, timeout=3000, bouncetime=200)
        reference_hit = time.time()
        print('set reference_hit')

# main
#
# i'm not sure if I need any of the following any more, I could just wrap the functions code in a while loop...
try:
    while True:
        random_engine()
except KeyboardInterrupt:
    GPIO.cleanup()