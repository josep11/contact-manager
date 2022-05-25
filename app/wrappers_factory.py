import os
import sys
from app.app_config import AppConfig
from app.google_contacts_wrapper import GoogleContactsWrapper
from app.google_sheets_wrapper import GoogleSheetsWrapper

try:
    # TODO: move back to outside of try block
    from app.logger_wrapper import logger
    from app.utils import get_bundle_dir

    from google_oauth_wrapper import get_credentials

    bundle_dir = get_bundle_dir()

    logger.info(f"bundle_dir = {bundle_dir}\n")
    print(f"bundle_dir = {bundle_dir}\n")

    credentials = get_credentials(
        APP_NAME=AppConfig.APP_NAME,
        PROJECT_ROOT_DIR=bundle_dir,
        SCOPES=AppConfig.SCOPES,
    )

    google_sheets_wrapper = GoogleSheetsWrapper(
        credentials, AppConfig.SPREADSHEET_ID)

    google_contacts_wrapper = GoogleContactsWrapper(credentials)

except Exception as e:
    logger.error(e, exc_info=True)
    print(sys.exc_info())
