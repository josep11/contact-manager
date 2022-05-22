import os
import unittest
from app.app_config import AppConfig
from app.google_sheets import get_rows

from google_oauth_wrapper import get_credentials


class GoogleSheetsWrapperText(unittest.TestCase):

    def test_get_rows(self):
        credentials = get_credentials(
            PROJECT_ROOT_DIR=os.getcwd(),
            APPLICATION_NAME=AppConfig.APPLICATION_NAME,
            SCOPES=AppConfig.SCOPES,
        )
        res = get_rows(credentials)
        self.assertGreaterEqual(len(res), 1)
