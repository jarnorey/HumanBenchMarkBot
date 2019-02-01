import numpy as np
import cv2
import mss
import mss.tools
import pyautogui
from PIL import ImageGrab

i = 0

while True:
    print(i)
    img = pyautogui.screenshot()
    img.getpixel((200, 300))
    if pyautogui.pixelMatchesColor(200, 300, (43, 135, 209)) == True:
        print('Blue')
        pyautogui.click(200, 300)

    if pyautogui.pixelMatchesColor(200, 400, (75, 219, 106)) == True:
        print('Clicking...')
        pyautogui.click(200, 300)
        i = i + 1
        if i == 5:
            break


