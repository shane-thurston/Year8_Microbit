# Imports go at the top
from microbit import *
import radio

# Code in a 'while True:' loop repeats forever
radio.on()
radio.config(group=1,power=0)

while True:
    display.show("A")
    radio.send("becon")
    sleep(200)
    display.clear()
    sleep(200)
