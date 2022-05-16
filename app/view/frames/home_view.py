import tkinter as tk
from app.view.styles import *
import tkinter.ttk as ttk


class HomeView(tk.Frame):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.create_widgets()

    def create_widgets(self):
        self.register_button = tk.Button(
            self, text="Register", width=8, highlightthickness=0, command=lambda: self.manager.register_tab()
        )
        self.register_button.grid(row=0, column=0)
        self.user_button = tk.Button(
            self, text="Login", width=8, highlightthickness=0, command=lambda: self.manager.login_tab()
        )
        self.user_button.grid(row=1, column=0)
        # greeting = tk.Label(text="Hello, Tkinter", color=TEXT_COLOR)

        label = tk.Label(
            text="Hello, Tkinter",
            foreground="yellow",  # Set the text color to white
            background="black",  # Set the background color to black
        )
        label.pack()
