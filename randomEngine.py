#! /usr/bin/python

# print('hello world')

try:
    import time # load time module for sleep
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Maybe try 'sudo'")
try:
    import RPi.GPIO as GPIO # load RPi.GPIO module. I need it to have access to the GPIO pins.
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Maybe try 'sudo'")

GPIO.setmode(GPIO.BOARD) # I want to address the pins by the board number and not by the chip pin number.
# print(GPIO.getmode())
gpio_pin_7=7 # give a nive name to the GPIO pin the signal is attached to
GPIO.setup(gpio_pin_7, GPIO.IN) # set pin to accept input from radiation counter
# print(GPIO.input(gpio_pin_7))

while True:
    print('looping')
    time.sleep(3)
    print(GPIO.input(gpio_pin_7))


# GPIO.cleanup()