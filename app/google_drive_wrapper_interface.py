import abc


class GoogleDriveWrapperInterface():

    @abc.abstractmethod
    def create_folder(self, contact_name: str) -> str:
        """Creates a folder in Google Drive with `contact_name`, 
        creates a scaffolding project directory under it and makes it public to read and returns the public URL

        Args:
            contact_name (str): the contact name that will give name to the internal folder

        Returns:
            str: the public URL
        """
        pass

    @abc.abstractmethod
    def delete_file(self, file_id: str):
        pass

    @abc.abstractmethod
    def delete_folders_by_name(self, file_name: str):
        pass
