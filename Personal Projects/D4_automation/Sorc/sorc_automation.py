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
mouse_flag = False

uc_orig = [104, 55, 44]
ls_orig = [113, 57, 44]
ib_orig = [111, 86, 37]
ia_orig = [119, 97, 44]
fs_orig = [35, 63, 104]

damage_buff_orig = cv.imread('/home/brantley/Documents/my-projects/Personal Projects/D4_automation/Sorc/damage_buff.png', cv.IMREAD_GRAYSCALE)

keyboard = pynput.keyboard.Controller()

uc_key = '1'
ls_key = '2'
ib_key = '3'
ia_key = '4'
fs_key = '5'

uc_color = [0,0,0]
ls_color = [0,0,0]
ib_color = [0,0,0]
ia_color = [0,0,0]
fs_color = [0,0,0]
buff_source = Image


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
    sc_timer.start()
    sleep(0.05)
    uc_timer.start()
    ls_timer.start()
    ib_timer.start()
    ia_timer.start()
    fs_timer.start()

def stop():
    sc_timer.stop()
    uc_timer.stop()
    ls_timer.stop()
    ib_timer.stop()
    ia_timer.stop()
    fs_timer.stop()

def toggle():
    global toggle_flag
    t.delete('1.0' , END)
    toggle_flag = not toggle_flag

    if toggle_flag:
        t.insert(END, "ACTIVE", 'center')
        start()
    else:
        t.insert(END, "INACTIVE", 'center')
        stop()

def quit():
    stop()
    hotkey_toggle.stop()
    hotkey_quit.stop()
    root.quit()
    os._exit(0)

def get_color(img):
    avg_color_per_row = np.average(img, axis=0)
    avg_colors = np.average(avg_color_per_row, axis=0)
    int_averages = np.array(avg_colors, dtype=np.uint8)
    return int_averages

def get_diff(color1, color2):
    return np.sum(color1 - color2)

def on_click(x, y, button, pressed):
    global mouse_flag

    if button == pynput.mouse.Button.left:
        if pressed:
            mouse_flag = True
        else:
            mouse_flag = False

def screenshot():
    global uc_color
    global ls_color
    global ib_color
    global ia_color
    global fs_color
    global buff_source

    with mss() as sct:
        uc_monitor = {"top": 1300, "left": 5593, "width": 80, "height": 80}
        ls_monitor = {"top": 1300, "left": 5675, "width": 80, "height": 80}
        ib_monitor = {"top": 1300, "left": 5757, "width": 80, "height": 80}
        ia_monitor = {"top": 1300, "left": 5839, "width": 80, "height": 80}
        fs_monitor = {"top": 1300, "left": 6003, "width": 80, "height": 80}
        buff_monitor = {"top": 1110, "left": 5585, "width": 458, "height": 120}

        uc_color = get_color(sct.grab(uc_monitor))[:-1]
        ls_color = get_color(sct.grab(ls_monitor))[:-1]
        ib_color = get_color(sct.grab(ib_monitor))[:-1]
        ia_color = get_color(sct.grab(ia_monitor))[:-1]
        fs_color = get_color(sct.grab(fs_monitor))[:-1]
        buff_source = cv.cvtColor(np.asarray(sct.grab(buff_monitor))[:-1], cv.COLOR_RGB2GRAY)
    
    if debug_val:
        os.system('clear')

def uc_recognition():
    threshold = 25

    result = get_diff(uc_orig, uc_color)

    if debug_val:
        print("UC Value:", result)

    if result <= threshold and mouse_flag:
        keyboard.tap(uc_key)

def ls_recognition():
    threshold = 25

    result = get_diff(ls_orig, ls_color)

    if debug_val:
        print("LS Value:", result)

    if result <= threshold and mouse_flag:
        keyboard.tap(ls_key)

def ib_recognition():
    threshold = 25

    result = get_diff(ib_orig, ib_color)

    if debug_val:
        print("IB Value:", result)

    if result <= threshold and mouse_flag:
        keyboard.tap(ib_key)

def ia_recognition():
    threshold = 25

    result = get_diff(ia_orig, ia_color)

    if debug_val:
        print("IA Value:", result)

    if result <= threshold and mouse_flag:
        keyboard.tap(ia_key)

def fs_recognition():
    buff_threshold = 0.70
    color_threshold = 25

    buff_result = cv.matchTemplate(buff_source, damage_buff_orig, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(buff_result)

    color_result = get_diff(fs_orig, fs_color)

    if debug_val:
        print("FS Value:", color_result)
        print("Buff Value:", max_val)

    if max_val <= buff_threshold and color_result <= color_threshold and mouse_flag:
        keyboard.tap(fs_key)

delay_time = 0.25
sc_timer = RepeatedTimer(delay_time, screenshot)
uc_timer = RepeatedTimer(delay_time, uc_recognition)
ls_timer = RepeatedTimer(delay_time, ls_recognition)
ib_timer = RepeatedTimer(delay_time, ib_recognition)
ia_timer = RepeatedTimer(delay_time, ia_recognition)
fs_timer = RepeatedTimer(delay_time, fs_recognition)

start()
stop()

mouse_listner = pynput.mouse.Listener(on_click=on_click)
hotkey_toggle = pynput.keyboard.GlobalHotKeys({'<alt>+]': toggle})
hotkey_quit = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': quit})

t.insert(END, "INACTIVE")

mouse_listner.start()
hotkey_toggle.start()
hotkey_quit.start()

root.mainloop()
mouse_listner.join()
hotkey_toggle.join()
hotkey_quit.join()