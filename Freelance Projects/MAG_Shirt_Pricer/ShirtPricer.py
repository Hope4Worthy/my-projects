from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
import pandas as pd
import numpy as np
import os
import openpyxl
from PIL import Image, ImageTk

filetypes = (("Excel files", ("*xlsx", "*xls")), ("All files", "*.*"))

# input file information
filePathFile = os.path.dirname(os.path.realpath(__file__)) + "/dataFileLocation.txt"
file = open(filePathFile, "r+")
pricingFilePath = file.read()
pricingFilePath = pricingFilePath.strip()

if os.path.exists(pricingFilePath) == False:
    pricingFilePath = fd.askopenfilename(title="Open a file", initialdir=os.path.expanduser(""), filetypes=filetypes)
    file.seek(0)
    file.write(pricingFilePath)
    file.truncate()



data = pd.read_excel(pricingFilePath, "Screen Printing")
pricingBoundryMatrix = [23, 47, 71, 143, 284, 575, 1199, 1200]  # upper bounds of each pricing bracket
multiplier = np.delete(data.loc[14:14, :].values, 0)  # multiplier for each pricing bracket
priceMatrix = np.delete(data.loc[1:8, :].values, 0, axis=1)  # additions based on number of colors

# entry filed widths
entryWidth = 15
buttonWidth = 14
comboWidth = 13
embroideryTypeComboWidth = 40

# position values for placment of objects
initialOffset = 25
yOffset = 50
labelX = 20
entryX = 225

# lists for comboboxes
numPositionsList = ("1", "2", "3", "4")

avalableColorList1 = ("1", "2", "3")
avalableColorList2 = ("1", "2", "3", "4", "5")
avalableColorList3 = ("1", "2", "3", "4", "5", "6", "7", "8")

embroideryTypeList = (
    "Text Only",
    "Logo",
    "Hats",
    "Towels",
    "Medium - Over 10,000 Stitches",
    "Full Size (10.75 x 10.75)",
    "Full Size (10.75 x 10.75) Over 50,000 Stitches",
)

# set font and size
fontData = ("Calibri", 15)

# create window
win = Tk()
win.title("Caculate Prices")
win.geometry("800x550")

# set font size for tabs
s = ttk.Style()
s.configure("TNotebook.Tab", font=("Calibri", 12))

# create Tabs
tabControl = ttk.Notebook(win)

ScreenPrintTab = ttk.Frame(tabControl, width=500, height=500)
EmbroideryTab = ttk.Frame(tabControl)
HomeTab = ttk.Frame(tabControl)

tabControl.add(HomeTab, text="Home")
tabControl.add(ScreenPrintTab, text="Screen Printing")
tabControl.add(EmbroideryTab, text="Embroidery")


class seperator:
    def headerComment():
        # contain the information for a vertical separator
        #
        # contains the following objects:
        # 	seperator - the seperator
        #
        # contians the folloving methods
        # 	__init__: initilizes the seperator object
        #
        # 	place: places the seperator
        return

    def __init__(self, tab):
        self.seperator = ttk.Separator(tab, orient="vertical")

    def place(self):
        self.seperator.place(x=400, width=0.2, relheight=1)


