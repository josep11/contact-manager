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
            self, text="Create Contact", width=8, highlightthickness=0, command=lambda: self.manager.register_tab()
        )
        self.register_button.grid(row=0, column=0)
        self.user_button = tk.Button(
            self, text="Delete Contact", width=8, highlightthickness=0, command=lambda: self.manager.login_tab()
        )
        self.user_button.grid(row=2, column=0)
