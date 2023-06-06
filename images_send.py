from microbit import *
import radio

radio.on()
radio.config(channel=9)

while True:
    if button_a.was_pressed():
        radio.send('yes no')
