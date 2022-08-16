from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Have two variables called m and n as the running coordinator to travel throw the matrix, where m represents the current row, and n represents the current column we're at.
        we have a variable called direction to save the current direction our pointer is running toward.
        we have 4 variables called top_bound, bottom_bound, left_bound, right_bound, which represent the current limit of our pointer in 4 directions.
        Move the pointer in the order:
        1. left -> right (n = n + 1).
        2. top -> bottom (m = m + 1).
        3. right -> left (n = n - 1).
        4. bottom -> top (m = m - 1).

        Each time we hit a bound, adjust the bound values:
        1. Hit right bound => done screening the top border:
            top += 1
        2. Hit bottom bound => done screening the right border:
            right -= 1
        3. Hit left bound => done screening the bottom border:
            bottom -= 1
        4. Hit top bound: done screening the left border:
            left += 1


        At each iteration, append the number at the current position (m, n) to the ans array.
        Continue the loop until len(ans) == len(matrix) * len(matrix[0])
        """
        direction = "left_to_right"
        ans = []
        row, col = len(matrix), len(matrix[0])
        m = 0
        n = 0

        left_bound = 0
        right_bound = col - 1
        top_bound = 0
        bottom_bound = row - 1

        while len(ans) < row * col:
            ans.append(matrix[m][n])
            if direction == "left_to_right":
                if n >= right_bound:
                    direction = "top_to_bottom"
                    top_bound += 1
                    m += 1
                else:
                    n += 1
            elif direction == "top_to_bottom":
                if m >= bottom_bound:
                    direction = "right_to_left"
                    right_bound -= 1
                    n -= 1
                else:
                    m += 1
            elif direction == "right_to_left":
                if n <= left_bound:
                    direction = "bottom_to_top"
                    bottom_bound -= 1
                    m -= 1
                else:
                    n -= 1
            else:  # direction == "bottom_to_top"
                if m <= top_bound:
                    direction = "left_to_right"
                    left_bound += 1
                    n += 1
                else:
                    m -= 1

        return ans
