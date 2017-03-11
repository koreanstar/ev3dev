from ev3dev.ev3 import *
from time import sleep

def do():
  Sound.tone([(262, 500, 0)]).wait()
  sleep(0.01)
def le():
  Sound.tone([(294, 500, 0)]).wait()
  sleep(0.01)
def me():
  Sound.tone([(330, 500, 0)]).wait()
  sleep(0.01)
def pa():
  Sound.tone([(349, 500, 0)]).wait()
  sleep(0.01)
def sol():
  Sound.tone([(392, 500, 0)]).wait()
  sleep(0.01)
def highDo():
  Sound.tone([(523, 500, 0)]).wait()
  sleep(0.01)
def do2():
  Sound.tone([(262, 1000, 0)]).wait()
  sleep(0.01)
def le2():
  Sound.tone([(294, 1000, 0)]).wait()
  sleep(0.01)
def me2():
  Sound.tone([(330, 1000, 0)]).wait()
  sleep(0.01)
def pa2():
  Sound.tone([(349, 1000, 0)]).wait()
  sleep(0.01)
def sol2():
  Sound.tone([(392, 1000, 0)]).wait()
  sleep(0.01)
def highDo2():
  Sound.tone([(523, 1000, 0)]).wait()
  sleep(0.01)
while True:
  sol2()
  me()
  me()
  sol()
  me()
  do2()
  le2()
  me()
  le()
  do()
  me()
  sol2()
  highDo2()
  sol()
  highDo2()
  sol()
  highDo()
  sol()
  me()
  sol2()
  le()
  pa()
  me()
  le()
  do()