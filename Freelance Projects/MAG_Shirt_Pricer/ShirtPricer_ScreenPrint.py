from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from PIL import Image, ImageTk

import pandas as pd
import numpy as np
from itertools import chain

import os
import openpyxl

# ---------- GLOBALS ---------- #
# active caculation flags
screen_print_calc_flag = False

# position values for object placment
initital_offset = 25
y_offset = 50
label_x = 20
entry_x = 250

# font data
font_data = ("Calibri", 12)

# input file types
filetypes = (("Excel files", ("*xlsx", "*xls")), ("All files", "*.*"))

# pricing boundry matricies
screen_print_boundry = [23, 47, 71, 143, 287, 575, 1199, 1200]

# pricing multipliet matricies
screen_print_mult = []

# pricing table matricies
screen_print_price = [[]]
jumbo_print_price = [[]]

# ---------- GET INPUT FILE ---------- #
# get pricing file location from stored location
filePathFile = os.path.dirname(os.path.realpath(__file__)) + "/dataFileLocation.txt"
file = open(filePathFile, "r+")
pricingFilePath = file.read().strip()

# if file not at stored location, ask for new location
if os.path.exists(pricingFilePath) == False:
    pricingFilePath = fd.askopenfilename(
        title="Open the Pricing File", initialdir=os.path.expanduser(""), filetypes=filetypes
    )
    file.seek(0)
    file.write(pricingFilePath)
    file.truncate()

# ---------- WINDOW INITILIZATION ---------- #
# create window
win = Tk()
win.title("Shirt Price Calculator")
win.geometry("920x650")

# set font for tabs
s = ttk.Style()
s.configure("TNotebook.Tab", font=("Calibri", 12))

# create tabs
tab_control = ttk.Notebook(win)

home_tab = ttk.Frame(tab_control)
screen_print_tab = ttk.Frame(tab_control)

tab_control.add(home_tab, text="Home")
tab_control.add(screen_print_tab, text="Screen Printing")

class seperator:
    def __init__(self, tab, location=460):
        self.seperator = ttk.Separator(tab, orient="vertical")
        self.location = location

    def place(self):
        self.seperator.place(x=self.location, width=0.2, relheight=1)

class LabeledCheckbox:
    def __init__(self, tab, label_text, widget_num, initital_value):
        self.value = IntVar(value=initital_value)
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.object = ttk.Checkbutton(tab, variable=self.value, onvalue=1, offvalue=0)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object.place(x=entry_x, y=self.y_pos)

    def get_value(self):
        try:
            return self.value.get()
        except:
            return 0

class LabeledCombobox_int:
    def __init__(self, tab, label_text, widget_num, value_list, initital_value, width):
        self.value = IntVar(value=initital_value)
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.object = ttk.Combobox(tab, values=value_list, textvariable=self.value, width=width, font=font_data)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object.place(x=entry_x, y=self.y_pos)

    def get_value(self):
        try:
            return self.object.get()
        except:
            return 0

class LabeledCombobox_str:
    def __init__(self, tab, label_text, widget_num, value_list, initital_value, width):
        self.value = StringVar(value=value_list[initital_value])
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.object = ttk.Combobox(tab, textvariable=self.value, values=value_list, width=width, font=font_data)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object.place(x=entry_x, y=self.y_pos)

    def get_value(self):
        try:
            
            return self.object.get()
        except:
            return 0

class LabeledSpinBox:
    def __init__(self, tab, label_text, widget_num, min_value, max_value, initital_value, width):
        self.value = IntVar(value=initital_value)
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.object = ttk.Spinbox(tab, from_= min_value, to = max_value, textvariable=self.value, width=width, font=font_data)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object.place(x=entry_x, y=self.y_pos)

    def get_value(self):
        try:
            return int(self.object.get())
        except:
            return 0

class LabeledEntrybox:
    def __init__(self, tab, label_text, widget_num, initital_value, width):
        self.value = DoubleVar(value=initital_value)
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.object = ttk.Entry(tab, width=width, textvariable=self.value, font=font_data)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object.place(x=entry_x, y=self.y_pos)

    def get_value(self):
        try:
            val = self.value.get()
        except:
            val = 0
        return val

