import pywinctl as pwc
import time
import pyautogui
import numpy as np
import cv2 as cv

time.sleep(2)
source = np.array(pyautogui.screenshot(region=(5585,1172,560,228)))
source = cv.cvtColor(source, cv.COLOR_RGB2BGR)
cv.imshow("test",source)
cv.waitKey()