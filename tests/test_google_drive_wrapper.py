import unittest

from app.wrappers_factory import google_drive_wrapper
import requests


contact_name = "unit_test_google_drive"


class GoogleDriveWrapperTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        # self.directory_names_created = []
        super(GoogleDriveWrapperTest, self).__init__(*args, **kwargs)

    def test_create_folder(self):
        directory_url = google_drive_wrapper.create_folder(contact_name)

        self.assertIsInstance(directory_url, str)
        self.assert_url_is_public(directory_url)

    def assert_url_is_public(self, url: str):
        response = requests.get(url)
        self.assertTrue(response.ok, "URL is not public or not valid")

    # def test_delete_file(self):
    #     google_drive_wrapper.delete_file_by_name(contact_name)

    def tearDown(self):
        google_drive_wrapper.delete_file_by_name(contact_name)
