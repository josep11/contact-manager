import tkinter as tk
from tkinter import Menu

import tkinter as tk

from app.view.frames.home_view import HomeView

# from views.home_view import HomeView
# from views.register_view import RegisterView
# from views.login_view import LoginView
# from views.user_view import UserView
# from views.deck_view import DeckView
# from views.card_view import CardView
from app.view.styles import *


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Contact Manager")
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        # self.container = tk.Frame(self)
        self.container = None

        # self.container.pack(
        #     # side=tk.TOP,
        #     # fill=tk.BOTH,
        #     side='top',
        #     fill='both',
        #     expand=True
        # )
        # self.container.configure(background='blue')
        # self.container.grid_columnconfigure(0, weight=1)
        # self.container.grid_rowconfigure(0, weight=1)
        # # Inicializamos el diccionario de los frames
        # self.frames = {}
        #
        # # Creamos una tupla con las clases que representan las pantallas para poder iterar sobre ellas
        # screens = (HomeView, RegisterView, LoginView, UserView, DeckView, CardView)
        # for screen in screens:
        #     # Creamos cada frame a partir de la clase de panatalla
        #     # !Aqui pasamos tanto el propio container donde se incrustan como el propio manager donde nos encontramos
        #     frame = screen(self.container, self)
        #     # Añadimos nuestro frame al diccionario de frames en la posicion de la pantalla correspondiente
        #     # !Cada frame es añadida al diccionario donde la key es la clase y el value es la instancia de la clase
        #     self.frames[screen] = frame
        #     # Colacamos los frames en formato grid ocupando el espacio en las 4 direcciones
        #     frame.grid(row=0, column=0, sticky=tk.NSEW)
        # # Llamamos al metodo de mostrar pantalla con la pantalla HomeScreen
        self.switch_view(HomeView)

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

    # Handle Views
    def home_tab(self):
        self.switch_view(HomeView)

    # def register_tab(self):
    #     self.switch_view(RegisterView)

    # def login_tab(self):
    #     self.switch_view(LoginView)

    # def user_tab(self):
    #     self.switch_view(UserView)

    # def deck_tab(self):
    #     self.switch_view(DeckView)

    # def card_tab(self):
    #     self.switch_view(CardView)
