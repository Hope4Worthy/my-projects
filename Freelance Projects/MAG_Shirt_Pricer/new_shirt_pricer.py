from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from PIL import Image, ImageTk

import pandas as pd
import numpy as np
from itertools import chain

import os
#import openpyxl #only needed if running in windows

# ---------- GLOBALS ---------- #
# active caculation flags
embroidery_calc_flag = False
screen_print_calc_flag = False

# position values for object placment
initital_offset = 25
y_offset = 50
label_x = 20
entry_x = 250

# font data
font_data = ("Calibri", 15)

# input file types
filetypes = (("Excel files", ("*xlsx", "*xls")), ("All files", "*.*"))

# pricing boundry matricies
screen_print_boundry = [23, 47, 71, 143, 287, 572, 1199, 1200]
embroidery_boundry = [1, 5, 11, 23, 47, 71, 143, 287, 575]

# pricing multipliet matricies
screen_print_mult = []
embroidery_mult = []

# pricing table matricies
screen_print_price = [[]]
embroidery_price = [[]]
supplied_embroidery_price = [[]]


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
win.geometry("920x550")

# set font for tabs
s = ttk.Style()
s.configure("TNotebook.Tab", font=("Calibri", 12))

# create tabs
tab_control = ttk.Notebook(win)

home_tab = ttk.Frame(tab_control)
screen_print_tab = ttk.Frame(tab_control)
embroidery_tab = ttk.Frame(tab_control)

tab_control.add(home_tab, text="Home")
tab_control.add(screen_print_tab, text="Screen Printing")
tab_control.add(embroidery_tab, text="Embroidery")

# ---------- OBJECT CLASSES ---------- #
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

class LabeledCombobox:
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
    # avabile numbe of colors based on number ordered
    avalable_colors_1 = ("1", "2", "3")
    avalable_colors_2 = ("1", "2", "3", "4", "5")
    avalable_colors_3 = ("1", "2", "3", "4", "5", "6", "7", "8")

    def __init__(self, tab, header_text, location_num):
        # value varriables
        self.special_value = DoubleVar(value=0.00)
        self.color_value = IntVar(value=0)

        # seperator object
        self.seperator = ttk.Separator(tab, orient="horizontal")

        # label objects
        self.header_label = ttk.Label(tab, text=header_text, font=font_data)
        self.color_label = ttk.Label(tab, text="Number of Colors", font=font_data)
        self.special_label = ttk.Label(tab, text="Special Ink", font=font_data)

        # entry objects
        self.color_select = ttk.Combobox(tab, textvariable=self.color_value, width=13, font=font_data)
        self.special_check = ttk.Checkbutton(tab, variable=self.special_value, onvalue=0.25, offvalue=0)

        # varriables for placement location
        self.row = 3 * (location_num - 1)
        self.sep_flag = location_num > 1
        self.sep_y = 115 * (location_num - 1)

    def place(self, num_ordered):
        # select list to be used based in number of shirts ordered
        if num_ordered <= screen_print_boundry[0]:
            self.color_select.config(values=self.avalable_colors_1)
        elif num_ordered <= screen_print_boundry[1]:
            self.color_select.config(values=self.avalable_colors_2)
        else:
            self.color_select.config(values=self.avalable_colors_3)

        # set initial values
        self.color_value.set(1)
        self.special_value.set(0.00)

        # place objects
        self.header_label.grid(row=self.row, column=2, padx=0, pady=10, sticky="w")

        self.color_label.grid(row=self.row + 1, column=1, padx=10, pady=2, sticky="w")
        self.color_select.grid(row=self.row + 1, column=2, padx=25, pady=2, sticky="w")

        self.special_label.grid(row=self.row + 2, column=1, padx=10, pady=2, sticky="w")
        self.special_check.grid(row=self.row + 2, column=2, padx=25, pady=2, sticky="w")

        if self.sep_flag:
            self.seperator.place(y=self.sep_y, x=460, height=0.2, relwidth=0.5)

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
        self.special_check.grid_forget()

    def get_price(self, index):
        if int(self.color_value.get()) == 0:
            return 0

        return self.special_value.get() + screen_print_price[int(self.color_value.get()) - 1][index]

