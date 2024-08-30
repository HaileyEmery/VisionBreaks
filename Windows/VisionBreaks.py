from time import sleep
from os import startfile, system
from ctypes import windll

SCREENSAVER_PATH = "C:\Windows\System32\\"
SCREENSAVER_NAME ="Ribbons.scr"
BREAK_DURATION_SECONDS = 30
BREAK_FREQUENCY_MINUTES = 20

def StartBreak():
    windll.user32.BlockInput(True) #Start Blocking Keyboard and Mouse Input
    startfile(SCREENSAVER_PATH + SCREENSAVER_NAME) #Start Screen Saver

def EndBreak():
    system("taskkill /f /im " + SCREENSAVER_NAME) #Close Screensaver
    windll.user32.BlockInput(False) #Stop Blocking Keyboard and Mouse Input

while True:
    sleep(BREAK_FREQUENCY_MINUTES*60 - BREAK_DURATION_SECONDS)
    StartBreak()
    sleep(BREAK_DURATION_SECONDS)
    EndBreak()
