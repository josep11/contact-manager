import os
from google_oauth_wrapper import get_credentials

from app.app_config import AppConfig


if __name__ == "__main__":
    credentials = get_credentials(
        PROJECT_ROOT_DIR=os.getcwd(),
        APP_NAME=AppConfig.APP_NAME,
        SCOPES=AppConfig.SCOPES,
    )
