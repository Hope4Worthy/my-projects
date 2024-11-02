import os
from threading import Timer
import pynput
from tkinter import *
from tkinter.font import Font
from time import sleep as wait

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

ice_shield_key = '4'
ice_blades_key = '3'
lightning_spear_key = '2'

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
    cast_all_timer.start()
    #ice_sheild_timer.start()
    #ice_blades_timer.start()
    #lightning_spear_timer.start()

def stop():
    cast_all_timer.stop()
    #ice_sheild_timer.stop()
    #ice_blades_timer.stop()
    #lightning_spear_timer.stop()

def toggle():
    global toggle_flag
    t.delete('1.0' , END)
    toggle_flag = not toggle_flag

    if toggle_flag:
        t.insert(END, "ACTIVE", 'center')
        cast_all()
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

def cast_all():
    lightning_spear_caster()
    ice_shiled_caster()
    ice_blades_caster()

def ice_shiled_caster():
    keyboard.tap(ice_shield_key)

def ice_blades_caster():
    keyboard.tap(ice_blades_key)

def lightning_spear_caster():
    keyboard.tap(lightning_spear_key)

#ice_sheild_timer = RepeatedTimer(4.4, ice_shiled_caster)
#ice_blades_timer = RepeatedTimer(3.52, ice_blades_caster)
#lightning_spear_timer = RepeatedTimer(4.5, lightning_spear_caster)

cast_all_timer = RepeatedTimer(2.0, cast_all)

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