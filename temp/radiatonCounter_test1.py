#! /usr/bin/python

# This program interfaces with a radiation counter and rounts the hits per minute.
# I'm connecting to the INT2 pin on the radiation conunter. It's normaly low.
# I'm using BOARD pin 12 on the raspberry pi
# A logic level converter takes care of the 3.3v <--> 5v conversion between counter and pi

import time # needed timestamp
import RPi.GPIO as GPIO # needed to access the GPIO pins

# initialising wariables
gpio_my_pin = 12 # the GPIO pin I'm connecting to the counter
time_reference = time.time()
count = 0
own_background = 12 # the j305 geiger tube according to it's datasheet, has a 0,2 PPS own background radiation ==> 12 PPM

# set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Input pin, accepts pullups from Radiation Counter.

# while the timer() runs, a callback function takes care of listening to GPIO_12 and updating the count variable
def hit_callback(channel):
    global count
    count += 1

GPIO.add_event_detect(gpio_my_pin, GPIO.RISING, callback=hit_callback)  # add rising edge detection on a channel

# time function --> keeps track of time and triggers every 60 seconds and prints out the radiation PPM
def timer():
    global time_reference
    global count
    global own_background
    current_time = time.time()
    if (time_reference + 60) <= current_time:
        time_reference = current_time # 
        adjusted_PPM = count - own_background
        print(f'the radiaton count at {current_time} since epoch is {adjusted_PPM} PulsePerMinute')
        count = 0 # reset counter

while True:
    timer()