# ---------- DATA READ FUNCTION ---------- #
def read_data():
    global screen_print_mult
    global screen_print_price
    global embroidery_mult
    global embroidery_price
    global supplied_embroidery_price

    # collect screen printing data
    data = pd.read_excel(pricingFilePath, "Screen Printing")
    screen_print_mult = list(chain.from_iterable(np.delete(data.loc[14:14, :].values, 0, axis=1)))
    screen_print_price = np.delete(data.loc[1:8, :].values, 0, axis=1)

    # collect embroidery data
    data = pd.read_excel(pricingFilePath, "Embroidery")
    embroidery_mult = np.delete(data.loc[11:11, :].values, 0)
    embroidery_price = np.delete(data.loc[1:9, :].values, 0, axis=1)

    # collect supplied embroidery data
    data = pd.read_excel(pricingFilePath, "Supplied Embroidery")
    supplied_embroidery_price = np.delete(data.loc[1:9, :].values, 0, axis=1)

# ---------- TAB SETUP FUNCTIONS ---------- #
def home_tab_setup():
    # open image and set properties
    file_path = os.path.dirname(os.path.realpath(__file__)) + "/mag.png"
    display = ImageTk.PhotoImage(Image.open(file_path).resize((750, 367)))
    image = Label(home_tab, image=display)
    image.image = display

    # create text object
    message = "To get started select the appropraite tab above"
    text = Label(home_tab, text=message, font=("Calibri", 25))

    # place objects
    image.grid(row=0, column=0)
    text.grid(row=1, column=0)

def screen_print_tab_setup():
    # ----- LOCAL VARRAIBELS ----- #
    combo_width = 13
    entry_width = 15
    num_positions = ("1", "2", "3", "4")
    message = (
        "This Tab is for Screen Printing Only\n"
        + "Below are the Pricing Ranges:\n"
        + "S1   12-24\n"
        + "S2   24-47\n"
        + "S3   47-71\n"
        + "S4   72-143\n"
        + "S5   144-287\n"
        + "S6   288-575\n"
        + "S7   576-1199\n"
        + "S8   1200+"
    )

    # ----- FUNCTIONS ----- #
    def display_color_locations(*args):
        print('** COLORS **')
        # colelct inputs
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
                price.object.delete(0, "end")
                price.object.insert(END, "INVALID RETAIL PRICE")

            elif number_ordered_value < 12:
                price.object.delete(0, "end")
                price.object.insert(END, "INVALID NUMBER ORDERED")
            elif screen_print_calc_flag == True:
                calculate_price()
        win.after(500, validate_inputs)

    def calculate_price():
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
        price_value = ((retail_price.get_value() * screen_print_mult[index]) + location_one.get_price(index) + location_two.get_price(index) + location_three.get_price(index) + location_four.get_price(index))
        price_value = round(price_value, 2)

        # display price
        price.value.set(price_value)

    # ----- CREATE OBJECTS ----- #
    spacer = ttk.Label(screen_print_tab, text="")
    vertical_seperator = seperator(screen_print_tab)

    retail_price = LabeledEntrybox(screen_print_tab, "Retail Price", 1, 1, entry_width)
    number_ordered = LabeledEntrybox(screen_print_tab, "Number Ordered", 2, 12, entry_width)
    number_locations = LabeledCombobox(screen_print_tab, "Number of Locations", 3, num_positions, 1, combo_width)
    price = LabeledEntrybox(screen_print_tab, "Price", 5, 0, entry_width)

    details = ttk.Label(screen_print_tab, text=message, font=font_data)

    location_one = ColorLocation(screen_print_tab, "Location One", 1)
    location_two = ColorLocation(screen_print_tab, "Location Two", 2)
    location_three = ColorLocation(screen_print_tab, "Location Three", 3)
    location_four = ColorLocation(screen_print_tab, "Location Four", 4)

    # ----- Place Objects ----- #
    spacer.grid(row=0, column=0, padx=230)
    vertical_seperator.place()
    retail_price.place()
    number_ordered.place()
    number_locations.place()
    price.place()
    details.place(x=label_x, y=275)
    location_one.place(12)

    # ----- MONITOR VALUES ----- #
    number_ordered.value.trace("w", display_color_locations)
    number_locations.value.trace("w", display_color_locations)

    validate_inputs() # validate and calculate every 500ms

