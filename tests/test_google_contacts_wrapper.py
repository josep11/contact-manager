import unittest
from app.logger_wrapper import logger
from app.utils import random_with_N_digits

from app.wrappers_factory import google_contacts_wrapper
import time


class GoogleSheetsWrapperTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        # the entries created in the people api
        self.names_of_contacts_created = []
        super(GoogleSheetsWrapperTest, self).__init__(*args, **kwargs)

    def test_get_contact_by_query(self):

        res = google_contacts_wrapper.get_contact_by_query("Jorge")
        # res = google_contacts_wrapper.get_contact_by_query("Fl AA_DUMMY_TEST_CONTACT735944")
        self.assertGreaterEqual(len(res), 1)

    def test_create_contact_google_contacts(self):

        # will potentially generate shit data
        name = 'AA_DUMMY_TEST_CONTACT' + str(random_with_N_digits(9))
        phone = '666666666'
        extra = '@' + name

        self.names_of_contacts_created.append(name)

        res = google_contacts_wrapper.create_contact_google_contacts(
            name,
            phone,
            extra,
        )

        time.sleep(30)

        res = google_contacts_wrapper.get_contact_by_query(name)
        self.assertIsNotNone(res, f'contact with name {name} not found')
        self.assertGreaterEqual(len(res), 1)
        # check biography
        contact = res[0]
        person = contact['person']
        # print (json.dumps(person, indent=4))
        self.assertGreaterEqual(len(person['biographies']), 1)
        notes = person['biographies'][0]['value']
        self.assertEqual(extra, notes)

        # clean up

    def tearDown(self):
        for name in self.names_of_contacts_created:
            logger.info("cleaning up contact with name {name}")
            # delete the record from contacts api
            google_contacts_wrapper.delete_contact_google_contacts(name)
