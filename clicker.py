import pyautogui
from time import sleep

coordinates = (730, 465)
color = [(1, (84, 174, 72, 255))]

sleep(2)

while True:
    sleep(1)
    s = pyautogui.screenshot(region=(745, 420, 1, 1))
    if s.getcolors() == color:
        pyautogui.click(coordinates)
        sleep(5)
