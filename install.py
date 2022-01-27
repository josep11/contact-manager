
from __future__ import print_function
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    # flags = parser.parse_args()
    # only the default arguments or it will fail if we call the script with our parameters
    flags = vars(parser.parse_args([]))
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/people.googleapis.com-python-quickstart.json
SCOPES = [
    'https://www.googleapis.com/auth/contacts',
    'https://www.googleapis.com/auth/spreadsheets',
]
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Contacts Sync Python'
CREDENTIAL_NAME = 'token.json'


def get_credentials():
    """Gets valid user credentials from storage.


    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Documentation on Oauth for Clients: https://docs.gspread.org/en/latest/oauth2.html

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('./')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    
    credential_path = os.path.join(credential_dir,
                                   CREDENTIAL_NAME)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store)  # , flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


if __name__ == "__main__":
    credentials = get_credentials()