class colorLocation:
    def headerComment():
        # contains information about a location for printing
        #
        # contains the following objects
        # 	specialValue - value used for special ink checkbox
        # 	colorValue - value used for number of colorn dropbox
        # 	seperator - line seperator used for clarity
        # 	headerLabel - text object for a section header
        # 	numLabel - text object to tabel entry field for number of colors
        # 	numEntry - dropbox for the avaliable values of number of colors
        # 	specialCheck - checkbox to denote the use of special inks
        # 	placeRow - varriable to denote what rows to place objects in
        # 	sepFlag - a flag to denote if the seperator is needed
        # 	sepY - a varriable that specifies the Y coordinate of the seperator
        #
        # contains the following methods:
        # 	__init__ : initilives the object
        # 		takes:
        # 			headerText - string - text to be placed in the header label
        # 			locationNum - int - the number of places from the top this object will be placed
        #
        # 	place : places all objects contained within this class
        # 		takes:
        # 			numOrdered - int - value for the number of untis ordered, used to select number of avalable colors
        #
        # 	destroy: removes all objects associated with the class from the window
        #
        # 	getPrice: add all pricing fields associated with this class
        # 		takes:
        # 			mI - int - the index used to acess the price matrix (calculated from numOrdered)
        # 		returns:
        # 			real value that is the sum of the pricing info in the object
        return

    def __init__(self, headerText, locationNum, tab):
        # value varriables
        self.specialvalue = DoubleVar(value=0.00)
        self.colorValue = IntVar(value=0)

        # seperator object
        self.seperator = ttk.Separator(tab, orient="horizontal")

        # label objects
        self.headerLabel = ttk.Label(ScreenPrintTab, text=headerText, font=fontData)
        self.numLabel = ttk.Label(tab, text="Number of Colors", font=fontData)
        self.specialLabel = ttk.Label(tab, text="Special Ink", font=fontData)

        # entry field objects
        self.numEntry = ttk.Combobox(tab, textvariable=self.colorValue, width=comboWidth, font=fontData)
        self.specialCheck = ttk.Checkbutton(tab, variable=self.specialvalue, onvalue=0.25, offvalue=0)

        # varriables for placment location
        self.placeRow = 3 * (locationNum - 1)
        self.sepFlag = locationNum > 1
        self.sepY = 115 * (locationNum - 1)

    def place(self, numOrdered):
        # select what list to use for number of locations
        if numOrdered <= pricingBoundryMatrix[0]:
            self.numEntry.config(values=avalableColorList1)
        elif numOrdered <= pricingBoundryMatrix[1]:
            self.numEntry.config(values=avalableColorList2)
        else:
            self.numEntry.config(values=avalableColorList3)

        # set initial values
        self.colorValue.set(1)
        self.specialvalue.set(0.00)

        # place objects
        self.headerLabel.grid(row=self.placeRow, column=2, padx=0, pady=10, sticky="w")
        self.numLabel.grid(row=self.placeRow + 1, column=1, padx=10, pady=2, sticky="w")
        self.specialLabel.grid(row=self.placeRow + 2, column=1, padx=10, pady=2, sticky="w")
        self.numEntry.grid(row=self.placeRow + 1, column=2, padx=25, pady=2, sticky="w")
        self.specialCheck.grid(row=self.placeRow + 2, column=2, padx=25, pady=2, sticky="w")

        # place seperator if this is the 2 - 4 color location object
        if self.sepFlag:
            self.seperator.place(y=self.sepY, x=400, height=0.2, relwidth=0.5)

    def destroy(self):
        # clear entry fields
        self.colorValue.set(0)
        self.specialvalue.set(0.00)

        # remove all objects
        self.seperator.place(height=0, relwidth=0)
        self.seperator.grid_forget()
        self.headerLabel.grid_forget()
        self.numLabel.grid_forget()
        self.specialLabel.grid_forget()
        self.numEntry.grid_forget()
        self.specialCheck.grid_forget()

    def getPrice(self, mI):
        if int(self.colorValue.get()) == 0:
            return 0
        return self.specialvalue.get() + priceMatrix[int(self.colorValue.get()) - 1][mI]


class LabeledCheckbox:
    def headerComment():
        # contains information about a labeled checkbox
        #
        # contains the following objects:
        # 	value - a value used to track changes to the entry field
        # 	label - a text object that describes what the entry is
        # 	entry - a field that is used to input information
        # 	yPos - a varriable that denotes the y coordinate to place the objects at
        #
        # contains the following methods:
        # 	__init__: ititalizes a class object
        # 		takes:
        # 			labelText - string - what text to place in the label
        # 			widgetNum - int - the position from the top, used for placment
        # 			initial value - int - a number use to initilize entry
        #
        # 	place: places all objects contained within the class
        return

    def __init__(self, labelText, widgetNum, initialValue, tab):
        self.value = IntVar()
        self.label = ttk.Label(tab, text=labelText, font=fontData)
        self.entry = ttk.Checkbutton(tab, variable=self.value, onvalue=1, offvalue=0)
        self.yPos = initialOffset + (yOffset * (widgetNum - 1))

    def place(self):
        self.value.set(0)
        self.label.place(x=labelX, y=self.yPos)
        self.entry.place(x=entryX, y=self.yPos)


class LabeledEntry:
    def headerComment():
        # contains information about a labeled entry
        #
        # contains the following objects:
        # 	value - a value used to track changes to the entry field
        # 	label - a text object that describes what the entry is
        # 	entry - a field that is used to input information
        # 	yPos - a varriable that denotes the y coordinate to place the objects at
        #
        # contains the following methods:
        # 	__init__: ititalizes a class object
        # 		takes:
        # 			labelText - string - what tekt to place in the label
        # 			widgetNum - int - the position from the top, used for placment
        # 			initial value - int - a number use to initilize entry
        #
        # 	place: places all objects contained within the class
        return

    def __init__(self, labelText, widgetNum, inialValue, tab):
        self.value = DoubleVar(value=inialValue)
        self.label = ttk.Label(tab, text=labelText, font=fontData)
        self.entry = ttk.Entry(tab, width=entryWidth, textvariable=self.value, font=fontData)
        self.yPos = initialOffset + (yOffset * (widgetNum - 1))

    def place(self):
        self.label.place(x=labelX, y=self.yPos)
        self.entry.place(x=entryX, y=self.yPos)

    def get_value(self):
        return int(self.entry.get())


