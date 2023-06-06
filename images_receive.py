from microbit import *
import radio

radio.on()
radio.config(channel=9)

images_dict = {"yes":Image.YES,
              "no":Image.NO,
              "meh":Image.MEH,
              "sad":Image.SAD}

while True:
    message = radio.receive()
    msg_string = str(message)
    msg_string = msg_string.split()
    if len(msg_string) == 2:
        image = images_dict[msg_string[0]]
        display.show(image)
        sleep(500)
        image2 = images_dict[msg_string[1]]
        display.show(image2)
        sleep(500)

    display.clear()
