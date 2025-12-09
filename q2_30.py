class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year):
        return current_year - self.birth_year


    @staticmethod
    def is_valid_birth_date(birth_date):
        if len(birth_date) != 10:
            return False
        if birth_date[2] != '-' or birth_date[5] != '-':
            return False
        parts = birth_date.split('-')
        if len(parts) != 3:
            return False
        day, month, year = parts
        return (day.isdigit() and month.isdigit() and year.isdigit() and len(day) == 2 and len(month) == 2 and len(year) == 4)

    @classmethod
    def from_birth_date(cls, name, birth_date):
        if not cls.is_valid_birth_date(birth_date):
            print("Birth date is invalid")
            return
        year = int(birth_date.split('-')[2])
        return cls(name, year)

