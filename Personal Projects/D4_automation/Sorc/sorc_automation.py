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
root.overrideredirect(True)
root.attributes('-topmost',True)

t = Text(root, height=5, width=200, padx=10)
t.tag_configure("center", justify='center')
t.tag_add('center', '1.0', 'end')
t.configure(font = Font(family="Times New Roman", size=20, weight="bold"))
t.pack()

toggle_flag = False
mouse_flag = False

keyboard = pynput.keyboard.Controller()

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

class color_skill_watcher(object):

    global keyboard
    global toggle_flag
    global mouse_flag

    def __init__(self, key, monitor_coordinates, source_color, interval, threshold, *args, **kwargs):
        self.cast_key = key
        self.monitor = monitor_coordinates
        self.orig = source_color
        self.interval = interval
        self.threshold = threshold
        self.args = args
        self.kwargs = kwargs

        self.timer = None

    def _run(self):
        with mss() as sct:
            img = sct.grab(self.monitor)
        avg_color_per_row = np.average(img, axis=0)
        avg_colors = np.average(avg_color_per_row, axis=0)
        color = np.array(avg_colors, dtype=np.uint8)[:-1]

        result = np.sum(color - self.orig)

        if result <= self.threshold and toggle_flag and mouse_flag:
            keyboard.tap(self.cast_key)

    def start(self):
        if self.timer == None:
            self.timer = RepeatedTimer(self.interval, self._run)
        self.timer.start()
    
    def stop(self):
        if self.timer != None:
            self.timer.stop()

class hybrid_skill_watcher(object):
    
    global keyboard
    global toggle_flag
    global mouse_flag

    def __init__(self, key, color_monitor_coordinates, img_monitor_coordinates, source_color, source_img_path, interval, color_threshold, img_threshold, mode, *args, **kwargs):
        self.cast_key = key
        self.colorMonitor = color_monitor_coordinates
        self.imgMonitor = img_monitor_coordinates
        self.origColor = source_color
        self.origImg = cv.imread(source_img_path, cv.IMREAD_GRAYSCALE)

        self.interval = interval
        self.colorThreshold = color_threshold
        self.imageThreshold = img_threshold
        self.mode = mode # 0 for img_result <= threshold, 1 for img_result >= threshold
        self.args = args
        self.kwargs = kwargs

        self.timer = None

    def _run(self):
        with mss() as sct:
            color_img = sct.grab(self.colorMonitor)
            img_img = cv.cvtColor(np.asarray(sct.grab(self.imgMonitor))[:-1], cv.COLOR_RGB2GRAY)

        avg_color_per_row = np.average(color_img, axis=0)
        avg_colors = np.average(avg_color_per_row, axis=0)
        color = np.array(avg_colors, dtype=np.uint8)[:-1]

        color_result = np.sum(color - self.origColor)

        buff_result = cv.matchTemplate(self.origImg, img_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(buff_result)

        if self.mode == 0:
            if color_result <= self.colorThreshold and max_val <= self.imageThreshold and toggle_flag and mouse_flag:
                keyboard.tap(self.cast_key)
        else:
            if color_result <= self.colorThreshold and max_val >= self.imageThreshold and toggle_flag and mouse_flag:
                keyboard.tap(self.cast_key)

    def start(self):
        if self.timer == None:
            self.timer = RepeatedTimer(self.interval, self._run)
        self.timer.start()
    
    def stop(self):
        if self.timer != None:
            self.timer.stop()

class img_skill_watcher(object):
    global keyboard
    global toggle_flag
    global mouse_flag

    def __init__(self, key, monitor_coordinates, source_img_path, interval, img_threshold, mode, *args, **kwargs):
        self.cast_key = key
        self.monitor = monitor_coordinates
        self.orig = cv.imread(source_img_path, cv.IMREAD_GRAYSCALE)
        self.interval = interval
        self.threshold = img_threshold
        self.mode = mode # 0 for result <= threshold, 1 for result >= threshold
        self.args = args
        self.kwargs = kwargs

        self.timer = None

    def _run(self):
        with mss() as sct:
            img_img = cv.cvtColor(np.asarray(sct.grab(self.monitor))[:-1], cv.COLOR_RGB2GRAY)

        result = cv.matchTemplate(self.orig, img_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if self.mode == 0:
            if max_val <= self.threshold and toggle_flag and mouse_flag:
                keyboard.tap(self.cast_key)
        else:
            if max_val >= self.threshold and toggle_flag and mouse_flag:
                keyboard.tap(self.cast_key)

    def start(self):
        if self.timer == None:
            self.timer = RepeatedTimer(self.interval, self._run)
        self.timer.start()
    
    def stop(self):
        if self.timer != None:
            self.timer.stop()

def start():
    uc_timer.start()
    ls_timer.start()
    ib_timer.start()
    ia_timer.start()
    fs_timer.start()

def stop():
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

def on_click(x, y, button, pressed):
    global mouse_flag

    if button == pynput.mouse.Button.left:
        if pressed:
            mouse_flag = True
        else:
            mouse_flag = False

buff_path = '/home/brantley/Documents/my-projects/Personal Projects/D4_automation/Sorc/damage_buff.png'

uc_timer = color_skill_watcher('1', {"top": 1300, "left": 5593, "width": 80, "height": 80}, [104, 55, 44], 0.25, 25)
ls_timer = color_skill_watcher('2', {"top": 1300, "left": 5675, "width": 80, "height": 80}, [113, 57, 44], 0.25, 25)
ib_timer = color_skill_watcher('3', {"top": 1300, "left": 5757, "width": 80, "height": 80}, [111, 86, 37], 0.25, 25)
ia_timer = color_skill_watcher('4', {"top": 1300, "left": 5839, "width": 80, "height": 80}, [119, 97, 44], 0.25, 25)
fs_timer = hybrid_skill_watcher('5', {"top": 1300, "left": 6003, "width": 80, "height": 80}, {"top": 1110, "left": 5585, "width": 458, "height": 120}, [35, 63, 104], buff_path, 0.25, 25, 0.70, 0)

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