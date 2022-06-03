import sys
from app.exceptions import ContactAlreadyExistException
from app.folder_manager import FolderManager
from app.google_contacts_wrapper_interface import GoogleContactsWrapperInterface
from app.google_sheets_wrapper_interface import GoogleSheetsWrapperInterface
# from app.view.main_window import MainWindow


class DeleteContactController:
    def __init__(self,
                 main_window,
                 main_controller
                 #  google_sheets_wrapper: GoogleSheetsWrapperInterface,
                 #  google_contacts_wrapper: GoogleContactsWrapperInterface,
                 #  folder_manager: FolderManager
                 ):
        self.main_window = main_window
        self.main_controller = main_controller

    def delete_contact(self, nom: str):
        return self.main_controller.delete_contact(nom)
    
    def switch_to_create_frame(self):
        self.main_controller.switch_to_create_frame()