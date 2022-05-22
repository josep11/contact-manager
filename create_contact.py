#!/usr/bin/env python
from google_oauth_wrapper import get_credentials
from google.auth import credentials
from app.app_config import AppConfig
from app.utils import eprint
from app.exceptions import ContactAlreadyExistException
from app.google_contacts import create_contact_google_contacts
import argparse
import os
from sty import fg  # , bg, ef, rs

from app.app_config import AppConfig

from app.wrappers_factory import google_sheets_wrapper

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to create (wrapped it between brackets)")
    parser.add_argument("phone", type=str,
                        help="the phone of the contact to create (wrapped it between brackets)")
    args = parser.parse_args()
except ImportError:
    args = None


def open_directory(targetDirectory):
    from subprocess import call
    call(["open", targetDirectory])


def create_contact_folder(name):
    contact_dir = os.path.join(AppConfig.PROJECTS_ROOTDIR, name)
    if not os.path.exists(contact_dir):
        os.makedirs(contact_dir)
        print(f'Created directory: {contact_dir}')
    return contact_dir


if __name__ == "__main__":
    name = args.name
    phone = args.phone

    contact_dir = create_contact_folder(name)

    credentials = get_credentials(
        PROJECT_ROOT_DIR=os.getcwd(),
        APPLICATION_NAME=AppConfig.APPLICATION_NAME,
        SCOPES=AppConfig.SCOPES,
    )

    # Google Contacts
    try:
        create_contact_google_contacts(credentials, name, phone)
    except ContactAlreadyExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
        print('skipping Google Contacts creation')
    except BaseException as err:
        eprint(err)
        exit(1)

    # Google Sheet Customer Database list: add the customer
    rows = google_sheets_wrapper.get_rows()
    google_sheets_wrapper.add_customer(rows, name)

    # opening the directory in finder
    open_directory(contact_dir)
