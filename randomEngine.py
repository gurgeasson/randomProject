#! /usr/bin/python

###   Description   ###
# This program interfaces with a radiation counter and generates random numbers from the detected signal.
# I'm connecting to the INT pin on the radiation conunter. It's normaly HIGH.
# I'm using BOARD pin 16 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

# The raw random number (float) is the elapsed time between radiation events in seconds.
# I convert this to a intiger from 1 to 6 to represent 6 sided dice rolls.
# I have plans to generate these numbers for a couble of days, and than analise the randomness of the rolls.

###   Import Modules and .py Scripts   ###
import time # needed for sleep and for timestamp
import math
import RPi.GPIO as GPIO # needed to access the GPIO pins

###   Global Variables   ###
gpio_my_pin = 16 # the GPIO pin I'm connecting to the counter
time_reference = time.time()
reference_hit = 0
random_hit = 0
dice_roll = 0

###   set up GPIO pins   ###
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Input pin, accepts pullups from Radiation Counter.

###   Function Definitions   #### random_engine function --> generating true random numbers
def random_engine():
    global time_reference
    global reference_hit
    global dice_roll
    delta_time
    # wait for up to 60 seconds for a rising edge (timeout is in milliseconds)
    if GPIO.wait_for_edge(gpio_my_pin, GPIO.FALLING, timeout=6000, bouncetime=200) is None:
        time_reference += 60
        return
    else:
        second_hit_time = time.time() # Store the current time stamp
        delta_time = second_hit_time - reference_hit # Calculate elapsed time from reference_hit to random_hit, and call that my random number
        conversion_factor = 100 / 6
        dice_roll = math.ceil(((delta_time ** 9) % 1 * 100) / conversion_factor)
        print (f'{dice_roll} : {time.strftime("%Y %b %d %H:%M:%S", time.gmtime())}') # prints the random number to the terminal

def timer(): # timer() function keeps track of time and triggers some events every 60 seconds.
        global time_reference
        global dice_roll
        current_time = time.time()
        if (time_reference + 60) <= current_time: # if 60 seconds passed
            # wait for up to 60 seconds for a rising edge (timeout is in milliseconds)
            if GPIO.wait_for_edge(gpio_my_pin, GPIO.FALLING, timeout=6000, bouncetime=200) is None:
                time_reference += 60
                return
            else:
                time_reference += 60 # update time_reference.
                try:
                    random_engine() # call function
                except KeyboardInterrupt:
                    print('keyboard interrupt while calculating random number')
                    GPIO.cleanup() # clean up GPIO on CTRL+C exit
                except Exception as e:
                    print (e)
                    GPIO.cleanup() # clean up GPIO on Exception
        
                human_current_time = time.strftime('%H:%M:%S - %Y/%b/%d', time.localtime()) # generate time
                file = open('/var/www/html/randomProject/list.html', 'at') # open list.html, 'at' - Append and Text mode
                file.write(f'{dice_roll}, {human_current_time} </br>') # append random number and time it was created
                file.close()
                # time.sleep(29) # no point cheching time in the next 29 secs.

###   Main Loop   ###
while True:
    try:
        timer() # call function
    except KeyboardInterrupt:
        print('keyboard interrupt while running timer()')
        GPIO.cleanup() # clean up GPIO on CTRL+C exit
    except Exception as e:
        print (e)
        GPIO.cleanup() # clean up GPIO on Exception

# GPIO.cleanup() # clean up GPIO on normal exit