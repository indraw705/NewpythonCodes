import pyautogui as spam
import time

limit = 50
msg = "I LOVE YOU PANU "
time.sleep(10)

i = 0
while i < limit:
    spam.typewrite(msg)
    spam.press('Enter')
    i += 1
