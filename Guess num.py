import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
mynum=random.randint(0,10)
print(mynum)
def button_ok():
    guess=int(spinnum.get())
    if mynum==guess:
        messagebox.showinfo(title="Congrats",message="you won")
    else:
        messagebox.showinfo(title="Sorry",message="you lost")
def button_cancel():
    window.destroy()
window = tk.Tk()
window.title("welcome to guess number")
window.configure(bg="pink")
window.geometry("900x250")
window.tk.call("tk","scaling",2)
lbl=tk.Label(window,text="Guess the number",bg="pink")
lbl.grid(row=0,column=0,padx=80,pady=80)
button=tk.Button(window,text="ok",bg="grey",command= button_ok)
button.grid(row=1,column=1,padx=10,pady=10)
button1=tk.Button(window,text="cancel",bg="grey",command=button_cancel)
button1.grid(row=1,column=0,padx=10,pady=10)
spinnum=tk.Spinbox(window,from_=0,to=10,fg="grey")
spinnum.grid(row=0,column=1,padx=10,pady=10)
window.mainloop()



