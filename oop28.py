# Напишите определение класса Date


class Date:
    def __init__(self, d, m, y):
        self.__date = d
        self.__month = m
        self.__year = y

    @property
    def date(self):
        return f"{self.__date:02d}/{self.__month:02d}/{self.__year:04d}"

    @property
    def usa_date(self):
        return f"{self.__month:02d}-{self.__date:02d}-{self.__year:04d}"


# Ниже код для проверки методов класса Date

d1 = Date(5, 10, 2001)
assert isinstance(d1, Date)
assert d1.date == "05/10/2001"
assert d1.usa_date == "10-05-2001"
assert isinstance(type(d1).date, property), "Вы не создали property date"
print(d1.date, d1.usa_date)

d2 = Date(15, 3, 999)
assert isinstance(d2, Date)
assert d2.date == "15/03/0999"
assert d2.usa_date == "03-15-0999"
assert isinstance(type(d2).date, property), "Вы не создали property date"
print(d2.date, d2.usa_date)

d3 = Date(3, 5, 3)
assert d3.date == "03/05/0003"
assert d3.usa_date == "05-03-0003"
print(d3.date, d3.usa_date)
