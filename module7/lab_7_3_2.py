class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_date_valid(date_as_string, splitter):
        day, month, year = map(int, date_as_string.split(splitter))
        return 0 < day <= 31 and 0 <month <= 12 and 0 < year <= 3999

    @classmethod
    def from_string(cls, date_as_string, splitter):
        day, month, year = map(int,date_as_string.split(splitter))
        new_date = cls(day, month, year)
        return new_date

    @staticmethod
    def from_string_static(date_as_string, splitter):
        day, month, year = map(int, date_as_string.split(splitter))
        new_date = Date(day, month, year)
        return new_date


class UserDate(Date):
    pass


is_user_date1 = UserDate.is_date_valid('26-07-2020', '-')
user_date1 = UserDate.from_string('26-07-2020', '-')
print(is_user_date1, user_date1.day, user_date1.month, user_date1.year)

is_user_date2 = UserDate.is_date_valid('27-10-2021', '-')
user_date2 = UserDate.from_string_static('27-10-2021', '-')
print(is_user_date2, user_date2.day, user_date2.month, user_date2.year)

print(isinstance(user_date1, UserDate))
print(isinstance(user_date2, UserDate))
