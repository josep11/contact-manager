import abc


class GoogleDriveWrapperInterface():

    @abc.abstractmethod
    def create_folder(self, contact_name: str) -> str:
        pass

    @abc.abstractmethod
    def delete_file(self, file_id: str):
        pass

    @abc.abstractmethod
    def delete_file_by_name(self, file_name: str):
        pass
