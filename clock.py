#!/usr/bin/env python3
import sys
from tkinter import *
import time

def tick():
    time_string = time.strftime("%H:%M:%S") # get current local time
    clock.config(text=time_string)           # if time_string changes, update
    clock.after(200, tick)

root = Tk()
clock = Label(root, font = ("Vulf Mono Code", 200, "bold"), bg = "white")
clock.grid(row=0, column=1)
tick() # call function
root.mainloop()
