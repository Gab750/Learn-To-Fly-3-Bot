from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def longclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(20) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def start():
    time.sleep(10)
    pyautogui.moveTo(1562,104)
    click()
    sleep(1)
    pyautogui.moveTo(1563,104)
    click()
    sleep(1)
    longclick()




while True:
    start()
    sleep(100)
    click()









