from pywinauto.application import Application
import pywinauto
import pyautogui
import time

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe" ')
# qwidget = app.QWidget
# qwidget.Wait('ready')
# qwidget.Click()
time.sleep(2)
pyautogui.hotkey('ctrl','n')
time.sleep(2)
pyautogui.typewrite('Hello world!') 
time.sleep(2)
pyautogui.press('enter')
