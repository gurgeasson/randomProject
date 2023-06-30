#! /usr/bin/python

# This program interfaces with a radiation counter and rounts the hits per minute.
# I'm connecting to the INT2 pin on the radiation conunter. It's normaly low.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

import time # needed timestamp
import RPi.GPIO as GPIO # needed to access the GPIO pins
import thingSpeakPublish # import thingSpeakPublish

# initialising wariables
gpio_my_pin = 12 # the GPIO pin I'm connecting to the counter
time_reference = time.time() # where count starts in time
current_time = 0 # initialise current time
count = 0 # radiation rolling count
own_background = 12 # the j305 geiger tube according to it's datasheet, has a 0,2 CPS own background radiation ==> 12 CPM
adjusted_CPM = 0 # the real and final count CPM

# set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

# while the timer() runs, a callback function takes care of listening to GPIO_12 and updating the count variable
def hit_callback(channel):
    global count
    count += 1

GPIO.add_event_detect(gpio_my_pin, GPIO.RISING, callback=hit_callback)  # add rising edge detection on channel 12

# calc_CPM() function calculates and adjusts CPM
def calc_CPM():
    global count
    global own_background
    global current_time
    global adjusted_CPM
    raw_CPM = round(count / 15) # The measurement is over 15 mins, so to calculate CPM I need to dived by the minutes. Also round to nearest whole
    adjusted_CPM = raw_CPM - own_background # adjust for the tubes own background radiation
    print(f'the radiaton count at {current_time} since epoch is {adjusted_CPM} CountsPerMinute')
    count = 0 # reset counter

# timer() function keeps track of time and triggers some events every 900 seconds 1/4 hours.
def timer():
    global time_reference
    global current_time
    current_time = time.time()
    if (time_reference + 900) <= current_time: # if 900 seconds passed
        time_reference = current_time # update time_reference to currant_time
        calc_CPM() # call function
        thingSpeakPublish.thinSpeakWrite(adjusted_CPM) # from thingSpeakPublish.py

while True:
    timer() # call function
