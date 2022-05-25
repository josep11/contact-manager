#!/usr/bin/env python
from app import google_sheets_wrapper
from app import google_contacts_wrapper
from app.app_config import AppConfig
from app.folder_manager import FolderManager
from app.utils import eprint
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
import argparse
import os
from sys import exit

from send2trash import send2trash
from sty import fg  # , bg, ef, rs

from app.wrappers_factory import google_sheets_wrapper, google_contacts_wrapper

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to delete (wrapped it between brackets)")
    args = parser.parse_args()
except ImportError:
    args = None

folder_manager = FolderManager(AppConfig.PROJECTS_ROOTDIR)

if __name__ == "__main__":
    name = args.name

    # Google Contacts Delete
    try:
        google_contacts_wrapper.delete_contact_google_contacts(name)
    except ContactDoesNotExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
        print('skipping Google Contacts deletion as it doesn\'t exist')
    except BaseException as err:
        eprint(err)
        exit(1)

    # Delete Contact from Google Sheets
    try:
        rows = google_sheets_wrapper.get_rows()
        google_sheets_wrapper.delete_customer(rows, name)
    except ContactDoesNotExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
    except IndexError as err:
        raise err
    except BaseException as err:
        eprint(err)
        exit(1)

    # Sending it to the trash (not completely remove)
    folder_manager.delete_contact_folder(name)
