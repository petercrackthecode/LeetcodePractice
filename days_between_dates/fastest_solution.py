from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        start = date.fromisoformat(date1)
        end = date.fromisoformat(date2)

        delta = end - start
        return abs(delta.days)
