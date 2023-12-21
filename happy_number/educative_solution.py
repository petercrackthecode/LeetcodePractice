# https://leetcode.com/problems/happy-number/
def sum_of_squared_digits(num: int) -> int:
    ans = 0

    while num != 0:
        digit = num % 10
        ans += (digit ** 2)
        num //= 10

    return ans


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = sum_of_squared_digits(slow)

        while fast != 1 and fast != slow:
            slow = sum_of_squared_digits(slow)
            fast = sum_of_squared_digits(sum_of_squared_digits(fast))

        return fast == 1
