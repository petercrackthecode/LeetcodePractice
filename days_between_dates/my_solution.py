# https://leetcode.com/problems/number-of-days-between-two-dates/
from typing import List


def to_date_list(datestring: str) -> List[int]:
    return [int(timeunit) for timeunit in datestring.split('-') if timeunit != '']


def is_year_earlier(date1: List[int], date2: List[int]) -> bool:
    [year_1, month_1, day_1] = date1
    [year_2, month_2, day_2] = date2

    if year_1 != year_2:
        return year_1 < year_2
    # year_1 == year_2
    if month_1 != month_2:
        return month_1 < month_2
    # month_1 == month_2
    return day_1 < day_2


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def date_gap(start: List[int], end: List[int]) -> int:
    full_month_days = 0
    year, month, day = end

    month_to_day = {
        1: 31,
        2: 29 if is_leap_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    curr_month = 1

    while curr_month < month:
        full_month_days += month_to_day[curr_month]
        curr_month += 1

    return full_month_days + day


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
        ans = 0

        have a function to convert a date string into an array of [year: int, month: int, day: int]: to_date_list(datestring: str) -> List[int]
        assign the result of to_date_list(date1) to date1
        assign the result of to_date_list(date2) to date2
        start = the earlier date among date1 and date2 (have a function called is_year_earlier to help you do so)
        end = the later date among date1 and date2

        have a helper function called is_leap_year(year: int) -> bool that verify if a year is a leap year or not.
        have a function to get the number of dates between 2 days in the same years date_gap(day1: List[int], day2: List[int]) -> int.

        calculate the number of days between start and the first day of the year in start's year using the date_gap function, then assign it to start_gap.
        calculate the number of days between start and the first day of the year in end's year using the date_gap function, then assign it to end_gap.
        have a variable between_year = start's year + 1
        loop while between start's year < between_year < end's year:
            if between_year is a leap year, increment end_gap by 366, otherwise 365.
            increment between year by 1.
        return end_gap - start_gap
        """
        date1 = to_date_list(date1)
        date2 = to_date_list(date2)

        start = date1 if is_year_earlier(date1, date2) else date2
        end = date2 if is_year_earlier(date1, date2) else date1

        start_gap = date_gap([start[0], 1, 1], start)
        end_gap = date_gap([end[0], 1, 1], end)

        between_year = start[0]

        while between_year < end[0]:
            end_gap += 366 if is_leap_year(between_year) else 365
            between_year += 1

        return end_gap - start_gap
