def is_leap_year(year):
    """
    It is a leap year if divisible by four EXCEPT if it is
    also divisible by 100. It is still a leap year if it is also
    divisible by 400.
    :params year:integer
    :return bool
    """
    return (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)
