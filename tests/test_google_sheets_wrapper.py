import unittest

from app.wrappers_factory import google_sheets_wrapper


class GoogleSheetsWrapperTest(unittest.TestCase):

    def test_get_rows(self):

        res = google_sheets_wrapper.get_rows()
        self.assertGreaterEqual(len(res), 1)
