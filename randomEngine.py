# print('hello world')

# load RPi.GPIO module. I need it to have access to the GPIO pins.
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Maybe try 'sudo'")
# I want to address the pins by the board number and not by the chip pin number.
GPIO.setmode(GPIO.BOARD)
# print(GPIO.getmode())
gpio_pin_7=7 # give a nive name to the GPIO pin the signal is attached to
# set pin to accept input from radiation counter
GPIO.setup(gpio_pin_7, GPIO.IN)
# print(GPIO.input(gpio_pin_7))

while True:
    print('looping')




# GPIO.cleanup()