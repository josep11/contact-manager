import os
from google_oauth_wrapper import get_credentials

from app.constants import APPLICATION_NAME, SCOPES

if __name__ == "__main__":
    credentials = get_credentials(
        PROJECT_ROOT_DIR=os.getcwd(),
        APPLICATION_NAME=APPLICATION_NAME,
        SCOPES=SCOPES,
    )
