from microbit import *
while True:
    #red light on
    if button_a.was_pressed():
        #red light off
        sleep(500)
        #orange light on
        sleep(500)
        #orange light off
        sleep(500)
        #green light on
        sleep(2000)
        #green light off
        sleep(500)
