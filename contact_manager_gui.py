import sys
from sys import exit
from datetime import datetime

from app.logger_wrapper import logger
from app.app_config import AppConfig
from app.view.frames.create_contact_frame import CreateContactFrame

from app.view.main_window import MainWindow

from app.controller.main_controller import MainController

from app.wrappers_factory import google_sheets_wrapper, google_contacts_wrapper, google_drive_wrapper
# logger.info(AppConfig.APP_NAME)


def main():
    logger.info("#" * 20)
    logger.info(datetime.now().isoformat())
    logger.info("#" * 20)

    main_window = MainWindow()
    main_window.switch_view(CreateContactFrame)

    main_controller = MainController(
        main_window,
        google_sheets_wrapper,
        google_contacts_wrapper,
        google_drive_wrapper,
    )

    main_window.set_controller(main_controller)

    main_window.mainloop()


try:
    main()
except Exception as e:
    logger.error(e, exc_info=True)
    print(sys.exc_info())
