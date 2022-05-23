from app.app_config import AppConfig
from app.controller.main_controller import MainController
from app.folder_manager import FolderManager
from app.view.main_window import MainWindow

from app.wrappers_factory import google_sheets_wrapper, google_contacts_wrapper

folder_manager = FolderManager(AppConfig.PROJECTS_ROOTDIR)


main_window = MainWindow()

main_controller = MainController(
    main_window, google_sheets_wrapper, google_contacts_wrapper, folder_manager)

main_window.set_controller(main_controller)

main_window.mainloop()
