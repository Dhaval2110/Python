# Automating webbrowser applications

# Global Imports
import webbrowser
import tkinter as tk

#Global variables
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#root=tk.Tk()

# # 1. Automation Youtube
# # webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=U5GPvBErVVc") #Open URL in Chrome

# # 2. Facebook automation
# webbrowser.get(chrome_path).open("https://www.facebook.com/")                   # If already logged in :(


### TKINTER EXAMPLES #######

#1. Normal window widget

# w = tk.Label(root, text="Hello Tkinter!")
# w.pack()

# root.mainloop()

#2. Picture widget
# logo = tk.PhotoImage(file="MCC.gif")
# w1 = tk.Label(root, image=logo).pack(side="right")
# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface 
# exists to allow additional image file
# formats to be added easily."""
# w2 = tk.Label(root, 
#               justify=tk.LEFT,
#               padx = 10, 
#               text=explanation).pack(side="left")
# root.mainloop()

#3. Dynmical content in label

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()