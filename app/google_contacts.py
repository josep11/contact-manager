
from __future__ import print_function

from googleapiclient.discovery import build
from app.exceptions import ContactAlreadyExistException
from app.utils import eprint, transform_name, transform_phone


def get_contact_by_query(service, query):
    # first we should warm un the cache
    # GET /v1/people:searchContacts?query=&readMask=names,emailAddresses HTTP/1.1
    service.people().searchContacts(
        query="", readMask="names,emailAddresses").execute()

    # There is a bug in the service and it takes some 30 seconds to be able to find a newly added contact

    # The query will match everything that starts with that query but not middle parts
    results = service.people().searchContacts(
        pageSize=10, query=query, readMask="names").execute()

    if not results:
        return None

    resultsArr = results['results']
    print(f'trobats {len(resultsArr)} amb nom exacte {query}')
    return resultsArr


def create_service(credentials):
    service = build('people', 'v1', credentials=credentials)
    return service


def create_contact(service, name, phone):
    print(f"About to create {name} with phone {phone}")

    service.people().createContact(body={
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


def create_contact_google_contacts(credentials, name, phone):
    name = transform_name(name)
    phone = transform_phone(phone)

    service = create_service(credentials)
    contact = get_contact_by_query(service, name)
    if contact is not None:
        raise ContactAlreadyExistException(
            f'Error: contact with name "{name}" already exists')

    create_contact(service, name, phone)
    print(f"Created contact {name} with phone {phone}")
    # except BaseException as err:
    #     msg = err.args
    #     eprint(msg)
