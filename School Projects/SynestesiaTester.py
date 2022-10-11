from tkinter import *
from tkinter import colorchooser
from sys import platform
import pandas as pd


if platform == "linux" or platform == "linux2":
    import os
elif platform == "win32":
    import winsound

freq_list = [
    27.50,  # A0
    29.14,  #
    30.87,  #
    32.70,  #
    34.65,  #
    36.71,  #
    38.89,  #
    41.20,  #
    43.65,  #
    46.25,  #
    49.00,  #
    51.91,  #
    55.00,  #
    58.27,  #
    61.74,  #
    65.41,  #
    69.30,  #
    73.42,  #
    77.78,  #
    82.41,  #
    87.31,  #
    92.50,  #
    98.00,  #
    103.83,  #
    110.00,  #
    116.54,  #
    123.47,  #
    130.81,  #
    138.59,  #
    146.83,  #
    155.56,  #
    164.81,  #
    174.61,  #
    185.00,  #
    196.00,  #
    207.65,  #
    220.00,  #
    233.08,  #
    246.94,  #
    261.63,  #
    277.18,  #
    293.66,  #
    311.13,  #
    329.63,  #
    349.23,  #
    369.99,  #
    392.00,  #
    415.30,  #
    440.00,  #
    466.16,  #
    493.88,  #
    523.25,  #
    554.37,  #
    587.33,  #
    622.25,  #
    659.25,  #
    698.46,  #
    739.99,  #
    783.99,  #
    830.61,  #
    880.00,  #
    932.33,  #
    987.77,  #
    1046.50,  #
    1108.73,  #
    1174.66,  #
    1244.51,  #
    1318.51,  #
    1396.91,  #
    1479.98,  #
    1567.98,  #
    1661.22,  #
    1760.00,  #
    1864.66,  #
    1975.53,  #
    2093.00,  #
    2217.46,  #
    2349.32,  #
    2489.02,  #
    2637.02,  #
    2793.83,  #
    2959.96,  #
    3135.96,  #
    3322.44,  #
    3520.00,  #
    3729.31,  #
    3951.07,  #
    4186.01,  # C8
]
color_list = [000000] * 108
index = 0
duration = 1000  # ms


def choose_color():
    global color_list
    color_list[index] = colorchooser.askcolor(title="Choose Color")
    color_label.config(text=str(color_list[index]), bg=color_list[index][1])


def next_color():
    global index
    index += 1
    freq_label.config(text=str(freq_list[index]))
    color_label.config(text=str(color_list[index]), bg=color_list[index][1])


def last_color():
    global index
    index -= 1
    freq_label.config(text=str(freq_list[index]))
    color_label.config(text=str(color_list[index]), bg=color_list[index][1])


def play_sound():
    freq = freq_list[index]
    if platform == "linux" or platform == "linux2":
        os.system("play -n synth %s sin %s" % (duration / 1000, freq))
    elif platform == "win32":
        winsound.Beep(freq, duration)


def export_selections():
    d = {"frequency": freq_list, "color": color_list}
    df = pd.DataFrame(d)
    writer = pd.ExcelWriter("test.xlsx")
    df.to_excel(writer, sheet_name="welcome", index=False)
    writer.save()


win = Tk()

choose_color_button = Button(win, text="Select color", command=choose_color)
next_color_button = Button(win, text="Next color", command=next_color)
last_color_button = Button(win, text="Last color", command=last_color)
play_sound_button = Button(win, text="Play Sound", command=play_sound)
export_button = Button(win, text="Export", command=export_selections)
freq_label = Label(win, width=25, text=str(freq_list[index]))
color_label = Label(win, width=25, text=str(color_list[index]))

freq_label.grid(column=0, row=0, padx=20, pady=5)
play_sound_button.grid(column=1, row=0, padx=20, pady=5)
last_color_button.grid(column=0, row=1, padx=20, pady=5)
next_color_button.grid(column=1, row=1, padx=20, pady=5)
color_label.grid(column=0, row=2, padx=20, pady=5)
choose_color_button.grid(column=1, row=2, padx=20, pady=5)

export_button.grid(column=0, row=3)
win.geometry("400x200")
win.mainloop()
