from constants.constants import MENU
from handlers.all_command_handlers import *
from addressBook.address_book import AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():    
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print(MENU)

    while True:        
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hello, \nHow can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(update_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            book.get_birthdays_per_week()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()