import os
from sty import fg  # , bg, ef, rs
from sys import exit

from dotenv import load_dotenv
from app.utils import get_env_file_path

load_dotenv(get_env_file_path())

from app.logger_wrapper import logger

ENV = os.getenv('ENV')

isDev = False

if "test" == ENV:
    print(f'overriding env vars with {ENV}')
    load_dotenv(".env.test", override=True)

if "dev" == ENV:
    print(f'overriding env vars with {ENV}')
    load_dotenv(".env.dev", override=True)
    isDev = ENV == "dev"


def die(msg: str):
    logger.critical(msg)
    exit(1)


PROJECTS_ROOTDIR = os.getenv("PROJECTS_ROOTDIR")
if not PROJECTS_ROOTDIR:
    die(fg.red + "Error: environments not set!" + fg.rs)

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
if not SPREADSHEET_ID:
    die(
        fg.red + "Error: environments SPREADSHEET_ID not set!" + fg.rs)

LOGS_DIRECTORY = os.getenv('LOGS_DIRECTORY')
if not LOGS_DIRECTORY:
    die(
        fg.red + "Error: environments LOGS_DIRECTORY not set!" + fg.rs)

DEFAULT_BROWSER = os.getenv('DEFAULT_BROWSER') or 'brave'


class AppConfig:
    PROJECTS_ROOTDIR = PROJECTS_ROOTDIR

    # If modifying these scopes, delete the file token.json.
    SCOPES = [
        'https://www.googleapis.com/auth/contacts',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    APP_NAME = os.getenv('APP_NAME')
    SPREADSHEET_ID = SPREADSHEET_ID

    GOOGLE_DRIVE_ROOT_PROJECT_DIR_ID = "1uZNaMYudSyY9m0miNrhKUnnYjWh7xz1_"

    isDev = isDev

    LOGS_DIRECTORY = LOGS_DIRECTORY

    DEFAULT_BROWSER = DEFAULT_BROWSER
