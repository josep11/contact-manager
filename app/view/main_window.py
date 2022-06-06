import tkinter as tk
import tkinter.messagebox
from app.app_config import AppConfig

from app.controller.main_controller import MainController
from app.view.frames.create_contact_frame import CreateContactFrame

# from views.home_view import HomeView
# from views.register_view import RegisterView
# from views.login_view import LoginView
# from views.user_view import UserView
# from views.deck_view import DeckView
# from views.card_view import CardView
from app.view.styles import *

from app.logger_wrapper import logger


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Contact Manager")
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        # self.container = tk.Frame(self)
        self.container = None
        # self.switch_view(CreateContactFrame)

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

    # def switch_view(self, container):
    #     # Saca el frame desde el diccionario
    #     frame = self.frames[container]
    #     # Pone enfrente la pantalla correspondiente
    #     frame.tkraise()

    def switch_view(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self.container is not None:
            self.container.destroy()
        self.container = new_frame
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(1, weight=1)

