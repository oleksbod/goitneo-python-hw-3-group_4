from addressBook.name import Name
from addressBook.phone import Phone
from addressBook.birthday import Birthday 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):        
        if not list(filter(lambda p: p.value == phone, self.phones)):
            self.phones.append(Phone(phone))
        else:
            print(f"Phone number {phone} already exists for {self.name.value}.")

    def remove_phone(self, phone):       
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        print(f"Phone number {old_phone} not found for {self.name.value}.")

    def change_phone(self, new_phone):
        if len(self.phones) > 0:
            self.remove_phone(self.phones[0].value)
        self.add_phone(new_phone)        

    def find_phone(self, phone):       
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None
    
    def add_birthday(self, birthday):
        if not hasattr(self, 'birthday'):
            self.birthday = Birthday(birthday)
            return "Birthday added."
        else:
            return f"{self.name.value} already has a birthday."
        
    def show_birthday(self):
        if not hasattr(self, 'birthday'):
            return f"No Birthday found for {self.name.value}"
        else:
            return f"{self.birthday.value}"
        
    def get_birthday(self):
        if not hasattr(self, 'birthday'):
            return None
        else:
            return self.birthday.value

    def __str__(self):
        return f"Contact name: {self.name.value}, {'phone' if len(self.phones) == 1 else 'phones'}: {'; '.join(p.value for p in self.phones)}"