import pyautogui as gui
import time
# import webbrowser as wb
# wb.open('https://www.google.com')
time.sleep(30)
for i in range(5):
    gui.typewrite('Hello World')
    gui.press('enter')