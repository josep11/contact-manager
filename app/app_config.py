
import os
from sty import fg  # , bg, ef, rs

from dotenv import load_dotenv
from app.utils import eprint
load_dotenv()

PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    eprint(fg.red + "Error: environments not set!" + fg.rs)
    exit(1)


class AppConfig:
    PROJECTS_ROOTDIR = PROJECTS_ROOTDIR

    APPLICATION_NAME = 'Contacts Sync Python'
    SCOPES = [
        'https://www.googleapis.com/auth/contacts',
        'https://www.googleapis.com/auth/spreadsheets',
    ]
