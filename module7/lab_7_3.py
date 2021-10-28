class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_date_valid(date_as_string, splitter):
        day, month, year = map(int, date_as_string.split(splitter))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 3999

    @classmethod
    def from_string(cls, date_as_string, splitter):
        day, month, year = map(int, date_as_string.split(splitter))
        new_date = cls(day, month, year)
        return new_date

    @staticmethod
    def from_string_static(date_as_string, splitter):
        day, month, year = map(int, date_as_string.split(splitter))
        new_date = Date(day, month, year)
        return new_date


is_date1 = Date.is_date_valid('26-10-2020', '-')
date1 = Date.from_string('26-10-2020', '-')
print(is_date1, date1.day, date1.month, date1.year)

is_date2 = Date.is_date_valid('27-10-2021', '-')
date2 = Date.from_string('27-10-2021', '-')
print(is_date2, date2.day, date2.month, date2.year)

print(isinstance(date1, Date))
print(isinstance(date1, Date))