
import os
from sty import fg  # , bg, ef, rs


from dotenv import load_dotenv
from app.utils import eprint
load_dotenv()

ENV = os.getenv('ENV')
ENV_FILE = ".env"

if "test" == ENV:
    print(f'overriding env vars with {ENV}')
    load_dotenv(".env.test", override=True)

PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    eprint(fg.red + "Error: environments not set!" + fg.rs)
    exit(1)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
if not SPREADSHEET_ID:
    eprint(fg.red + "Error: environments SPREADSHEET_ID not set!" + fg.rs)
    exit(1)


class AppConfig:
    PROJECTS_ROOTDIR = PROJECTS_ROOTDIR

    APPLICATION_NAME = 'Contacts Sync Python'
    SCOPES = [
        'https://www.googleapis.com/auth/contacts',
        'https://www.googleapis.com/auth/spreadsheets',
    ]
    SPREADSHEET_ID = SPREADSHEET_ID
