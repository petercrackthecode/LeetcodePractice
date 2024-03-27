"""
Problem: "Balanced Substring"

You are given a string s consisting of only two types of characters: 'A' and 'B'. 
Your task is to find the length of the longest substring of s that is balanced. 
A substring is considered balanced if it contains an equal number of 'A's and 'B's.

Example:
    
     012345
s = "AABBAB"
len(s) = 6
Output: 4
Explanation:
The longest balanced substring is "AABB" or "BABA", both of which have a length of 4.

Constraints:

1 <= s.length <= 1000
s consists only of characters 'A' and 'B'.

brute-force:
- have a variable called ans: int = 0

- for each size from 1 -> len(s) (inclusively):
    - for each index from 0 -> len(s) - size (inclusively):
        - get the substring from index = 0 to len(s)-size (inclusively): substr = s[index:index+size]
        - calculate the number of balanced characters in the substring substr: have a helper function called count_balance(s: str) -> int
        to help us do so: balance = count_balance(substr)
        - ans = max(ans, balance)

- return ans
"""

from typing import List
from collections import Counter


def count_balance(substr) -> int:
    count_A_and_B = Counter(substr)

    return -1 if count_A_and_B["A"] != count_A_and_B["B"] else count_A_and_B["A"] * 2


def get_longest_balance(s: str) -> int:
    ans: int = 0

    for size in range(2, len(s) + 1):
        for i in range(len(s) - size + 1):
            substr = s[i : i + size]
            balance = count_balance(substr)
            print(f"substr = {substr}")
            print(f"balance = {balance}\n")
            ans = max(ans, balance)

    return ans


ans = get_longest_balance("AABBAB")
print(f"ans = {ans}")  # 4