class LabeledCombo:
    def headerComment():
        # contains information about a labeled combobox
        #
        # contains the following objects:
        # 	value - a value used to track changes to the entry field
        # 	label - a text object that describes what the entry is
        # 	entry - a field that is used to input information
        # 	yPos - a varriable that denotes the y coordinate to place the objects at
        #
        # contains the following methods:
        # 	__init__: ititalizes a class object
        # 		takes:
        # 			labelText - string - what tekt to place in the label
        # 			widgetNum - int - the position from the top, used for placment
        # 			initial value - int - a number use to initilize entry
        #
        # 	place: places all objects contained within the class
        return

    def __init__(self, labelText, valList, widgetNum, inialValue, tab, width=comboWidth):
        self.value = IntVar(value=inialValue)
        self.label = ttk.Label(tab, text=labelText, font=fontData)
        self.entry = ttk.Combobox(tab, values=valList, textvariable=self.value, width=width, font=fontData)
        self.yPos = initialOffset + (yOffset * (widgetNum - 1))

    def place(self):
        self.label.place(x=labelX, y=self.yPos)
        self.entry.place(x=entryX, y=self.yPos)


def ScreenPrintTabFunct():
    def caculate():
        data = pd.read_excel(pricingFilePath, "Screen Printing")
        multiplier = np.delete(data.loc[14:15, :].values, 0)  # multiplier for each pricing bracket
        priceMatrix = np.delete(data.loc[:7, :].values, 0, axis=1)  # additions based on number of colors

        num = int(numOrdered.entry.get())
        mI = 0
        for i in range(len(pricingBoundryMatrix)):
            if num <= pricingBoundryMatrix[i]:
                mI = i
                break
            elif num >= pricingBoundryMatrix[-1]:
                mI = int(len(pricingBoundryMatrix))

        if mI > 7:
            mI = 7
        calcPrice = (
            (int(retail.entry.get()) * multiplier[mI])
            + locOne.getPrice(mI)
            + locTwo.getPrice(mI)
            + locThree.getPrice(mI)
            + locFour.getPrice(mI)
        )
        calcPrice = round(calcPrice, 2)

        price.value.set(calcPrice)
        return

    def colloctClrInfo(var1, var2, var3):
        # used for the placment of the correct number of location objects

        numberLocations = int(numLocations.entry.get())
        numberOrdered = int(numOrdered.get_value())

        if numberLocations == 1:
            locOne.place(numberOrdered)
            locTwo.destroy()
            locThree.destroy()
            locFour.destroy()
            return

        elif numberLocations == 2:
            locOne.place(numberOrdered)
            locTwo.place(numberOrdered)
            locThree.destroy()
            locFour.destroy()
            return

        elif numberLocations == 3:
            locOne.place(numberOrdered)
            locTwo.place(numberOrdered)
            locThree.place(numberOrdered)
            locFour.destroy()
            return

        else:
            locOne.place(numberOrdered)
            locTwo.place(numberOrdered)
            locThree.place(numberOrdered)
            locFour.place(numberOrdered)
            return

    def Validate(var1, var2, var3):
        # validotes inputs
        # calculates the price if all inputs are valid
        calcFlag = True
        retailPrice = int(retail.entry.get())
        numberOrdered = int(numOrdered.entry.get())
        numberLocations = int(numLocations.entry.get())

        if retailPrice < 0:
            price.entry.delete(0, "end")
            price.entry.insert(END, "Invalid Retail Price")

        elif numberOrdered < 12:
            price.entry.delete(0, "end")
            price.entry.insert(END, "Invalid Number Ordered")

        else:
            caculate()

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

    # create objects
    spacer = ttk.Label(ScreenPrintTab, text="")
    vertSeperator = seperator(ScreenPrintTab)

    retail = LabeledEntry("Retail Price", 1, 1, ScreenPrintTab)
    numOrdered = LabeledEntry("Number Ordered", 2, 12, ScreenPrintTab)
    numLocations = LabeledCombo("Number of Locations", numPositionsList, 3, 1, ScreenPrintTab)
    price = LabeledEntry("Price", 5, 0, ScreenPrintTab)
    detail = ttk.Label(ScreenPrintTab, text=message, font=fontData)
    locOne = colorLocation("Location One", 1, ScreenPrintTab)
    locTwo = colorLocation("Location Two", 2, ScreenPrintTab)
    locThree = colorLocation("Location Three", 3, ScreenPrintTab)
    locFour = colorLocation("Location Four", 4, ScreenPrintTab)

    # place objects
    spacer.grid(row=0, column=0, padx=200)
    vertSeperator.place()
    retail.place()
    numOrdered.place()
    numLocations.place()
    price.place()
    detail.place(x=labelX, y=275)
    locOne.place(12)

    # validate changes whenever a change is nade to an entry
    retail.value.trace("w", Validate)

    numOrdered.value.trace("w", Validate)
    numOrdered.value.trace("w", colloctClrInfo)

    numLocations.value.trace("w", Validate)
    numLocations.value.trace("w", colloctClrInfo)

    locOne.specialvalue.trace("w", Validate)
    locOne.colorValue.trace("w", Validate)

    locTwo.specialvalue.trace("w", Validate)
    locTwo.colorValue.trace("w", Validate)

    locThree.specialvalue.trace("w", Validate)
    locThree.colorValue.trace("w", Validate)

    locFour.specialvalue.trace("w", Validate)
    locFour.colorValue.trace("w", Validate)

    colloctClrInfo(1, 2, 3)
    Validate(1, 2, 3)


