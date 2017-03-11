from ev3dev.ev3 import *
from time import sleep

btn = Button()

# Do something when state of any button changes:
  
def left(state):
    Sound.tone([(500, 500, 0)]).wait()
def right(state):  # neater use of 'if' follows:
    Sound.tone([(700, 500, 0)]).wait()
    
def up(state):
    Sound.tone([(900, 500, 0)]).wait()
    
def down(state):
    Sound.tone([(1100, 500, 0)]).wait()
    
def enter(state):
    Sound.tone([(1300, 500, 0)]).wait()
    
def backspace(state):
    Sound.tone([(1500, 500, 0)]).wait()
    
btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
btn.on_backspace = backspace

while True:  # This loop checks buttons state continuously, 
             # calls appropriate event handlers
    btn.process() # Check for currently pressed buttons. 
    # If the new state differs from the old state, 
    # call the appropriate button event handlers.
    sleep(0.01)  # buttons state will be checked every 0.01 second