import pynput
import time
import os
from stratagem_list import *

# ********** loadouts ********** #
loadout_attack_bots         = [eagle_clusterBomb, eagle_airstrike, support_railgun, backpack_personalShield]
loadout_attack_bots_low     = [eagle_airstrike, orbital_railcannonStrike, orbital_precisionStrike, support_railgun]
loadout_attack_bots_high    = [eagle_airstrike, orbital_railcannonStrike, support_railgun, backpack_personalShield]
loadout_attack_bugs         = [eagle_airstrike, orbital_railcannonStrike, orbital_precisionStrike, backpack_personalShield]
loadout_attack_bugs_high    = [eagle_airstrike, orbital_railcannonStrike, support_expendableAntiTank, backpack_personalShield]

loadout_defense         = [sentry_mortar, sentry_autocannon, support_quasarCannon, backpack_personalShield]

active_loadout = loadout_attack_bugs_high

# set to none if no active global stratagem
stratagemG      = none

# overide loadout stratagem
overide1 = none
overide2 = none 
overide3 = none 
overide4 = none

# ********** Set strategem ********** #

stratagem1 = active_loadout[0] if overide1 == none else overide1
stratagem2 = active_loadout[1] if overide2 == none else overide2
stratagem3 = active_loadout[2] if overide3 == none else overide3
stratagem4 = active_loadout[3] if overide4 == none else overide4

# ********** Strategem keys ********** #
stratagem1_key      = pynput.keyboard.Key.home
stratagem2_key      = pynput.keyboard.Key.end
stratagem3_key      = pynput.keyboard.Key.page_up
stratagem4_key      = pynput.keyboard.Key.page_down
stratagemG_key      = '5'

resupply_key    = pynput.keyboard.Key.insert
reinforce_key   = pynput.keyboard.Key.delete
hellbomb_key    = pynput.keyboard.Key.f4

stratagem_toggle = pynput.keyboard.Key.alt_l

# ********** Varriables ********** #

key_delay   = 0.06 #  adjusts speed at which strategems inputs are used
flag        = True # set for starting state
input       = pynput.keyboard.Controller()

# ********** Program Functions ********** #

def toggle_print(): # print message in toggle
    global flag
    
    os.system('clear')
    if(flag):
        print("***** ACTIVE *****")
    else:
        print("***** INACTIVE *****")

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
    os.system('clear')
    exit()

def on_active_toggle(): # toggle active / inactive
    global flag

    flag = not flag
    toggle_print()

def on_press(key): # listner function
    if(flag):
        # ***** strategem 1 ***** #
        if(key == stratagem1_key):
            execute(stratagem1)
        # ***** stragem 2 ***** #
        if(key == stratagem2_key):
            execute(stratagem2)
        # ***** stragem 3 ***** #
        if(key == stratagem3_key):
            execute(stratagem3)
        # ***** stragem 4 ***** #
        if(key == stratagem4_key):
            execute(stratagem4)
        # ***** global stratagem ***** #
        if(key == stratagemG_key):
            execute(stratagemG)

        # ***** mission stratagems ***** #
        if(key == resupply_key):
            execute(mission_resupply)
        if(key == reinforce_key): 
            execute(mission_reinforce)
            execute(mission_hellbomb)

# ********** Startup Script ********** #

toggle_print()

# define program listners
hotkey_quit     = pynput.keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': on_active_quit})
hotkey_toggle   = pynput.keyboard.GlobalHotKeys({'<alt>+]': on_active_toggle})
listner         = pynput.keyboard.Listener(on_press=on_press)

# start lisnters
hotkey_quit.start()
hotkey_toggle.start()
listner.start()

# start threads
hotkey_quit.join()
hotkey_toggle.join()
listner.join()
