import pyautogui
import cv2 as cv
import numpy as np
import os
from threading import Timer
import os
from time import sleep
import pynput

p_flag = False
c_flag = False

keyboard = pynput.keyboard.Controller()

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
    
    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
    
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
    
    def stop(self):
        self._timer.cancel()
        self.is_running = False

def start_timers():
    Timer(0.1, start_timers)
    precision()
    combo()
    cast()

def precision():
    global p_flag

    threshold = 0.80

    orig = cv.imread('C:\\Users\\b\\D4_automation\\precision0.png', cv.IMREAD_COLOR)

    source=pyautogui.screenshot(region=(465,1172,400,55))
    source.save('precision.png')
    source = cv.imread("precision.png", cv.IMREAD_COLOR)

    result = cv.matchTemplate(source, orig, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val >= threshold:
        p_falg = True
        print('found precsion')

def combo():
    global c_flag

    threshold = 0.80

    orig = cv.imread('C:\\Users\\b\\D4_automation\\combo0.png', cv.IMREAD_COLOR)

    source=pyautogui.screenshot(region=(975,1250,50,150))
    source.save('combo.png')
    source = cv.imread("combo.png", cv.IMREAD_COLOR)

    result = cv.matchTemplate(source, orig, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val >= threshold:
        c_falg = True
        print('found combo')


def cast():
    global p_flag
    global c_flag

    if p_flag and c_flag:
        keyboard.tap('5')
        c_flag = False
        p_falg = False


hotkey_toggle_1 = pynput.keyboard.GlobalHotKeys({'<alt>+]': start_timers})
hotkey_toggle_1.start()
hotkey_toggle_1.join()