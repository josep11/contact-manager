import tkinter as tk
import tkinter.ttk as ttk
# from app.controller.main_controller import MainController
from app.utils import random_with_N_digits
from app.view.frames.frame_constants import DummyContact

from app.view.styles import *
from app.app_config import AppConfig


class CreateContactFrame(tk.Frame):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.config(padx=50, pady=50,
                    bg=BACKGROUND_COLOR,
                    )
        self.create_widgets()
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def created_button_pressed(self):
        if self.controller.create_contact(
                self.nom.get(),
                self.telefon.get(),
                self.extra.get()
        ):
            self.clear_entries()

    def clear_entries(self):
        self.nom.delete(0, tk.END)
        self.telefon.delete(0, tk.END)
        self.extra.delete(0, tk.END)

    def switch_to_delete_frame(self):
        self.controller.switch_to_delete_frame()

    def create_widgets(self):

        # username
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.nom = ttk.Entry(self)
        self.nom.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        self.telefon_label = ttk.Label(self, text="Telefon:")
        self.telefon_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.telefon = ttk.Entry(self)
        self.telefon.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # extra
        self.extra_label = ttk.Label(self, text="Extra Info:")
        self.extra_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.extra = ttk.Entry(self)
        self.extra.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        if AppConfig.isDev:
            self.nom.insert(0, DummyContact.name)
            self.telefon.insert(0, DummyContact.phone)
            self.extra.insert(0, DummyContact.extra)

        # login button
        create_contact_button = ttk.Button(
            self, text="Create Contact", command=self.created_button_pressed)
        create_contact_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5,
                                   )

        # go to delete button
        go_to_delete_button = ttk.Button(
            self, text="Go To Delete", command=self.switch_to_delete_frame)
        go_to_delete_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5,
                                 )
