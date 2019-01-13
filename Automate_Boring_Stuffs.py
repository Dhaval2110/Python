# Automating webbrowser applications

# Global Imports
import webbrowser

#Global variables
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# 1. Automation Youtube
# webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=U5GPvBErVVc") #Open URL in Chrome

# 2. Facebook automation
webbrowser.get(chrome_path).open("https://www.facebook.com/")                   # If already logged in :(

