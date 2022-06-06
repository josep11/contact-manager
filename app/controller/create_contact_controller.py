# from app.view.main_window import MainWindow


class CreateContactController:
    def __init__(self,
                 main_window,
                 main_controller
                 #  google_sheets_wrapper: GoogleSheetsWrapperInterface,
                 #  google_contacts_wrapper: GoogleContactsWrapperInterface,
                 #  folder_manager: FolderManager
                 ):
        self.main_window = main_window
        self.main_controller = main_controller

    def create_contact(self, name: str, phone: str) -> bool:
        return self.main_controller.create_contact(name, phone)

    def switch_to_delete_frame(self):
        self.main_controller.switch_to_delete_frame()
