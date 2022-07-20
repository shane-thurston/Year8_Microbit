# Imports go at the top
from microbit import *
import radio

# Code in a 'while True:' loop repeats forever
radio.on()
radio.config(group=1,power=0)

while True:
    msg = radio.receive()
    if msg == "becon":
        display.show(Image.HEART_SMALL)
        sleep(50)
        display.clear()
