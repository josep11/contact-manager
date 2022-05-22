
import abc


class GoogleSheetsWrapperInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_rows():
        pass
