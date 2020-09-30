import sys
from tkinter import *

import ctypes

# changing the system DPI awareness
ctypes.windll.shcore.SetProcessDpiAwareness(1)


myApp = Tk()
myApp.title('My App')

myApp.geometry('400x400+350+340')

label = Label(text='My Label', fg ='red', bg = 'white').grid(row=0,column=0,sticky=E)

myApp.mainloop()
