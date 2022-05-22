import abc


class GoogleSheetsWrapperInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_rows(self) -> list:
        pass

    @abc.abstractmethod
    def add_customer(self, rows: list, name: str):
        pass

    @abc.abstractmethod
    def delete_customer(self, rows: list, name: str):
        pass
