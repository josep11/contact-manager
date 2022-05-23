class ContactAlreadyExistException(BaseException):
    pass


class ContactDoesNotExistException(BaseException):
    pass


class WrongPhoneNumberException(BaseException):
    pass


class InvalidNameException(BaseException):
    def __init__(self, message="The name cannot be empty"):
        self.message = message
        super().__init__(self.message)
