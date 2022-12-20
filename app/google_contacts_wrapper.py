
from __future__ import print_function

from googleapiclient.discovery import build
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
from app.google_contacts_wrapper_interface import GoogleContactsWrapperInterface
from app.utils import transform_name, transform_phone


class GoogleContactsWrapper(GoogleContactsWrapperInterface):

    def __init__(self, credentials):
        self.credentials = credentials
        self.service = build('people', 'v1', credentials=credentials)

    def get_contact_by_query(self, query) -> list:
        # first we should warm un the cache
        # GET /v1/people:searchContacts?query=&readMask=names,emailAddresses HTTP/1.1
        fields="names,emailAddresses,clientData,userDefined,metadata,biographies"
        self.service.people().searchContacts(
            query="", readMask=fields).execute()

        # There is a bug in the self.service and it takes some 30 seconds to be able to find a newly added contact

        # The query will match everything that starts with that query but not middle parts
        results = self.service.people().searchContacts(
            pageSize=10, query=query, readMask=fields).execute()

        if not results:
            return None

        resultsArr = results['results']
        
        print(f'trobats {len(resultsArr)} amb nom exacte {query}')
        
        return resultsArr

    def _create_contact(self, name: str, phone: str, extra: str = None):
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
            "biographies": [
                {
                    'value': extra or ''
                }
            ]
            # "emailAddresses": [
            #     {
            #         'value': 'myemail@gmail.com'
            #     }
            # ]
        }).execute()

    def create_contact_google_contacts(self, name: str, phone: str, extra: str = None):
        name = transform_name(name)
        phone = transform_phone(phone)

        contact = self.get_contact_by_query(name)
        if contact is not None:
            raise ContactAlreadyExistException(
                f'Error: contact with name "{name}" already exists')

        self._create_contact(name, phone, extra)

        print(f"\nCreated contact {name} with phone {phone}\n")
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

        print(f'\ndeleting {resourceName} from Google Contacts\n')

        self.service.people().deleteContact(resourceName=resourceName).execute()