def HomeTabFunt():
    # open and set image object
    filePath = os.path.dirname(os.path.realpath(__file__)) + "/mag.png"
    image = Image.open(filePath).resize((750, 367))
    display = ImageTk.PhotoImage(image)
    image = Label(HomeTab, image=display)
    image.image = display

    # create text object
    message = "To get started select the appropraite tab above"
    text = Label(HomeTab, text=message, font=("Calibri", 25))

    # place objects
    image.grid(row=0, column=0)
    text.grid(row=1, column=0)


def EmbroideryTabFunct():
    def calculate():
        # collect inputs
        suppliedInput = int(supplied.entry.get())
        retailInput = int(retail.entry.get())
        numOrderedInput = int(numOrdered.entry.get())
        secondLocationInput = int(secondLocation.entry.get())
        titleInput = int(title.entry.get())
        setup = int(setup.entry.get())
        return

    def validate():
        retailPrice = int(retail.entry.get())
        numberOrdered = int(numOrdered.entry.get())

        if retailPrice < 0:
            price.entry.delete(0, "end")
            price.entry.insert(END, "Invalid Retail Price")

        elif numberOrdered < 1 or numberOrdered > 575:
            price.entry.delete(0, "end")
            price.entry.insert(END, "Invalid Number Ordered")

        else:
            calculate()

    # create objects
    spacer = ttk.Label(EmbroideryTab, text="")
    supplied = LabeledCheckbox("Supplied", 1, 0, EmbroideryTab)
    retail = LabeledEntry("Retail Price", 2, 1, EmbroideryTab)
    numOrdered = LabeledEntry("Number Ordered", 3, 12, EmbroideryTab)
    embroideryType = LabeledCombo("Type", embroideryTypeList, 4, 1, EmbroideryTab, width=embroideryTypeComboWidth)
    secondLocation = LabeledCheckbox("2nd Location", 5, 0, EmbroideryTab)
    title = LabeledCheckbox("Title/Name Added to 1st Location", 6, 0, EmbroideryTab)
    setup = LabeledCheckbox("Setup Fee", 7, 0, EmbroideryTab)
    price = LabeledEntry("Price", 9, 0, EmbroideryTab)

    # place objects
    spacer.grid(row=0, column=0, padx=200)
    supplied.place()
    retail.place()
    numOrdered.place()
    embroideryType.place()
    secondLocation.place()
    title.place()
    setup.place()
    price.place()

    # validate changes whenever a change is made
    supplied.value.trace("w", validate)
    retail.value.trace("w", validate)
    numOrdered.value.trace("w", validate)
    embroideryType.value.trace("w", validate)
    secondLocation.value.trace("w", validate)
    title.value.trace("w", validate)
    setup.value.trace("w", validate)


# start window# create fields
ScreenPrintTabFunct()
HomeTabFunt()
EmbroideryTabFunct()

tabControl.pack(expand=True, fill="both")  # display tabs

# display window
win.mainloop()
