from time import sleep   # needed for sleep
from ev3dev.ev3 import *  # needed for Sound
a = 500
while True:
  Sound.tone([(a, 100, 0)]).wait()
  sleep(0.01)
  a = a+100
