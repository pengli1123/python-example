#!/usr/bin/python

import threading
import time
import os
#import win32com.client
#import win32ui

from ctypes import *

# START SENDINPUT TYPE DECLARATIONS
PUL = POINTER(c_ulong)
class KeyBdInput(Structure):
    _fields_ = [("wVk", c_ushort),
             ("wScan", c_ushort),
             ("dwFlags", c_ulong),
             ("time", c_ulong),
             ("dwExtraInfo", PUL)]

class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
             ("wParamL", c_short),
             ("wParamH", c_ushort)]

class MouseInput(Structure):
    _fields_ = [("dx", c_long),
             ("dy", c_long),
             ("mouseData", c_ulong),
             ("dwFlags", c_ulong),
             ("time",c_ulong),
             ("dwExtraInfo", PUL)]

class Input_I(Union):
    _fields_ = [("ki", KeyBdInput),
              ("mi", MouseInput),
              ("hi", HardwareInput)]

class Input(Structure):
    _fields_ = [("type", c_ulong),
             ("ii", Input_I)]

class POINT(Structure):
    _fields_ = [("x", c_ulong),
             ("y", c_ulong)]
# END SENDINPUT TYPE DECLARATIONS

class Timer(threading.Thread):
	def __init__(self, seconds):
		self.runTime = seconds
		threading.Thread.__init__(self)
	def run(self):
		time.sleep(self.runTime)
		print "time's up"
		
user32 = windll.user32
FInputs = Input * 2
extra = c_ulong(0)

click = Input_I()
click.mi = MouseInput(0, 0, 0, 2, 0, pointer(extra))
release = Input_I()
release.mi = MouseInput(0, 0, 0, 4, 0, pointer(extra))

x = FInputs( (0, click), (0, release) )

class CountDownTimer(Timer):
	def __init__(self, timeout, runTime):
		Timer.__init__(self, runTime)
		self.timeout = timeout
		self.offset = 0
		
	def run(self):
		counter = 4948
		for sec in range(self.runTime):
			print counter
			time.sleep(self.timeout)
			counter += 3
			user32.SendInput(2, pointer(x), sizeof(x[0]))
			user32.SendInput(2, pointer(x), sizeof(x[0]))
		print "done"

if __name__ == "__main__":

	timeout = 180
	runTime = 250

	c = CountDownTimer(timeout, runTime)
	
	#x, y = win32ui.FindWindow(None, "Guild Wars").GetWindowRect()[0:2]
	#user32.SetCursorPos(x+100, y+150)
	c.start()

