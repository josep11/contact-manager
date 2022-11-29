#!/usr/bin/env python

from app.folder_manager import FolderManager
from app.utils import eprint
from app.exceptions import ContactAlreadyExistException
import argparse
from sty import fg  # , bg, ef, rs
from sys import exit

from app.app_config import AppConfig

from app.wrappers_factory import google_sheets_wrapper, google_contacts_wrapper

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to create (wrapped it between brackets)")
    parser.add_argument("phone", type=str,
                        help="the phone of the contact to create (wrapped it between brackets)")
    args = parser.parse_args()
except ImportError:
    args = None


folder_manager = FolderManager(AppConfig.PROJECTS_ROOTDIR)

if __name__ == "__main__":
    name = args.name
    phone = args.phone
    extra = args.extra or None

    # TODO: use drive wrapper
    contact_dir = folder_manager.create_contact_folder(name)

    # Google Contacts
    try:
        google_contacts_wrapper.create_contact_google_contacts(
            name,
            phone,
            extra,
        )
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
    folder_manager.open_directory(contact_dir)
