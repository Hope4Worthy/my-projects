import os
from threading import Timer
import pynput
from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry('%dx%d+%d+%d' % (160, 40, 5120, 0))
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
    #dark_shade_timer.start()
    imbument_timer.start()

def stop():
    #dark_shade_timer.stop()
    imbument_timer.stop()

def toggle():
    global toggle_flag
    t.delete('1.0' , END)
    toggle_flag = not toggle_flag

    if toggle_flag:
        t.insert(END, "ACTIVE", 'center')
        imbument_caster()
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

def dark_shade_caster():
    keyboard.tap(dark_shade_key)

def imbument_caster():
    keyboard.tap(imbument_key)

#dark_shade_timer = RepeatedTimer(16.31, dark_shade_caster)
imbument_timer = RepeatedTimer(9.98, imbument_caster)

hotkey_toggle = pynput.keyboard.GlobalHotKeys({'<alt>+]': toggle})
hotkey_quit = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': quit})

start()
stop()
t.insert(END, "INACTIVE")

hotkey_toggle.start()
hotkey_quit.start()

root.mainloop()
hotkey_toggle.join()
hotkey_quit.join()