from microbit import *
import radio

radio.on()
radio.config(channel=19)
while True:
    if button_a.was_pressed():
        radio.send('smile')
    elif button_b.was_pressed():
        radio.send('frown')
