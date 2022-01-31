#!/usr/bin/env python
import sys
from google_oauth_wrapper import get_credentials
from google.auth import credentials
from app import google_sheets
from app import google_contacts
from app.utils import eprint
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
import argparse
import os

from send2trash import send2trash
from sty import fg  # , bg, ef, rs

from app.constants import APPLICATION_NAME, SCOPES

from dotenv import load_dotenv
load_dotenv()

PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    eprint(fg.red + "Error: environments not set!" + fg.rs)
    exit(1)

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to delete (wrapped it between brackets)")
    args = parser.parse_args()
except ImportError:
    args = None


def delete_contact_folder(name):
    contact_dir = os.path.join(PROJECTS_ROOTDIR, name)
    try:
        send2trash(contact_dir)
    except OSError as e:
        print("Error sending to trash: %s : %s" % (contact_dir, e.strerror))
        return

    print(f'Deleted directory for contact: {name}')


if __name__ == "__main__":
    name = args.name

    credentials = get_credentials(
        PROJECT_ROOT_DIR=os.getcwd(),
        APPLICATION_NAME=APPLICATION_NAME,
        SCOPES=SCOPES,
    )

    # Google Contacts Delete
    try:
        google_contacts.delete_contact_google_contacts(credentials, name)
    except ContactDoesNotExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
        print('skipping Google Contacts deletion as it doesn\'t exist')
    except BaseException as err:
        eprint(err)
        exit(1)

    # Delete Contact from Google Sheets
    try:
        rows = google_sheets.get_rows(credentials)
        google_sheets.delete_customer(credentials, rows, name)
    except ContactDoesNotExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
    except IndexError as err:
        raise err
    except BaseException as err:
        eprint(err)
        exit(1)

    # Sending it to the trash (not completely remove)
    delete_contact_folder(name)
