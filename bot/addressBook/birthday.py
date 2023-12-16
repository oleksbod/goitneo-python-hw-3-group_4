from addressBook.field import Field
from datetime import datetime
from customException.invalid_birthday import InvalidBirthdayFormatError

class Birthday(Field):
    def __init__(self, value):        
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise InvalidBirthdayFormatError
        super().__init__(value)