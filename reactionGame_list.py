from microbit import *
import random
images = [Image.RABBIT, Image.COW, Image.PACMAN, Image.DUCK, Image.BUTTERFLY]

while True:
  goal = random.choice(images)
  display.show(goal)
  sleep(1000)
  display.clear()
  sleep(500)
  reactionTime = 0
  while not button_b.is_pressed():
    pic = random.choice(images)
    display.show(pic)
    sleep(500)
  if goal == pic:
    display.show(Image.YES)
    sleep(1000)
  else:
    display.show(Image.NO)
    sleep(1000)

