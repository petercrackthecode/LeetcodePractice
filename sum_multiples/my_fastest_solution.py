class Solution:
    def sumOfMultiples(self, n: int) -> int:
        """
        power_of_three = 3
        power_of_five
        power_of_seven

        keep adding 3 to power_of_three, if power_of_three is within the range [1, n], add power_of_three to sum. do sum until power_of_three > n
        keep adding 5 to power_of_five, if power_of_five is within the range [1, n], add power_of_five to sum. do sum until power_of_five > n
        keep adding 7 to power_of_seven, if power_of_seven is within the range [1, n], add power_of_seven to sum. do sum until power_of_seven > n

        Time: O(N/3 + N/5 + N/7) < O(N)
        Space: O(1)
        """
        power_of_three = 3
        power_of_five = 5
        power_of_seven = 7
        nums_sum = 0

        while power_of_three <= n:
            nums_sum += power_of_three
            # print('power_of_three = ', power_of_three)
            power_of_three += 3

        while power_of_five <= n:
            if power_of_five % 3 != 0:
                nums_sum += power_of_five
                # print('power_of_five = ', power_of_five)
            power_of_five += 5

        while power_of_seven <= n:
            if power_of_seven % 3 != 0 and power_of_seven % 5 != 0:
                nums_sum += power_of_seven
                # print('power_of_seven = ', power_of_seven)
            power_of_seven += 7

        return nums_sum
