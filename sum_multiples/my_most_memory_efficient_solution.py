class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        nums_sum = 0
        starting from 1 to n, have a number num. check if that number is divisible by 3 or 5 or 7:
        - yes: add that number to our sum.

        Time: O(N) N = n
        Space: O(1)
        """

        nums_sum = 0
        for num in range(1, n+1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                nums_sum += num

        return nums_sum
