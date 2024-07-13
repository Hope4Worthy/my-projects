import pyautogui
import cv2 as cv
import numpy as np
import os
from threading import Timer
import pynput
from tkinter import *
from tkinter.font import Font
from pywinctl import getActiveWindowTitle

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
flame_shiled_key = '4'

orig = cv.imread('/home/brantley/Documents/D4_automation/Sorc/flame_shield.png', cv.IMREAD_COLOR)

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
    source = np.array(pyautogui.screenshot(region=(5585,1172,560,228)))
    source = cv.cvtColor(source, cv.COLOR_RGB2BGR)
    return source

def flame_shield_recognition(source):
    flag = False

    threshold = 0.90

    result = cv.matchTemplate(source, orig, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if debug_val:
        print("Value:", max_val)

    if max_val >= threshold:
        flag = True

    if debug_flag_source:
        print("flag:", flag)
    
    return flag

def cast(flag):
    if debug_flag_cast:
        print('flag', flag)
    
    if (flag and getActiveWindowTitle() == 'Diablo IV'):
        keyboard.tap(flame_shiled_key)

def recognition_loop():
    global shield_caster
    t1 = cv.getTickCount()

    if debug_flag_cast or debug_flag_source or debug_val or debug_time:
        os.system('clear')
    source = screenshot()
    flag = flame_shield_recognition(source)
    cast(flag)

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