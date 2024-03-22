# https://leetcode.com/problems/encode-and-decode-strings
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        the format of our encoded string:
        - [string_1_number_of_characters](string_1)[string_1_number_of_characters](string_2)...[string_n_number_of_characters](string_n)

        ["Hello","World"] -> "5(Hello)5(World)"
        """
        ans: List[str] = []

        for s in strs:
            ans.append(f"{len(s)}({s})")

        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans: List[str] = []
        is_string_char: bool = False
        str_length: int = 0
        # "5(Hello)5(World)"
        i: int = 0

        while i < len(s):
            if not is_string_char:
                if s[i].isdigit():
                    str_length = (str_length * 10) + int(s[i])
                elif s[i] == "(":
                    is_string_char = True

                i += 1
            else:  # is_string_char == True
                # parse string
                curr_str: List[str] = []
                while str_length > 0:
                    curr_str.append(s[i])
                    str_length -= 1
                    i += 1

                ans.append("".join(curr_str))
                is_string_char = False

        return ans
