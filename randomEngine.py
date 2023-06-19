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
gpio_my_pin = 4 # create a variable to store the GPIO pin number that the signal is attached to
GPIO.setup(gpio_my_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set pin to accept input from radiation counter
# print(GPIO.input(gpio_my_pin))

while True:
    try:
        # wait for falling edge, store time in varable
        # wait for rising edge, divide time from time variable...
        # is this my random number? should I use it as a seed for shiftxor???
        # store my random number in list.html
        # sleep for about a minute??? half an hour??? to limit the number of random number entries 
        GPIO.wait_for_edge(gpio_my_pin, GPIO.FALLING)
        current_time = time.strftime("%H:%M:%S", time.localtime()) # generate time
        file = open('/var/www/html/randomProject/list.html', 'at') # open list.html, 'at' - Append and Text mode
        file.write(f'{GPIO.input(gpio_my_pin)} {current_time} </br>')
        file.close()
    except KeyboardInterrupt:
        GPIO.cleanup()       # clean up GPIO on CTRL+C exit
    GPIO.cleanup()           # clean up GPIO on normal exit

# while True:
#     # print('looping')
#     # time.sleep(30)
#     # print(GPIO.input(gpio_my_pin))

#     current_time = time.strftime("%H:%M:%S", time.localtime()) # generate time

#     # testing if I can add new entries as a list to my list.html.
#     # at the moment it is only the state of gpio_my_pin, and not a random number.
#     # later it will need to be database... actually just a text file.
#     # also I want the page automaticaly update every time I get a new random number.
#     file = open('/var/www/html/randomProject/list.html', 'at')
#     file.write(f'{GPIO.input(gpio_my_pin)} {current_time} </br>')
#     file.close()
    
#     time.sleep(30)

# GPIO.cleanup()
