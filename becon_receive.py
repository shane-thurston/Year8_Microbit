# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(group=1,power=0)

# Code in a 'while True:' loop repeats forever
while True:
    msg = radio.receive()
    if msg == "becon":
        display.show(Image.HEART_SMALL)
        sleep(50)
        display.clear()
