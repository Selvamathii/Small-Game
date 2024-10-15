# Digital clock

import tkinter as tk
import time as t
from tkinter import *
from time import *

def cancel_button():
    window.destroy()

def timer():
    x=t.strftime("%H:%M:%S %p",t.localtime())
    lbl.configure(text=x)
    lbl.after(1000,timer)
    
window=tk.Tk()
window.title("Digital clock")
window.geometry("500x170")
window.tk.call("tk","scaling",3.0)
window.configure(bg="#44575a")

txt=tk.Label(window,text="Digtal Clock",fg="#5dc3d3",bg="#44575a")
txt.pack(padx=40,pady=20)
lbl = Label(window, font=('Lemon', 23,'bold'),foreground='#18d4f1',bg="#44575a")
lbl.pack(anchor="center")



timer()
window.mainloop()

# you can check with my laptop timer on below of the screen 
# The END !!!





