from googleapiclient.discovery import build
from sty import fg
import os
from app.utils import eprint

from dotenv import load_dotenv
load_dotenv()

SAMPLE_SPREADSHEET_ID_input = os.getenv('SAMPLE_SPREADSHEET_ID_input')
if not SAMPLE_SPREADSHEET_ID_input:
    eprint(fg.red + "Error: environments SAMPLE_SPREADSHEET_ID_input not set!" + fg.rs)
    exit(1)

SAMPLE_RANGE_NAME = 'Customers'  # 'A2:A1000'


def create_service(credentials):
    service = build('sheets', 'v4', credentials=credentials)
    return service


def get_rows(credentials):
    """Gets the list of customers from Google Spreadsheet

    Returns:
        list[str]
    """
    service = create_service(credentials)
    result = service.spreadsheets().values().get(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input,  range=SAMPLE_RANGE_NAME).execute()
    rows = result.get('values', [])
    print('{0} contacts retrieved from spreadsheet'.format(len(rows)))
    return rows


def add_customer(credentials, rows, name):
    customers = [item for sublist in rows for item in sublist]
    if name in customers:
        print(f'Not adding {name} to spreadsheet. Already exists')
        return

    rows.append([name])

    service = create_service(credentials)
    value_input_option = 'USER_ENTERED'
    body = {
        'values': rows
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID_input, range=SAMPLE_RANGE_NAME,
        valueInputOption=value_input_option, body=body).execute()

    updated = result.get('updatedCells')
    print('{0} cells updated.'.format(updated))
    if updated != len(rows):
        raise 'No s\'ha actualitzat cap contacte!'
