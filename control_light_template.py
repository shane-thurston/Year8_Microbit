from microbit import *
import radio

radio.on()
radio.config(channel=13)
#send msg to slave to turn on red light
while True:
    #green light on, other lights off
    sleep(10000)
    #green light off, yellow on
    sleep(3000)
    #yellow off, red light on
    sleep(2000)
    #send msg to slave to turn green light on
    sleep(10000)
    #send msg to slave to turn yellow light on
    sleep(3000)
    #send msg to slave to turn red light on
    sleep(2000)
