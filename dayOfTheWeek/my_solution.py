# https://leetcode.com/problems/day-of-the-week
def check_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        """
        Simple algorithm in one sentence: Starting from the first available day (1/1/1971- Friday), calculate the days have passed from that date to the current date, module it to 7, then use a dictionary (key: int, value: day_of_the_week) to get the day of the week.
        """
        days_passed = 0

        curr_year = 1971
        while curr_year < year:
            is_leap_year = check_leap_year(curr_year)
            days_passed += 366 if is_leap_year else 365
            curr_year += 1

        is_input_year_leap_year = check_leap_year(year)
        curr_month = 1
        month_to_days = {
            1: 31,
            2: 29 if is_input_year_leap_year else 28,
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
        while curr_month < month:
            days_passed += month_to_days[curr_month]
            curr_month += 1

        day_of_week_lookup = {
            1: "Friday",
            2: "Saturday",
            3: "Sunday",
            4: "Monday",
            5: "Tuesday",
            6: "Wednesday",
            0: "Thursday"
        }

        days_passed += day

        return day_of_week_lookup[days_passed % 7]
