from app.utils import eprint
from app.exceptions import ContactAlreadyExistException
from app.create_contact import create_contact_google_contacts
import argparse
import os
from sty import fg  # , bg, ef, rs

from dotenv import load_dotenv
load_dotenv()

PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    eprint(fg.red + "Error: environments not set!" + fg.rs)
    exit(1)

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="the name of the contact to create")
    parser.add_argument("phone", type=str,
                        help="the phone of the contact to create")
    args = parser.parse_args()
except ImportError:
    args = None


def create_contact_folder():
    contact_dir = os.path.join(PROJECTS_ROOTDIR, name)
    if not os.path.exists(contact_dir):
        os.makedirs(contact_dir)


if __name__ == "__main__":
    name = args.name
    phone = args.phone

    create_contact_folder()

    try:
        create_contact_google_contacts(name, phone)
    except ContactAlreadyExistException as err:
        msg = err.args
        eprint(fg.red + msg[0] + fg.rs)
        exit(1)
    except BaseException as err:
        eprint(err)
        exit(1)

