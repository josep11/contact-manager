
from __future__ import print_function

from googleapiclient.discovery import build
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
from app.google_contacts_wrapper_interface import GoogleContactsWrapperInterface
from app.utils import eprint, transform_name, transform_phone


class GoogleContactsWrapper(GoogleContactsWrapperInterface):

    def __init__(self, credentials):
        self.credentials = credentials
        self.service = build('people', 'v1', credentials=credentials)

    def get_contact_by_query(self, query) -> list:
        # first we should warm un the cache
        # GET /v1/people:searchContacts?query=&readMask=names,emailAddresses HTTP/1.1
        self.service.people().searchContacts(
            query="", readMask="names,emailAddresses").execute()

        # There is a bug in the self.service and it takes some 30 seconds to be able to find a newly added contact

        # The query will match everything that starts with that query but not middle parts
        results = self.service.people().searchContacts(
            pageSize=10, query=query, readMask="names").execute()

        if not results:
            return None

        resultsArr = results['results']
        print(f'trobats {len(resultsArr)} amb nom exacte {query}')
        return resultsArr

    def _create_contact(self, name: str, phone: str):
        print(f"About to create {name} with phone {phone}")

        self.service.people().createContact(body={
            "names": [
                {
                    "givenName": name
                }
            ],
            "phoneNumbers": [
                {
                    'value': phone
                }
            ],
            # "biographies": [
            #     {
            #         "value": "Created automatically by Contacts Manager",
            #     }
            # ]
            # "emailAddresses": [
            #     {
            #         'value': 'myemail@gmail.com'
            #     }
            # ]
        }).execute()

    def create_contact_google_contacts(self, name: str, phone: str):
        name = transform_name(name)
        phone = transform_phone(phone)

        contact = self.get_contact_by_query(name)
        if contact is not None:
            raise ContactAlreadyExistException(
                f'Error: contact with name "{name}" already exists')

        self._create_contact(name, phone)
        print(f"Created contact {name} with phone {phone}")
        # except BaseException as err:
        #     msg = err.args
        #     eprint(msg)

    def delete_contact_google_contacts(self, name: str):
        name = transform_name(name)

        contact = self.get_contact_by_query(name)
        if contact is None:
            raise ContactDoesNotExistException(
                f'Error: contact with name "{name}" does not exists')

        resourceName = contact[0]['person']['resourceName']

        print(f'deleting {resourceName} from Google Contacts')

        self.service.people().deleteContact(resourceName=resourceName).execute()
