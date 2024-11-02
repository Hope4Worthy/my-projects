import cv2 as cv
import numpy as np
import os
from threading import Timer
import pynput
from tkinter import *
from tkinter.font import Font
from mss.linux import MSS as mss
from time import sleep

debug_val = False


root = Tk()
root.geometry('%dx%d+%d+%d' % (160, 40, 5120, 0))
root.geometry("160x40")
root.overrideredirect(True)
root.attributes('-topmost',True)

t = Text(root, height=5, width=200, padx=10)
t.tag_configure("center", justify='center')
t.tag_add('center', '1.0', 'end')
t.configure(font = Font(family="Times New Roman", size=20, weight="bold"))
t.pack()

toggle_flag = False

def get_color(img):
    avg_color_per_row = np.average(img, axis=0)
    avg_colors = np.average(avg_color_per_row, axis=0)
    int_averages = np.array(avg_colors, dtype=np.uint8)
    return int_averages

ls_orig = get_color(cv.imread('/home/brantley/Documents/my-projects/Personal Projects/D4_automation/Sorc/LightningSpear.png', cv.IMREAD_COLOR))

ib_orig = get_color(cv.imread('/home/brantley/Documents/my-projects/Personal Projects/D4_automation/Sorc/IceBlade.png', cv.IMREAD_COLOR))

ia_orig = get_color(cv.imread('/home/brantley/Documents/my-projects/Personal Projects/D4_automation/Sorc/IceArmor.png', cv.IMREAD_COLOR))

keyboard = pynput.keyboard.Controller()
ls_key = '2'
ib_key = '3'
ia_key = '4'

ls_color = [0,0,0]
ib_color = [0,0,0]
ia_color = [0,0,0]


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
    screenshot_timer.start()
    sleep(0.05)
    ls_timer.start()
    ib_timer.start()
    ia_timer.start()

def stop():
    screenshot_timer.stop()
    ls_timer.stop()
    ib_timer.stop()
    ia_timer.stop()

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

def get_diff(color1, color2):
    return np.sum(color1 - color2)

def screenshot():
    os.system('clear')
    global ls_color
    global ib_color
    global ia_color

    with mss() as sct:
        ls_monitor = {"top": 1300, "left": 5675, "width": 80, "height": 80}
        ib_monitor = {"top": 1300, "left": 5757, "width": 80, "height": 80}
        ia_monitor = {"top": 1300, "left": 5839, "width": 80, "height": 80}

        ls_color = get_color(sct.grab(ls_monitor))[:-1]
        ib_color = get_color(sct.grab(ib_monitor))[:-1]
        ia_color = get_color(sct.grab(ia_monitor))[:-1]

def ls_recognition():
    threshold = 200

    result = get_diff(ls_orig, ls_color)

    if debug_val:
        print("LS Value:", result)

    if result <= threshold:
        keyboard.tap(ls_key)

def ib_recognition():
    threshold = 200

    result = get_diff(ib_orig, ib_color)

    if debug_val:
        print("IB Value:", result)

    if result <= threshold:
        keyboard.tap(ib_key)

def ia_recognition():
    threshold = 200

    result = get_diff(ia_orig, ia_color)

    if debug_val:
        print("IA Value:", result)

    if result <= threshold:
        keyboard.tap(ia_key)

delay_time = 0.25
screenshot_timer = RepeatedTimer(delay_time, screenshot)
ls_timer = RepeatedTimer(delay_time, ls_recognition)
ib_timer = RepeatedTimer(delay_time, ib_recognition)
ia_timer = RepeatedTimer(delay_time, ia_recognition)

start()
stop()

hotkey_toggle = pynput.keyboard.GlobalHotKeys({'<alt>+]': toggle})
hotkey_quit = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': quit})

t.insert(END, "INACTIVE")

hotkey_toggle.start()
hotkey_quit.start()

root.mainloop()
hotkey_toggle.join()
hotkey_quit.join()