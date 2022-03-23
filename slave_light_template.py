from microbit import *
import radio

radio.on()
radio.config(channel=13)
msg = ''

while True:
    msg = radio.receive()
    if msg == 'green':
        #green light on, all other lights off
    if msg == 'yellow':
        #yellow light on, all other lights off
    if msg == 'red':
        #red light on, all other lights off
