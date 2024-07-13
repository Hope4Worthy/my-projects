import pyautogui
import cv2 as cv
import numpy as np
import os
from threading import Timer
import pynput
from tkinter import *
from tkinter.font import Font
from pygetwindow import getActiveWindowTitle as getWindow

debug_val = False
debug_flag_source = False
debug_flag_cast = False
debug_time = False

root = Tk()
root.geometry("160x40")
root.attributes('-alpha',0.5)
root.overrideredirect(True)
root.attributes('-topmost',True)

t = Text(root, height=5, width=200, padx=10)
t.tag_configure("center", justify='center')
t.tag_add('center', '1.0', 'end')
t.configure(font = Font(family="Times New Roman", size=20, weight="bold"))
t.pack()

toggle_flag = False

keyboard = pynput.keyboard.Controller()
imbument_key = '3'
dark_shade_key = '4'

orig_imbument = cv.imread('C:\\Users\\b\\D4_automation\\rouge\\imbument.png', cv.IMREAD_COLOR)
orig_dark_shade = cv.imread('C:\\Users\\b\\D4_automation\\rouge\\dark_shade.png', cv.IMREAD_COLOR)

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
    
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

def start():
    shield_caster.start()

def stop():
    shield_caster.stop()

def toggle():
    global toggle_flag
    t.delete('1.0' , END)
    toggle_flag = not toggle_flag

    if toggle_flag:
        t.insert(END, "ACTIVE", 'center')
        start()
    else:
        t.insert(END, "INACTIVE", 'centeraa')
        stop()

def quit():
    stop()
    hotkey_toggle.stop()
    hotkey_quit.stop()
    root.quit()
    os._exit(0)

def screenshot():
    source = np.array(pyautogui.screenshot(region=(465,1172,560,228)))
    source = cv.cvtColor(source, cv.COLOR_RGB2BGR)
    return source

def imbument_recognition(source):
    flag = False

    threshold = 0.70

    result = cv.matchTemplate(source, orig_imbument, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if debug_val:
        print("I - Value:", max_val)

    if max_val >= threshold:
        flag = True

    if debug_flag_source:
        print("I - flag:", flag)
    
    return flag

def dark_shade_recognition(source):
    flag = False

    threshold = 0.80

    result = cv.matchTemplate(source, orig_dark_shade, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if debug_val:
        print("DS - Value:", max_val)

    if max_val >= threshold:
        flag = True

    if debug_flag_source:
        print("DS - flag:", flag)
    
    return flag

def cast(flag_imbument, flag_dark_shade):
    if debug_flag_cast:
        print('imbument flag', flag_imbument)
        print('dark shade flag', flag_dark_shade)
    
    window_flag = (getWindow() == 'Diablo IV')

    if (flag_imbument and window_flag):
        keyboard.tap(imbument_key)
    if (flag_dark_shade and window_flag):
        keyboard.tap(dark_shade_key)

def recognition_loop():
    global shield_caster
    t1 = cv.getTickCount()

    if debug_flag_cast or debug_flag_source or debug_val or debug_time:
        os.system('cls')
    source = screenshot()
    flag_imbument = imbument_recognition(source)
    flag_dark_shade = dark_shade_recognition(source)
    cast(flag_imbument, flag_dark_shade)

    t2 = cv.getTickCount()
    time = (t2-t1)/cv.getTickFrequency()
    if debug_time:
        print("time per loop", time)
    shield_caster.interval = time

shield_caster = RepeatedTimer(0.10, recognition_loop)

hotkey_toggle = pynput.keyboard.GlobalHotKeys({'<alt>+]': toggle})
hotkey_quit = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': quit})

t.insert(END, "INACTIVE")

hotkey_toggle.start()
hotkey_quit.start()

root.mainloop()
hotkey_toggle.join()
hotkey_quit.join()