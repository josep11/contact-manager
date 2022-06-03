from googleapiclient.discovery import build
from app.exceptions import ContactDoesNotExistException
from app.utils import substract_prefix_name

from app.google_sheets_wrapper_interface import GoogleSheetsWrapperInterface

SAMPLE_RANGE_NAME = 'Customers'  # 'A2:A1000'


class GoogleSheetsWrapper(GoogleSheetsWrapperInterface):

    def __init__(self, credentials, spreadsheet_id: str):
        self.credentials = credentials
        self.service = build('sheets', 'v4', credentials=self.credentials)
        self.spreadsheet_id = spreadsheet_id

    # ---------------------
    # ----  SHARED FNS ----
    # ---------------------

    def _remove_value_from_rows(self, rows: list, value: str):
        # Will replace the cell value that is equal to @value param for ''
        return list(map(lambda cellVal: cellVal if len(cellVal) > 0 and cellVal[0] != value else [''], [cellVal for cellVal in rows]))

    # ---------------------
    # ----  INTERFACE FNS ----
    # ---------------------

    def get_rows(self) -> list:
        """Gets the list of customers from Google Spreadsheet

        Returns:
            list[str]
        """
        result = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id, range=SAMPLE_RANGE_NAME).execute()
        rows = result.get('values', [])
        print('{0} contacts retrieved from spreadsheet'.format(len(rows)))
        return rows

    def add_customer(self, rows: list, name: str):
        customers = [item for sublist in rows for item in sublist]
        if name in customers:
            print(f'Not adding {name} to spreadsheet. Already exists')
            return

        non_empty_rows_before = len([x for x in rows if x])

        rows.append([name])

        value_input_option = 'USER_ENTERED'
        body = {
            'values': rows
        }
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=SAMPLE_RANGE_NAME,
            valueInputOption=value_input_option, body=body).execute()

        updated_rows = result.get('updatedCells')
        print('{0} cells updated.'.format(updated_rows))
        if updated_rows != (non_empty_rows_before + 1):
            raise BaseException('No s\'ha actualitzat cap contacte!')

    def delete_customer(self, rows: list, name: str):
        customers = [item for sublist in rows for item in sublist]
        if not name in customers:
            name = substract_prefix_name(name)
            if not name in customers:
                raise ContactDoesNotExistException(
                    f'Error: contact with name "{name}" does not exists on Google Sheets')

        rows = self._remove_value_from_rows(rows, name)

        value_input_option = 'USER_ENTERED'
        body = {
            'values': rows
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=SAMPLE_RANGE_NAME,
            valueInputOption=value_input_option, body=body).execute()

        print(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')
