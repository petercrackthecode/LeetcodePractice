# https://leetcode.com/problems/number-of-days-between-two-dates/
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        a = datetime.strptime(date1, '%Y-%m-%d').date()
        b = datetime.strptime(date2, '%Y-%m-%d').date()
        start = min(a, b)
        end = max(a, b)

        return (end - start)

    return (end - start).days

