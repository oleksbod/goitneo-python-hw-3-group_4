from addressBook.field import Field
from customException.invalid_phone import InvalidPhoneFormatError

class Phone(Field):
    def __init__(self, value):
        # має бути 10 цифр
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise InvalidPhoneFormatError
        super().__init__(value)