class ColorLocation:
    special_inks = ("Standard", "Shimmer", "Cristilina", "Glimmer", "Glow")

    def __init__(self, tab, header_text, location_num):
        # value varriables
        self.special_value = StringVar(value="Standard")
        self.color_value = IntVar(value=0)

        # seperator object
        self.seperator = ttk.Separator(tab, orient="horizontal")

        # label objects
        self.header_label = ttk.Label(tab, text=header_text, font=font_data)
        self.color_label = ttk.Label(tab, text="Number of Colors", font=font_data)
        self.special_label = ttk.Label(tab, text="Ink Type", font=font_data)

        # entry objects
        self.color_select = ttk.Spinbox(tab,from_ = 1, to = 3, textvariable=self.color_value, width=13, font=font_data)
        self.special_select = ttk.Combobox(tab, textvariable=self.special_value, width=13, font=font_data)

        # varriables for placement location
        self.row = 4 * (location_num - 1)
        self.sep_flag = location_num > 1
        self.sep_y = 115 * (location_num - 1)

    def place(self, num_ordered):
        # select list to be used based in number of shirts ordered
        if num_ordered <= screen_print_boundry[0]:
            max_value = 3
        elif num_ordered <= screen_print_boundry[1]:
            max_value = 5
        elif num_ordered <= screen_print_boundry[2]:
            max_value = 8
        elif num_ordered <= screen_print_boundry[3]:
            max_value = 11
        else:
            max_value = 13

        self.special_select.config(values=self.special_inks)
        self.color_select.config(to=max_value)

        # set initial values
        if self.color_value.get() == 0:
            self.color_value.set(1)
        else:
            self.color_value.set(self.color_value.get())
        self.special_value.set("Standard")

        y_pad = 11

        if self.sep_flag:
            self.seperator.grid(row=self.row, column=1, columnspan=20, sticky='w', pady=y_pad, ipadx=300)

        # place objects
        if not self.sep_flag:
            self.header_label.grid(row=self.row + 1, column=2, padx=0, pady=0, sticky="w")
        else:
            self.header_label.grid(row=self.row + 1, column=2, padx=0, pady=y_pad, sticky="w")

        self.color_label.grid(row=self.row + 2, column=1, padx=10, pady=y_pad, sticky="w")
        self.color_select.grid(row=self.row + 2, column=2, padx=25, pady=y_pad, sticky="w")

        self.special_label.grid(row=self.row + 3, column=1, padx=10, pady=y_pad, sticky="w")
        self.special_select.grid(row=self.row + 3, column=2, padx=25, pady=y_pad, sticky="w")

    def destroy(self):
        # clear values
        self.color_value.set(0)
        self.special_value.set(0)

        # remove objects
        self.seperator.place(height=0, relwidth=0)

        self.header_label.grid_forget()

        self.color_label.grid_forget()
        self.color_select.grid_forget()

        self.special_label.grid_forget()
        self.special_select.grid_forget()

    def get_price(self, index, print_type):
        value = int(self.color_select.get())

        if value == 0:
            return 0

        ink_type = self.special_value.get()
        if ink_type == self.special_inks[0]:
            ink_price = 0
        elif ink_type == self.special_inks[1] or ink_type == self.special_inks[2] or ink_type == self.special_inks[3]:
            ink_price = 0.25
        else:
            ink_price = 0.50

        if print_type == "Jumbo":
            if type(jumbo_print_price[value - 1][index]) is float:
                return jumbo_print_price[value - 1][index] + ink_price
            else:
                return 0
        else:
            if type(screen_print_price[value - 1][index]) is float:
                return screen_print_price[value - 1][index] + ink_price
            else:
                return 0

