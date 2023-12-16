from addressBook.record import Record
from customDecorators.errorsHandler import input_error

@input_error
def add_contact(args, book):
    name, phone = args
    if book.find(name) is not None:
        return f"Contact '{name}' exist!"
    
    new_record = Record(name)
    new_record.add_phone(phone)
    book.add_record(new_record)

    return "Contact added."

@input_error
def update_contact(args, book):
    name, phone = args   
    record = book.find(name)
    if record is None:
        raise KeyError
    
    record.change_phone(phone)

    return "Contact updated."

@input_error
def show_phone(args, book):
    if len(args) > 1:
        raise IndexError
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError
    
    return record
    
def show_all(book):
    if len(book) == 0:
        print("Where are no data in Address Book")
        
    for name, record in book.data.items():
        print(record)

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError
    return record.add_birthday(birthday)

@input_error
def show_birthday(args, book):
    if len(args) > 1:
        raise IndexError
    
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError
    
    return record.show_birthday()