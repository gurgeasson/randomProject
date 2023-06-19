#! /usr/bin/python

# print('hello world')

try:
    import time # load time module for sleep
except RuntimeError:
    print("Error importing time! This is probably because you need superuser privileges. Maybe try 'sudo'")
try:
    import RPi.GPIO as GPIO # load RPi.GPIO module. I need it to have access to the GPIO pins.
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Maybe try 'sudo'")

GPIO.setmode(GPIO.BCM) # I want to address the pins by the BCM number and not by the board number.
# print(GPIO.getmode())
gpio_my_pin = 4 # creatr a variable to store the GPIO pin number that the signal is attached to
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to accept input from radiation counter
# print(GPIO.input(gpio_my_pin))

while True:
    print('looping')
    time.sleep(1)
    print(GPIO.input(gpio_my_pin))


# GPIO.cleanup()
