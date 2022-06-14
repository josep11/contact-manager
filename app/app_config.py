import os
from sty import fg  # , bg, ef, rs
from sys import exit

from dotenv import load_dotenv
from app.utils import get_bundle_dir

from os import path

from app.logger_wrapper import logger

path_to_env = path.abspath(path.join(get_bundle_dir(), '.env'))
load_dotenv(path_to_env)

ENV = os.getenv('ENV')

isDev = False

if "test" == ENV:
    print(f'overriding env vars with {ENV}')
    load_dotenv(".env.test", override=True)

if "dev" == ENV:
    print(f'overriding env vars with {ENV}')
    load_dotenv(".env.dev", override=True)
    isDev = ENV == "dev"

PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    logger.critical(fg.red + "Error: environments not set!" + fg.rs)
    exit(1)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
if not SPREADSHEET_ID:
    logger.critical(
        fg.red + "Error: environments SPREADSHEET_ID not set!" + fg.rs)
    exit(1)


class AppConfig:
    PROJECTS_ROOTDIR = PROJECTS_ROOTDIR

    # If modifying these scopes, delete the file token.json.
    SCOPES = [
        'https://www.googleapis.com/auth/contacts',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    APP_NAME = "ContactManager"
    SPREADSHEET_ID = SPREADSHEET_ID

    GOOGLE_DRIVE_ROOT_PROJECT_DIR_ID = "1uZNaMYudSyY9m0miNrhKUnnYjWh7xz1_"

    isDev = isDev
