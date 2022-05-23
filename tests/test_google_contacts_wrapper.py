import unittest

from app.wrappers_factory import google_contacts_wrapper


class GoogleSheetsWrapperTest(unittest.TestCase):

    def test_get_rows(self):

        res = google_contacts_wrapper.get_contact_by_query("Jorge")
        self.assertGreaterEqual(len(res), 1)
