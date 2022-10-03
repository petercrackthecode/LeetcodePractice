# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 2D array
        ans = []
        for i in range(1, numRows+1):
            last_row = len(ans) - 1
            curr_row_iterator = 0
            curr_row = []
            while curr_row_iterator < i:
                if curr_row_iterator <= 0 or curr_row_iterator >= i-1:
                    curr_row.append(1)
                else:
                    sum_of_two_numbers_from_above_row = ans[last_row][curr_row_iterator -
                                                                      1] + ans[last_row][curr_row_iterator]
                    curr_row.append(sum_of_two_numbers_from_above_row)
                curr_row_iterator += 1
            ans.append(curr_row)

        return ans
