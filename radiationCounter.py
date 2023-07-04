#! /usr/bin/python

###   Description   ###
# This program interfaces with a radiation counter and rounts the hits per minute.
# I'm connecting to the INT2 pin on the radiation conunter. It's normaly low.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

###   Import Modules and .py Scripts   ###
import time # needed timestamp
import RPi.GPIO as GPIO # needed to access the GPIO pins
import thingSpeakPublish # import thingSpeakPublish

###   Global Variables   ###
gpio_my_pin = 12 # the GPIO pin I'm connecting to the counter
time_reference = time.time() # when count starts in time
current_time = 0 # initialise current time
count = 0 # radiation rolling count
adjusted_CPM = 0 # the real and final count CPM

###   set up GPIO pins   ###
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.
# while the timer() runs, a callback function takes care of listening to gpio_my_pin and updating the count variable
def hit_callback(channel):
    global count
    count += 1
GPIO.add_event_detect(gpio_my_pin, GPIO.RISING, callback=hit_callback)  # add rising edge detection.

###   Function Definitions   ###
def calc_CPM(): # calc_CPM() function calculates and adjusts CPM
    global count
    global current_time
    global adjusted_CPM
    raw_CPM = round(count / 15) # The measurement is over 15 mins, so to calculate CPM I need to dived by the minutes. Also round to nearest whole
    adjusted_CPM = raw_CPM - 12 # the j305 geiger tube according to it's datasheet, has a 0,2 CPS own background radiation ==> 12 CPM
    print(f'the radiaton count at {current_time} since epoch is {adjusted_CPM} CountsPerMinute')
    count = 0 # reset counter

def timer(): # timer() function keeps track of time and triggers some events every 900 seconds 15 mins.
    global time_reference
    global current_time
    current_time = time.time()
    if (time_reference + 900) <= current_time: # if 900 seconds passed (15 mins)
        time_reference += 900 # update time_reference to currant_time.
        try:
            calc_CPM() # call function
        except KeyboardInterrupt:
            print('keyboard interrupt while calculating CPM')
            GPIO.cleanup() # clean up GPIO on CTRL+C exit
        except Exception as e:
            print (e)
            GPIO.cleanup() # clean up GPIO on Exception
        try:
            thingSpeakPublish.thinSpeakWrite(adjusted_CPM) # from thingSpeakPublish.py
        except KeyboardInterrupt:
            print('keyboard interrupt while publishing to thigSpeak')
            GPIO.cleanup() # clean up GPIO on CTRL+C exit
        except Exception as e:
            print (e)
            GPIO.cleanup() # clean up GPIO on Exception

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
