# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

#单选框
import tkinter
from tkinter import *
import loggerReader

win = tkinter.Tk()
win.title("Logerr watch")
win.geometry('1000x1500')

text = loggerReader.get_1000_lines()

for tt in text:
    Label(win,
    text = tt,
    bg = 'grey',
    width = 1000,
    height = 4,
    wraplength = 1000,
    justify = 'left'
    ).pack()





win.mainloop()
