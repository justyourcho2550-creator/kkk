# Do not remove this line!
from poomdt import is_leap_year

# Test 1 - Test whether is_leap_year can handle 0 correctly
def test_year_is_zero():
    if is_leap_year(0) == True:
        return True
    else:
        return False

# Test 2 - Test typical leap year (divisible by 4 but not 100)
# Reason to fail: is_leap_year does not recognize normal leap years
def test_typical_leap_year():
    year = 2004
    result = is_leap_year(year)
    return result == True

# Test 3 - Test typical common year (not divisible by 4)
# Reason to fail: is_leap_year incorrectly marks non-leap years as leap
def test_common_year():
    year = 2001
    result = is_leap_year(year)
    return result == False

# Test 4 - Test century non-leap year (divisible by 100 but not 400)
# Reason to fail: is_leap_year does not handle century rule correctly
def test_century_non_leap_year():
    year = 1900
    result = is_leap_year(year)
    return result == False

# Test 5 - Test exceptional leap year (divisible by 400)
# Reason to fail: is_leap_year misses the exception for year divisible by 400
def test_exceptional_leap_year():
    year = 2000
    result = is_leap_year(year)
    return result == True