def embroidery_tab_setup():
    # ----- LOCAL VARRIABLES ----- #
    combo_width = 40
    entry_width = 15
    types = ('Text Only', 'Logo', 'Hats', 'Towel', 'Medium Size Over 10,000 Stitches', "Full Size (10.75 x 10.75)", 'Full Size (10.75 x 10.75) Over 50,000 Stitches')
    message = (
        "This Tab is for Embroidery Only\n"
        + "Below are the Pricing Ranges:\n"
        + "S1   1\n"
        + "S2   2-5\n"
        + "S3   6-11\n"
        + "S4   12-23\n"
        + "S5   24-47\n"
        + "S6   48-71\n"
        + "S7   72-143\n"
        + "S8   144-287\n"
        + "S9   288-575"
    )
    # ----- FUNCTIONS ----- #
    def validate_inputs(*args):
        if embroidery_calc_flag:
            # collect inputs
            retail_price_value = retail_price.get_value()
            number_ordered_value = number_ordered.get_value()

            if retail_price_value < 0:
                price.object.delete(0, "end")
                price.object.insert(END, "INVALID RETAIL PRICE")

            elif number_ordered_value < 1:
                price.object.delete(0, "end")
                price.object.insert(END, "INVALID NUMBER ORDERED")

            else:
                calculate_price()
        win.after(500, validate_inputs)

    def calculate_price():
        # get updated pricing info
        read_data()

        # calcuate position on pricing matricies
        number_ordered_value = int(number_ordered.get_value())
        index = 0
        for i in range(len(embroidery_boundry)):
            if number_ordered_value <= embroidery_boundry[i]:
                index = i
                break

        if index > 8:
            index = 8

        type_value = type_ordered.get_value()
        type_index = 0
        if type_value == types[0]: type_index=0
        elif type_value == types[1]: type_index=1
        elif type_value == types[2]: type_index=4
        elif type_value == types[3]: type_index=5
        elif type_value == types[4]: type_index=6
        elif type_value == types[5]: type_index=7
        elif type_value == types[6]: type_index=8

        # calculate and round price
        if supplied.get_value() == 1:
            price_value = (retail_price.get_value() * embroidery_mult[index]) + (second_location.get_value() * supplied_embroidery_price[2][index]) + (title.get_value() * supplied_embroidery_price[3][index]) + supplied_embroidery_price[type_index][index]
        else:
            price_value = (retail_price.get_value() * embroidery_mult[index]) + (second_location.get_value() * embroidery_price[2][index]) + (title.get_value() * embroidery_price[3][index]) + embroidery_price[type_index][index]
        price_value = round(price_value, 2)

        # display price
        price.value.set(price_value)

    # ----- CREATE OBJECTS ----- #
    supplied = LabeledCheckbox(embroidery_tab, 'Supplied', 1, 0)
    retail_price = LabeledEntrybox(embroidery_tab, "Retail Price", 2, 1, entry_width)
    number_ordered = LabeledEntrybox(embroidery_tab, "Number Ordered", 3, 1, entry_width)
    type_ordered = LabeledCombobox(embroidery_tab, 'Type', 4, types, types[0], combo_width)
    second_location = LabeledCheckbox(embroidery_tab, 'Second Location', 5, 0)
    title = LabeledCheckbox(embroidery_tab, 'Name or Title Added', 6, 0)
    price = LabeledEntrybox(embroidery_tab, "Price", 8, 0, entry_width)
    details = ttk.Label(embroidery_tab, text=message, font=font_data)

    # ----- Place Objects ----- #
    supplied.place()
    retail_price.place()
    number_ordered.place()
    type_ordered.place()
    second_location.place()
    title.place()
    price.place()
    details.place(x = 475, y = 225)

    # ----- MONITOR VALUES ----- #
    validate_inputs() # validate and caculate every 500ms

# ---------- START TABS ---------- #
home_tab_setup()
screen_print_tab_setup()
embroidery_tab_setup()

tab_control.pack(expand=True, fill="both")

# ---------- GET INITIAL PRICING DATA ---------- #
read_data()

# ---------- START CACULATIONS FOR CURRENT TAB ---------- #
def on_tab_change(event):
    global screen_print_calc_flag
    global embroidery_calc_flag
    tab = event.widget.tab('current')['text']
    if tab == 'Home':
        screen_print_calc_flag = False
        embroidery_calc_flag = False
    elif tab == 'Screen Printing':
        screen_print_calc_flag = True
        embroidery_calc_flag = False
    elif tab == 'Embroidery':
        screen_print_calc_flag = False
        embroidery_calc_flag = True

tab_control.bind('<<NotebookTabChanged>>', on_tab_change)

# ---------- START WINDOW ---------- #
win.mainloop()
