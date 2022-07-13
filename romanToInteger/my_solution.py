# link: https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        romansToNumsLookup = {
            'I': 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        specialRomansToNumsLookup = {
            'IV': 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        index = 0
        ans = 0

        while index < len(s):
            curr_char = s[index]
            if (curr_char in ["I", "X", "C"]) and index < len(s) - 1:
                # Special characters and not staying at the last index in the string
                next_char = s[index+1]
                if f"{curr_char}{next_char}" in specialRomansToNumsLookup:
                    ans += specialRomansToNumsLookup[curr_char + next_char]
                    index += 1
                else:
                    ans += romansToNumsLookup[curr_char]
            else:
                ans += romansToNumsLookup[curr_char]

            index += 1

        return ans
