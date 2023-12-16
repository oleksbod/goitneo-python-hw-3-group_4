from collections import UserDict, defaultdict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):       
        self.data[record.name.value] = record

    def find(self, name):        
        return self.data.get(name)

    def delete(self, name):
        removed_record = self.data.pop(name, None)
        if removed_record is None:
            print(f"Record with name {name} not found.")

    def get_birthdays_per_week(self):
        birthdays_by_day = defaultdict(list, {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': []})
        
        today = self.get_next_sunday()

        for name, record in self.data.items():
            birthdayStr = record.get_birthday()
            if birthdayStr is None:
                continue

            birthday = datetime.strptime(birthdayStr, "%d.%m.%Y").date()
            
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            delta_days = (birthday_this_year - today).days
        
            if 0 <= delta_days < 7:           
                day_of_week = (today + timedelta(days=delta_days)).strftime('%A')

                if day_of_week == 'Sunday':
                    day_of_week = 'Monday'
                
                birthdays_by_day[day_of_week].append(name)
        
        self.print_birthdays(birthdays_by_day)

    def get_next_sunday(self):
        today = datetime.today().date()
        days_until_next_sunday = (6 - today.weekday()) % 7
        next_sunday = today + timedelta(days=days_until_next_sunday)
        return next_sunday

    def print_birthdays(self, birthdays_by_day):
        for day, names in birthdays_by_day.items():
            if len(names) == 0:
                continue
            print(f"{day}: {', '.join(names)}")