from microbit import *
import radio

radio.on()
radio.config(channel=19)
while True:
    message = radio.receive()
    if message == "smile":
        display.show(Image.HAPPY)
        sleep(500)
    elif message == 'frown':
        display.show(Image.SAD)
        sleep(500)
    display.clear()
