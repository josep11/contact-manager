import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Menu, messagebox
from app import get_version
from app.app_config import AppConfig


from app.view.styles import *

from app.logger_wrapper import logger


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Contact Manager")
        self.config(padx=50, pady=50,
                    bg=BACKGROUND_COLOR
                    )
        self.container = None
        s = ttk.Style()
        s.configure('.',
                    # font=('Helvetica', 12, 'bold'),
                    background=BACKGROUND_COLOR,
                    )
        s.configure('TButton', foreground=TEXT_COLOR)

        # https://tkdocs.com/tutorial/styles.html
        # https://docs.python.org/es/3.10/library/tkinter.ttk.html

        s.theme_use('clam') #('aqua', 'clam', 'alt', 'default', 'classic')

        menubar = Menu(self)
        # Adding Help Menu
        self.create_help_submenu(menubar, get_version())
        # Adding to the view
        self.config(menu=menubar)

    def create_help_submenu(self, menubar: tk.Menu, version: str) -> tk.Menu:
        help_ = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_)
        # TODO: do it though the official "About" submenu on the app that OS X provides
        about_info = f"{AppConfig.APP_NAME} v{version}"
        # messagebox.showinfo("Versió", about_info)
        help_.add_command(label="About", command=lambda: messagebox.showinfo("Versió", about_info))

    def set_controller(self, controller):
        self.controller = controller
        if self.container:
            self.container.set_controller(controller)
        else:
            logger.error(
                f"should have container initialised before calling set_controller")

    def show_error(self, msg: str):
        messagebox.showerror(title=AppConfig.APP_NAME, message=msg)

    def show_info(self, msg: str):
        messagebox.showinfo(title=AppConfig.APP_NAME, message=msg)

    def switch_view(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self.container is not None:
            self.container.destroy()
        self.container = new_frame
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
