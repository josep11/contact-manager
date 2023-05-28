import sys
from app.controller.create_contact_controller import CreateContactController
from app.controller.delete_contact_controller import DeleteContactController
from app.google_drive_wrapper_interface import GoogleDriveWrapperInterface
from app.utils import open_browser
from app.view.frames.delete_contact_frame import DeleteContactFrame
from app.view.frames.create_contact_frame import CreateContactFrame
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
from app.google_contacts_wrapper_interface import GoogleContactsWrapperInterface
from app.google_sheets_wrapper_interface import GoogleSheetsWrapperInterface
# from app.view.main_window import MainWindow

from app.logger_wrapper import logger


class MainController:
    def __init__(self,
                 main_window,
                 google_sheets_wrapper: GoogleSheetsWrapperInterface,
                 google_contacts_wrapper: GoogleContactsWrapperInterface,
                 google_drive_wrapper_interface: GoogleDriveWrapperInterface
                 ):
        self.main_window = main_window
        self.google_sheets_wrapper = google_sheets_wrapper
        self.google_contacts_wrapper = google_contacts_wrapper
        self.google_drive_wrapper_interface = google_drive_wrapper_interface

    def create_contact(self, name: str, phone: str, extra: str = None) -> bool:
        """creates a contact

        Args:
            name (str):
            phone (str):
            extra (str):

        Returns:
            bool: True if successful
        """
        if not name or not phone:
            self.main_window.show_error(
                "Please fill the required fields (name and phone)")
            return

        # contact_dir = self.folder_manager.create_contact_folder(name)

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
                name,
                phone,
                extra,
            )
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
        # self.folder_manager.open_directory(contact_dir)

        # Google Drive Create Folder
        try:
            drive_folder_url = self.google_drive_wrapper_interface.create_folder(
                name)
        except BaseException as err:
            logger.error('failed creating drive directory for contact')
            ex_type, ex_value, ex_traceback = sys.exc_info()
            self.main_window.show_error(ex_value)
            return False

        # self.main_window.show_info("Contact Created Successfully")

        open_browser(drive_folder_url)
        return True

    def delete_contact(self, name: str) -> bool:
        if not name:
            self.main_window.show_error("Please fill all the fields")
            return False

        ran_ok = True

        # Google Contacts Delete
        try:
            self.google_contacts_wrapper.delete_contact_google_contacts(name)
        except ContactDoesNotExistException as err:
            msg = err.args
            self.main_window.show_error(msg)
            logger.error(err)
            ran_ok = False
        except BaseException as err:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            self.main_window.show_error(ex_value)
            ran_ok = False

        # Delete Contact from Google Sheets
        try:
            rows = self.google_sheets_wrapper.get_rows()
            self.google_sheets_wrapper.delete_customer(rows, name)
        except ContactDoesNotExistException as err:
            msg = err.args
            self.main_window.show_error(msg)
            logger.error(err)
        except IndexError as err:
            logger.critical(err)
            raise err
        except BaseException as err:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            self.main_window.show_error(ex_value)
            ran_ok = False

        # Google Drive Delete Folder
        try:
            self.google_drive_wrapper_interface.delete_folders_by_name(name)
        except BaseException as err:
            logger.error('failed deleting drive directory for contact')
            ex_type, ex_value, ex_traceback = sys.exc_info()
            logger.error(ex_traceback)
            self.main_window.show_error(ex_value)
            return False

        # Sending it to the trash (not completely remove)
        # self.folder_manager.delete_contact_folder(name)

        if ran_ok:
            self.main_window.show_info("Contact Deleted Successfully")
        return ran_ok

    def switch_to_delete_frame(self):
        self.delete_contact_controller = DeleteContactController(
            self.main_window,
            self,
        )
        self.main_window.switch_view(DeleteContactFrame)
        self.main_window.container.set_controller(
            self.delete_contact_controller)

    def switch_to_create_frame(self):
        self.create_contact_controller = CreateContactController(
            self.main_window,
            self,
        )
        self.main_window.switch_view(CreateContactFrame)
        self.main_window.container.set_controller(
            self.create_contact_controller)
