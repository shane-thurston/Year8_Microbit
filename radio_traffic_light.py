from microbit import *
import radio

radio.on()
radio.config(channel=19)
while True:
  message = radio.receive()
  if message == "cross":
    # Green light off
    # sleep
    # Yellow light on
    # sleep
    # Yellow light off
    # sleep
    # Red light on
    # sleep
    # Red light off
  else:
    # Green light on
