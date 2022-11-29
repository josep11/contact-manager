import abc


class GoogleContactsWrapperInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_contact_by_query(self, query) -> list:
        pass

    @abc.abstractmethod
    def create_contact_google_contacts(self, name: str, phone: str, extra: str = None):
        pass

    @abc.abstractmethod
    def delete_contact_google_contacts(self, name: str):
        pass
