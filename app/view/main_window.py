import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from turtle import bgcolor
from app.app_config import AppConfig

from app.controller.main_controller import MainController
from app.view.frames.create_contact_frame import CreateContactFrame

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
        s.configure('TButton', foreground=TEXT_COLOR )

        # https://tkdocs.com/tutorial/styles.html
        # https://docs.python.org/es/3.10/library/tkinter.ttk.html

        # ('aqua', 'clam', 'alt', 'default', 'classic')
        s.theme_use('clam')
        # s.configure('JS.TButton',
        #             # font=('Helvetica', 12),
        #             overrelief=tk.RIDGE,
        #             foreground='black', 
        #             background='blue',
        #             # foreground=COMPONENT_COLOR
        #             )


    def set_controller(self, controller: MainController):
        self.controller = controller
        if self.container:
            self.container.set_controller(controller)
        else:
            logger.error(
                f"should have container initialised before calling set_controller")

    def show_error(self, msg: str):
        tkinter.messagebox.showerror(title=AppConfig.APP_NAME, message=msg)

    def show_info(self, msg: str):
        tkinter.messagebox.showinfo(title=AppConfig.APP_NAME, message=msg)

    def switch_view(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self.container is not None:
            self.container.destroy()
        self.container = new_frame
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(1, weight=1)
