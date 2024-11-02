import cv2 as cv
from mss.linux import MSS as mss
import numpy as np
from PIL import Image

def get_color(img):
    avg_color_per_row = np.average(img, axis=0)
    avg_colors = np.average(avg_color_per_row, axis=0)
    int_averages = np.array(avg_colors, dtype=np.uint8)
    return int_averages

with mss() as sct:
    uc_monitor = {"top": 1300, "left": 6005, "width": 80, "height": 80}
    ls_monitor = {"top": 1300, "left": 5675, "width": 80, "height": 80}
    ib_monitor = {"top": 1300, "left": 5757, "width": 80, "height": 80}
    ia_monitor = {"top": 1300, "left": 5839, "width": 80, "height": 80}

    uc_color = get_color(sct.grab(uc_monitor))[:-1]
    ls_color = get_color(sct.grab(ls_monitor))[:-1]
    ib_color = get_color(sct.grab(ib_monitor))[:-1]
    ia_color = get_color(sct.grab(ia_monitor))[:-1]

    print("UC Color: ", uc_color)
    print("LS Color: ", ls_color)
    print("IB Color: ", ib_color)
    print("IA Color: ", ia_color)

