from googleapiclient.discovery import build
from apiclient import errors

from app.google_drive_wrapper_interface import GoogleDriveWrapperInterface


class GoogleDriveWrapper(GoogleDriveWrapperInterface):

    def __init__(self, credentials, projects_root_dir: str):
        """_summary_

        Args:
            credentials (_type_): the credentials
            projects_root_dir (str): the root directory id in drive
        """
        self.credentials = credentials
        self.service = build('drive', 'v3', credentials=self.credentials)
        self.projects_root_dir = projects_root_dir

    # ---------------------
    # ----  SHARED FNS ----
    # ---------------------

    def get_folder_url(self, file_id: str):
        prop = "webViewLink"
        resp = self.service.files().get(
            fileId=file_id,
            fields=prop
        ).execute()

        return resp[prop] if prop in resp else None

    # ---------------------
    # ----  INTERFACE FNS ----
    # ---------------------

    def create_folder(self, contact_name: str) -> str:
        """Creates a folder in Google Drive with `contact_name`, 
        creates a scaffolding project directory under it and makes it public to read and returns the public URL

        Args:
            contact_name (str): the contact name that will give name to the internal folder

        Returns:
            str: the public URL
        """
        # TODO: should search if the contact already exists (or it creates duplicated folders)

        file_metadata = {
            'parents': [self.projects_root_dir],
            'name': contact_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.service.files().create(body=file_metadata,
                                           fields='id').execute()
        alumno_root_folder_id = file.get('id')
        # print(f"Folder ID:{file.get('id')}")

        # Now create the one that will be shared publicly for the project
        file_metadata = {
            'parents': [alumno_root_folder_id],
            'name': 'project',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.service.files().create(body=file_metadata,
                                           fields='id').execute()

        project_folder_id = file.get('id')

        permission = {
            'type': 'anyone',
            'role': 'reader',
        }

        self.service.permissions().create(
            fileId=project_folder_id, body=permission).execute()

        return self.get_folder_url(project_folder_id)

    def get_file_ids_by_name(self, file_name: str) -> list:
        """Gets the files by exact name and returns the ids

        Args:
            file_name (str): 

        Returns:
            list: the array of ids
        """
        page_token = None
        response = self.service.files().list(q=f"mimeType='application/vnd.google-apps.folder' and name='{file_name}'",
                                             spaces='drive',
                                             fields='nextPageToken, files(id, name)',
                                             pageToken=page_token).execute()

        return response.get('files', [])

    def delete_file(self, file_id: str):
        try:
            self.service.files().delete(fileId=file_id).execute()
            print(f"deleted file with id = {file_id}")
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

    def delete_file_by_name(self, file_name: str):
        # The list is non exhaustive as it picks only the first page
        # https://developers.google.com/drive/api/guides/search-files
        for file in self.get_file_ids_by_name(file_name):
            print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
            self.delete_file(file.get('id'))
