from customException.invalid_birthday import InvalidBirthdayFormatError
from customException.invalid_phone import InvalidPhoneFormatError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidBirthdayFormatError:
            return "Invalid birthday format. Please use DD.MM.YYYY."
        except InvalidPhoneFormatError:
            return "Invalid phone number format."    
        except ValueError:
            return "Give me name and phone(or birthday) please!"
        except KeyError:
            return "This user doesn't exist! Enter correct user name!"
        except IndexError:
            return "Give me name please!"
    return inner