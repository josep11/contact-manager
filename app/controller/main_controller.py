import sys
from app.exceptions import ContactAlreadyExistException
from app.folder_manager import FolderManager
from app.google_contacts_wrapper_interface import GoogleContactsWrapperInterface
from app.google_sheets_wrapper_interface import GoogleSheetsWrapperInterface
# from app.view.main_window import MainWindow

from app.logger_wrapper import logger


class MainController:
    def __init__(self,
                 main_window,
                 google_sheets_wrapper: GoogleSheetsWrapperInterface,
                 google_contacts_wrapper: GoogleContactsWrapperInterface,
                 folder_manager: FolderManager
                 ):
        self.main_window = main_window
        self.google_sheets_wrapper = google_sheets_wrapper
        self.google_contacts_wrapper = google_contacts_wrapper
        self.folder_manager = folder_manager

    def create_contact(self, name: str, phone: str) -> bool:
        """creates a contact

        Args:
            name (str): 
            phone (str): 

        Returns:
            bool: True if successful
        """
        if not name or not phone:
            self.main_window.show_error("Please fill all the fields")
            return

        contact_dir = self.folder_manager.create_contact_folder(name)

        # Google Sheet Customer Database list: add the customer
        try:
            rows = self.google_sheets_wrapper.get_rows()
            self.google_sheets_wrapper.add_customer(rows, name)
        except BaseException as err:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            self.main_window.show_error(ex_value)
            return False

        # Google Contacts
        try:
            self.google_contacts_wrapper.create_contact_google_contacts(
                name, phone)
        except ContactAlreadyExistException as err:
            msg = err.args
            self.main_window.show_error(msg)
            logger.info(
                'ContactAlreadyExistException: skipping Google Contacts creation')
            return
        except BaseException as err:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            self.main_window.show_error(ex_value)
            return False

        # opening the directory in finder
        self.folder_manager.open_directory(contact_dir)

        self.main_window.show_info("Contact Created Successfully")
        return True
