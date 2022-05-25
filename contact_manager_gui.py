import logging
import os
import sys
from sys import exit

from app.logger_wrapper import logger
from app.app_config import AppConfig

# logger.info(AppConfig.APP_NAME)

# TODO: move outside of main again
def main():
    from app.view.main_window import MainWindow

    from app.controller.main_controller import MainController
    from app.folder_manager import FolderManager

    from app.wrappers_factory import google_sheets_wrapper, google_contacts_wrapper

    folder_manager = FolderManager(AppConfig.PROJECTS_ROOTDIR)
    main_window = MainWindow()

    main_controller = MainController(
        main_window, google_sheets_wrapper, google_contacts_wrapper, folder_manager)

    main_window.set_controller(main_controller)

    main_window.mainloop()


try:
    main()
except Exception as e:
    logger.error(e, exc_info=True)
    print(sys.exc_info())
