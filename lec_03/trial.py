def is_leap_year(year):
    _is_leap_year = year % 4 == 0
    _is_leap_year = _is_leap_year and (year%100 != 0)
    _is_leap_year = _is_leap_year or (year%400 == 0)
    return is_leap_year

year = 1999
_is_leap_year = is_leap_year(year)

print("{year} is leap year! {_is_leap_year}")