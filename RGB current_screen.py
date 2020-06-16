import pyautogui
from os import system

while True:
    screenshot = pyautogui.screenshot()
    screendata = list(screenshot.getdata())
    data_len = len(screendata)

    red = 0
    green = 0
    blue = 0

    for pix in screendata:
        r, g, b = pix
        red += r
        green += g
        blue += b
    system('cls')
    print(f'Average RGB: ({red/data_len}, {green/data_len}, {blue/data_len})')