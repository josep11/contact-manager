
from __future__ import print_function
import httplib2

from apiclient import discovery
from app.install import get_credentials
from app.utils import transform_name, transform_phone


def get_contact_by_query(service, query):
    # The query will match everything that starts with that query but not middle parts
    results = service.people().searchContacts(
        pageSize=10, query=query, readMask="names").execute()

    if not results:
        return None

    resultsArr = results['results']
    print(f'trobats {len(resultsArr)} amb nom exacte {query}')
    return resultsArr


def create_service():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('people', 'v1', http=http,
                              discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')
    return service


def create_contact(service, name, phone):
    name = transform_name(name)
    phone = transform_phone(phone)

    print(f"about to create {name} with phone {phone}")

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
        "biographies": [
            {
                "value": "Created automatically by Contacts Creator",
            }
        ]
        # "emailAddresses": [
        #     {
        #         'value': 'myemail@gmail.com'
        #     }
        # ]
    }).execute()


def main(name, phone):
    try:
        service = create_service()
        contact = get_contact_by_query(service, transform_name(name))
        if contact is not None:
            print(f'contact ${phone} already exists')
            exit(1)

        create_contact(service, name, phone)
        print(f"Created contact {name} with phone {phone}")
    except Exception as e:
        raise e
