import os
from app.app_config import AppConfig
from app.google_sheets_wrapper import GoogleSheetsWrapper
from google_oauth_wrapper import get_credentials

credentials = get_credentials(
    PROJECT_ROOT_DIR=os.getcwd(),
    APPLICATION_NAME=AppConfig.APPLICATION_NAME,
    SCOPES=AppConfig.SCOPES,
)

google_sheets_wrapper = GoogleSheetsWrapper(credentials)