class PocketPrint:
    def __init__(self, tab, label_text, widget_num):
        self.value_check = DoubleVar(value=0)
        self.value_spin = IntVar(value=1)
        self.label = ttk.Label(tab, text=label_text, font=font_data)
        self.spin_label = ttk.Label(tab, text="Colors:", font=font_data)
        self.object_check = ttk.Checkbutton(tab, variable=self.value_check, onvalue=0.35, offvalue=0)
        self.object_spin = ttk.Spinbox(tab, from_= 1, to = 3, textvariable=self.value_spin, width=5, font=font_data)
        self.y_pos = initital_offset + (y_offset * (widget_num - 1))
        self.value_check.trace_add('write', self.update_color)
    
    def update_color(*args):
        if args[0].value_check.get() == 0:
            args[0].object_spin.place_configure(height=0, width=0)
            args[0].spin_label.place_configure(height=0, width=0)
        else:
            args[0].object_spin.place_configure(height=25, width=50)
            args[0].spin_label.place_configure(height=25, width=75)

    def place(self):
        self.label.place(x=label_x, y=self.y_pos)
        self.object_check.place(x=entry_x, y=self.y_pos)
        self.object_spin.place(x=entry_x+75, y=self.y_pos+30, height=0, width=0)
        self.spin_label.place(x=entry_x, y=self.y_pos+30, height=0, width=0)

    def get_value(self, index):
        value_spin = int(self.value_spin.get())
        value_check = float(self.value_check.get())

        if value_check == 0:
            return 0

        if type(screen_print_price[value_spin - 1][index]) is float:
            return screen_print_price[value_spin - 1][index] + value_check
        else:
            return 0

# ---------- DATA READ FUNCTION ---------- #
def read_data():
    global screen_print_mult
    global screen_print_price
    global jumbo_print_price

    # collect screen printing data
    data = pd.read_excel(pricingFilePath, "Screen Print")
    screen_print_mult = list(chain.from_iterable(np.delete(data.loc[16:16, :].values, 0, axis=1)))
    screen_print_price = np.delete(data.loc[1:13, :].values, 0, axis=1)
    i = 0
    for mult in screen_print_mult:
        screen_print_mult[i] = mult[mult.rfind('x'):mult.rfind('S')][1:].strip()
        i += 1

    # collect jumbo screen printing data
    data = pd.read_excel(pricingFilePath, "Jumbo SP")
    jumbo_print_price = np.delete(data.loc[1:13, :].values, 0, axis=1)

# ---------- TAB SETUP FUNCTIONS ---------- #
def home_tab_setup():
    # open image and set properties
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/mag.png"
    display = ImageTk.PhotoImage(Image.open(file_path).resize((900, 517)))
    image = Label(home_tab, image=display)
    image.image = display

    # create text object
    message = "To get started select the appropraite tab above"
    text = Label(home_tab, text=message, font=("Calibri", 25))

    # place objects
    image.place(x=(920/2) - (900/2), y = 25)
    text.place(x = 55, y = 567)

