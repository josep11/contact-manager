from tkinter import Tk
import tkinter.ttk as ttk

# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry
win.geometry("700x350")

# Set the default color of the window
win.config(background="#24f3f0")
win.config(bg="SkyBlue1")

ttk.Label(win, text="Hey There! Welcome to TutorialsPoint", font=("Helvetica 22 bold"), foreground="navy").pack()

win.mainloop()
