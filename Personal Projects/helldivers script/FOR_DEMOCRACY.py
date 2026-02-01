import pynput
import time
import os
from stratagem_list import *

# ********** loadouts ********** #

loadouts = [
    ["Bots : Low",eagle_airstrike, orbital_railcannonStrike, orbital_precisionStrike, support_railgun],
    ["Bots : High",eagle_airstrike, orbital_railcannonStrike, support_railgun, backpack_personalShield],
    ["Bugs : Low",eagle_airstrike, orbital_railcannonStrike, orbital_precisionStrike, backpack_personalShield],
    ["Bugs : High",eagle_airstrike, orbital_railcannonStrike, support_expendableAntiTank, backpack_personalShield],
    ["Defense",sentry_autocannon, orbital_railcannonStrike, support_quasarCannon, backpack_personalShield]
]

active_loadout = 0

# ********** Strategem keys ********** #
stratagem1_key      = pynput.keyboard.Key.home
stratagem2_key      = pynput.keyboard.Key.end
stratagem3_key      = pynput.keyboard.Key.page_up
stratagem4_key      = pynput.keyboard.Key.page_down
stratagemG_key      = '5'

resupply_key    = pynput.keyboard.Key.insert
reinforce_key   = pynput.keyboard.Key.delete

stratagem_toggle = pynput.keyboard.Key.alt_l

# ********** Varriables ********** #

key_delay   = 0.02 #  adjusts speed at which strategems inputs are used
flag        = True # set for starting state
input       = pynput.keyboard.Controller()

# ********** Program Functions ********** #

def toggle_print(): # print message in toggle
    global flag
    
    os.system('clear')
    if(flag):
        print("ACTIVE :", loadouts[active_loadout][0])
    else:
        print("INACTIVE")

def execute(strategem): # execute strategem
    global key_delay

    input.press(stratagem_toggle)

    for key in strategem:
        time.sleep(key_delay)
        input.press(key)
        time.sleep(key_delay)
        input.release(key)

    input.release(stratagem_toggle)

def on_active_quit(): # close threads and quit
    listner.stop()
    hotkey_quit.stop()
    hotkey_toggle.stop()
    hotkey_next.stop()
    hotkey_prev.stop()

    os.system('clear')
    os._exit(0)

def on_active_toggle(): # toggle active / inactive
    global flag

    flag = not flag
    toggle_print()

def next_loadout():
    global active_loadout
    active_loadout = (active_loadout + 1)
    
    if(active_loadout >= len(loadouts)): active_loadout = 0

    toggle_print()

def prev_loadout():
    global active_loadout
    active_loadout = (active_loadout - 1)
    
    
    if(active_loadout < 0): active_loadout = len(loadouts) - 1

    toggle_print()

def on_press(key): # listner function
    if(flag):
        # ***** strategem 1 ***** #
        if(key == stratagem1_key):
            execute(loadouts[active_loadout][1])
        # ***** stragem 2 ***** #
        if(key == stratagem2_key):
            execute(loadouts[active_loadout][2])
        # ***** stragem 3 ***** #
        if(key == stratagem3_key):
            execute(loadouts[active_loadout][3])
        # ***** stragem 4 ***** #
        if(key == stratagem4_key):
                execute(loadouts[active_loadout][4])

        # ***** mission stratagems ***** #
        if(key == resupply_key):
            execute(mission_resupply)
        if(key == reinforce_key): 
            execute(mission_reinforce)

# ********** Startup Script ********** #

toggle_print()

# define program listners
hotkey_quit     = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': on_active_quit})
hotkey_toggle   = pynput.keyboard.GlobalHotKeys({'<ctrl>+q': on_active_toggle})
hotkey_next     = pynput.keyboard.GlobalHotKeys({'<ctrl>+]': next_loadout}) 
hotkey_prev     = pynput.keyboard.GlobalHotKeys({'<ctrl>+[': prev_loadout})
listner         = pynput.keyboard.Listener(on_press=on_press)

# start lisnters
hotkey_quit.start()
hotkey_toggle.start()
hotkey_next.start()
hotkey_prev.start()
listner.start()

# start threads
hotkey_quit.join()
hotkey_toggle.join()
hotkey_next.join()
hotkey_prev.join()
listner.join()
