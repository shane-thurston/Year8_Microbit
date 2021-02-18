from microbit import *
while True:
  if button_a.is_pressed():
    display.show(Image.HAPPY)
    sleep(500)
    display.show(Image.MEH)
    sleep(500)
  else:
    display.show(Image.SAD)
