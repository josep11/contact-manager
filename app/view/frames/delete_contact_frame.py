import tkinter as tk
import tkinter.ttk as ttk
from app.view.frames.frame_constants import DummyContact

from app.view.styles import *
from app.app_config import AppConfig


class DeleteContactFrame(tk.Frame):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.config(padx=50, pady=50,
                    bg=BACKGROUND_COLOR
                    )
        self.create_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def delete_button_pressed(self):
        if self.controller.delete_contact(self.nom.get()):
            self.clear_entries()


    def clear_entries(self):
        self.nom.delete(0, tk.END)

    def switch_to_create_frame(self):
        self.controller.switch_to_create_frame()
    
    def create_widgets(self):

        # username
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.nom = ttk.Entry(self)
        self.nom.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        if AppConfig.isDev:
            self.nom.insert(0, DummyContact.name)

        # login button
        create_contact_button = ttk.Button(
            self, text="Delete Contact", command=self.delete_button_pressed)
        create_contact_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5,
                                   )


         # go to delete button
        go_to_create_button = ttk.Button(
            self, text="Go To Create", command=self.switch_to_create_frame)
        go_to_create_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5,
                                   )