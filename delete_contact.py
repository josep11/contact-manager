#!/usr/bin/env python
from app import google_sheets_wrapper
from app import google_contacts_wrapper
from app.app_config import AppConfig
from app.utils import eprint
from app.exceptions import ContactAlreadyExistException, ContactDoesNotExistException
import argparse
import os

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


def delete_contact_folder(name):
    contact_dir = os.path.join(AppConfig.PROJECTS_ROOTDIR, name)
    try:
        send2trash(contact_dir)
    except OSError as e:
        print("Error sending to trash: %s : %s" % (contact_dir, e.strerror))
        return

    print(f'Deleted directory for contact: {name}')


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
    delete_contact_folder(name)
