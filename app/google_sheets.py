from googleapiclient.discovery import build
from sty import fg
import os
from app.exceptions import ContactDoesNotExistException
from app.utils import eprint, substract_prefix_name

from dotenv import load_dotenv
load_dotenv()

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
if not SPREADSHEET_ID:
    eprint(fg.red + "Error: environments SPREADSHEET_ID not set!" + fg.rs)
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
        spreadsheetId=SPREADSHEET_ID,  range=SAMPLE_RANGE_NAME).execute()
    rows = result.get('values', [])
    print('{0} contacts retrieved from spreadsheet'.format(len(rows)))
    return rows


def add_customer(credentials, rows, name):
    customers = [item for sublist in rows for item in sublist]
    if name in customers:
        print(f'Not adding {name} to spreadsheet. Already exists')
        return

    non_empty_rows_before = len([x for x in rows if x])

    rows.append([name])

    service = create_service(credentials)
    value_input_option = 'USER_ENTERED'
    body = {
        'values': rows
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
        valueInputOption=value_input_option, body=body).execute()

    updated_rows = result.get('updatedCells')
    print('{0} cells updated.'.format(updated_rows))
    if updated_rows != (non_empty_rows_before + 1):
        raise BaseException('No s\'ha actualitzat cap contacte!')

# Will replace the cell value that is equal to @value param for ''


def remove_value_from_rows(rows, value):
    return list(map(lambda cellVal: cellVal if cellVal[0] != value else [''], [cellVal for cellVal in rows]))


def delete_customer(credentials, rows, name):
    customers = [item for sublist in rows for item in sublist]
    if not name in customers:
        name = substract_prefix_name(name)
        if not name in customers:
            raise ContactDoesNotExistException(
                f'Error: contact with name "{name}" does not exists on Google Sheets')

    rows = remove_value_from_rows(rows, name)

    service = create_service(credentials)
    value_input_option = 'USER_ENTERED'
    body = {
        'values': rows
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
        valueInputOption=value_input_option, body=body).execute()

    print(f'https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}')
