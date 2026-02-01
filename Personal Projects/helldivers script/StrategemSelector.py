import pynput
import time
import os
import tkinter as tk
from tkinter import ttk
from stratagem_list import *

# ---------- GLOBAL STATE ---------- #

current_loadout = [None, None, None, None]
flag = True
key_delay = 0.02

input = pynput.keyboard.Controller()

# ---------- CORE FUNCTIONS ---------- #

def execute(strategem):
    if not strategem:
        return

    input.press(pynput.keyboard.Key.alt_l)
    for key in strategem[:-1]:
        time.sleep(key_delay)
        input.press(key)
        time.sleep(key_delay)
        input.release(key)
    input.release(pynput.keyboard.Key.alt_l)

def on_active_toggle():
    global flag
    flag = not flag
    update_ui()

# ---------- KEY LISTENER ---------- #

def on_press(key):
    if not flag:
        return

    keymap = {
        pynput.keyboard.Key.home: 0,
        pynput.keyboard.Key.end: 1,
        pynput.keyboard.Key.page_up: 2,
        pynput.keyboard.Key.page_down: 3,
    }

    if key in keymap:
        execute(current_loadout[keymap[key]])
    elif key == pynput.keyboard.Key.insert:
        execute(mission_resupply)
    elif key == pynput.keyboard.Key.delete:
        execute(mission_reinforce)

# ---------- TKINTER UI ---------- #

def update_ui():
    status_label.config(text="Status: ACTIVE" if flag else "Status: INACTIVE")

def start_ui():
    global status_label

    root = tk.Tk()
    root.title("Strategem Selector")
    root.geometry("550x360")
    root.resizable(False, False)

    status_label = tk.Label(root, font=("Arial", 14))
    status_label.pack(pady=8)

    # --- Loadout selector ---
    loadout_var = tk.StringVar()
    loadout_box = ttk.Combobox(
        root, textvariable=loadout_var,
        values=list(loadouts.keys()),
        state="readonly", width=25
    )
    loadout_box.pack(pady=5)

    # --- Determine initial loadout (first one) ---
    first_loadout_name = list(loadouts.keys())[0]
    loadout_box.set(first_loadout_name)  # default selection

    # ---------- Slots ----------
    slot_frames = []

    def make_slot(parent, index):
        frame = tk.Frame(parent)
        frame.pack(pady=5, fill="x")

        tk.Label(frame, text=f"Slot {index + 1}", width=8).grid(row=0, column=0)

        group_var = tk.StringVar()
        strat_var = tk.StringVar()

        group_box = ttk.Combobox(
            frame, textvariable=group_var,
            values=list(GROUPS.keys()), state="readonly", width=12
        )
        group_box.grid(row=0, column=1, padx=5)

        strat_box = ttk.Combobox(
            frame, textvariable=strat_var,
            state="readonly", width=30
        )
        strat_box.grid(row=0, column=2, padx=5)

        def update_strategems(*_):
            group = group_var.get()
            names = [s[-1] for s in GROUPS[group]]
            strat_box["values"] = names
            if strat_var.get() not in names:
                strat_var.set(names[0])
                set_loadout()

        def set_loadout(*_):
            group = GROUPS[group_var.get()]
            name = strat_var.get()
            for strat in group:
                if strat[-1] == name:
                    current_loadout[index] = strat
                    return

        group_var.trace_add("write", update_strategems)
        strat_var.trace_add("write", set_loadout)

        slot_frames.append((group_var, strat_var))
        return group_var, strat_var

    slots_container = tk.Frame(root)
    slots_container.pack(pady=10)

    for i in range(4):
        make_slot(slots_container, i)

    # ---------- Function to switch loadouts ----------
    def loadout_selected(*_):
        name = loadout_var.get()
        if name not in loadouts:
            return
        for i, (g, s) in enumerate(loadouts[name]):
            group_var, strat_var = slot_frames[i]
            if g in GROUPS:
                group_var.set(g)
                # Set strategem only if valid in group
                if s in [x[-1] for x in GROUPS[g]]:
                    strat_var.set(s)
                else:
                    strat_var.set(GROUPS[g][0][-1])

    loadout_var.trace_add("write", loadout_selected)
    loadout_selected()  # initialize first loadout

    # ---------- Buttons ----------
    tk.Button(root, text="Toggle Active", command=on_active_toggle, width=25).pack(pady=8)
    tk.Button(root, text="Quit", command=root.destroy, width=25).pack()

    update_ui()
    root.mainloop()

# ---------- STARTUP ---------- #

listener = pynput.keyboard.Listener(on_press=on_press)
hotkey_toggle = pynput.keyboard.GlobalHotKeys({'<ctrl>+q': on_active_toggle})

listener.start()
hotkey_toggle.start()

start_ui()
