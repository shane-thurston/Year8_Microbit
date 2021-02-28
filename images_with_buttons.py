from microbit import *
while True:
  if button_a.is_pressed():
    display.show(Image.HAPPY)
    sleep(500)
    display.show(Image.MEH)
    sleep(500)
  elif button_b.is_pressed():
    display.show(Image.CLOCK12)
    sleep(300)
    display.show(Image.CLOCK3)
    sleep(300)
    display.show(Image.CLOCK6)
    sleep(300)
    display.show(Image.CLOCK9)
    sleep(300)
  else:
    display.show(Image.SAD)