def screen_print_tab_setup():
    # ----- LOCAL VARRAIBELS ----- #
    combo_width = 13
    entry_width = 13

    printing_options = ("Standard", "Jumbo")
    message = (
        "Standard printing minimum order quantity 12\n\n"
        + "Jumbo printing minimum order quantity 48\n"
        + "Jumbo printing is only on sizes above Adult Medium\n\n"
        + "Below are the pricing ranges:\n"
        + "S1   12-23 \t S5   144-287\n"
        + "S2   24-47 \t S6   288-575\n"
        + "S3   48-71 \t S7   576-1199\n"
        + "S4   72-143 \t S8   1200+\n"
    )

    # ----- FUNCTIONS ----- #
    def display_color_locations(*args):
        # collect inputs
        number_location_value = int(number_locations.get_value())
        number_ordered_value = int(number_ordered.get_value())

        # display collect number of positions
        if number_location_value == 1:
            location_one.place(number_ordered_value)
            location_two.destroy()
            location_three.destroy()
            location_four.destroy()
            return
        elif number_location_value == 2:
            location_one.place(number_ordered_value)
            location_two.place(number_ordered_value)
            location_three.destroy()
            location_four.destroy()
            return
        elif number_location_value == 3:
            location_one.place(number_ordered_value)
            location_two.place(number_ordered_value)
            location_three.place(number_ordered_value)
            location_four.destroy()
            return
        else:
            location_one.place(number_ordered_value)
            location_two.place(number_ordered_value)
            location_three.place(number_ordered_value)
            location_four.place(number_ordered_value)
            return

    def validate_inputs(*args):
        if screen_print_calc_flag:
            # collect inputs
            retail_price_value = retail_price.get_value()
            number_ordered_value = number_ordered.get_value()

            if retail_price_value < 0:
                retail_price.value.set(0)
            if printing_type.get_value() == "Standard":
                if number_ordered_value < 12:
                    number_ordered.value.set(12)
            elif printing_type.get_value() == "Jumbo":
                if number_ordered_value < 48:
                    number_ordered.value.set(48)
            if screen_print_calc_flag == True:
                calculate_price()
        win.after(500, validate_inputs)

    def calculate_price():
        #here to get around python garbage collection
        printing_type.value.set(printing_type.value.get())
        printing_type.object.set(printing_type.object.get())

        # get updated pricing info
        read_data()

        # calcuate position on pricing matricies
        number_ordered_value = int(number_ordered.get_value())
        index = 0
        for i in range(len(screen_print_boundry)):
            if number_ordered_value <= screen_print_boundry[i]:
                index = i
                break

        if index > 7:
            index = 7

        # calculate and round price
        print_type = printing_type.get_value()
        price_value = ((retail_price.get_value() * float(screen_print_mult[index])) + location_one.get_price(index, print_type) + location_two.get_price(index, print_type) + location_three.get_price(index, print_type) + location_four.get_price(index, print_type) + pocket.get_value(index))
        price_value = round(price_value, 2)
        total_value = round(price_value * number_ordered_value, 2)

        # display price
        price.object.delete(0, "end")
        price_total.object.delete(0, "end")
        price.object.insert(END, "%.2f" % price_value)
        price_total.object.insert(END, "%.2f" % total_value)

    # ----- CREATE OBJECTS ----- #
    spacer = ttk.Label(screen_print_tab, text="")
    vertical_seperator = seperator(screen_print_tab)

    printing_type = LabeledCombobox_str(screen_print_tab, "Printing Type", 1, printing_options, 0, combo_width)
    retail_price = LabeledEntrybox(screen_print_tab, "Retail Price", 2, 1, entry_width)
    number_ordered = LabeledSpinBox(screen_print_tab, "Number Ordered", 3, 12, 999999, 12, combo_width)
    number_locations = LabeledSpinBox(screen_print_tab, "Number of Locations", 4, 1,4, 1, combo_width)
    pocket = PocketPrint(screen_print_tab, "Pocket Printing", 5)
    price = LabeledEntrybox(screen_print_tab, "Price Per Shirt", 7, 0, entry_width)
    price_total = LabeledEntrybox(screen_print_tab, "Order Price", 8, 0, entry_width)

    details = ttk.Label(screen_print_tab, text=message, font=font_data)

    location_one = ColorLocation(screen_print_tab, "Location One", 1)
    location_two = ColorLocation(screen_print_tab, "Location Two", 2)
    location_three = ColorLocation(screen_print_tab, "Location Three", 3)
    location_four = ColorLocation(screen_print_tab, "Location Four", 4)

    # ----- Place Objects ----- #
    spacer.grid(row=0, column=0, padx=230)
    printing_type.place()
    vertical_seperator.place()
    retail_price.place()
    number_ordered.place()
    number_locations.place()
    pocket.place()
    price.place()
    price_total.place()
    details.place(x=label_x, y=415)
    location_one.place(12)

    # ----- MONITOR VALUES ----- #
    number_ordered.value.trace_add("write", display_color_locations)
    number_locations.value.trace_add("write", display_color_locations)

    validate_inputs() # validate and calculate every 500ms

# ---------- START TABS ---------- #
home_tab_setup()
screen_print_tab_setup()

tab_control.pack(expand=True, fill="both")

# ---------- GET INITIAL PRICING DATA ---------- #
read_data()

# ---------- START CACULATIONS FOR CURRENT TAB ---------- #
def on_tab_change(event):
    global screen_print_calc_flag
    tab = event.widget.tab('current')['text']
    if tab == 'Home':
        screen_print_calc_flag = False
    elif tab == 'Screen Printing':
        screen_print_calc_flag = True

tab_control.bind('<<NotebookTabChanged>>', on_tab_change)

# ---------- START WINDOW ---------- #
win.mainloop()