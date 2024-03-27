"""
Problem: "Encode and Decode Strings"

You are tasked with designing two functions, encode and decode, for a messaging application.

Encode Function:

This function takes a list of strings as input.
The function should return a single string which is an encoding of the list of strings.
Each string should be encoded in such a way that you can uniquely identify where it starts and ends in the encoded form.
Decode Function:

This function takes an encoded string (output of the encode function) and decodes it back into the original list of strings.
Example:

Input for Encode Function:

["Hello", "World", "!"]
Output of Encode Function and Input for Decode Function:

Encoded string (example format): "5#Hello5#World1#!"
Output of Decode Function:

["Hello", "World", "!"]
Consider the following:

Strings can contain any character, including numbers and special characters.
The length of individual strings can vary.
The list can contain any number of strings, including zero.
"""

from typing import List, Set, Dict


def encode(strs: List[str]) -> str:
    # ["Hello", "World", "!"]
    # []
    # ["Hello", "World", "!"] -> 5(Hello)5(World)0()
    """
    encoded_str: 5(Hello)5(World)1(!)
    - have a list of str called ans:List[str] = []
    - loop: for each string s within strs:
        - get the len of s: len_s = len(s)
        - append the string len_s(s) to ans: ans.append(f'{len_s}({s})')

    - return ''.join(ans)
    """
    ans: List[str] = []

    for s in strs:
        ans.append(f"{len(s)}({s})")

    return "".join(ans)


def decode(s: str) -> List[str]:
    # ["He5lo", "World", "!"] -> 5(He5lo)5(World)1(!)

    """
    - has a flag called is_reading_str to know when we're reading a string. is_reading_str = False
    - have a list of str called ans. ans:List[str] = []
    - have a variable called curr_length to save the current length of the string. curr_length:int = 0
    - have a variable called curr_str to save the current string we're parsing. curr_str:List[str] = []
    - i = 0
    - loop while i is smaller than s's length:
        - if we are not within a str:
            - if ch is a digit (ch.isnumeric()):
                - curr_length = curr_length * 10 + int(ch)
            - otherwise, if ch == '(':
                - is_reading_str = True
            - increment i by 1

        - otherwise (is_reading_str = True):
            - loop: while curr_length > 0:
                - append s[i] to curr_str
                - increment i by 1
                - decrement curr_length by 1
            - append ''.join(curr_str) to ans
            - set curr_str = []
            - set is_reading_str to False
    - return ans
    """
    is_reading_str: bool = False
    ans: List[str] = []
    curr_length: int = 0
    curr_str: List[str] = []

    i: int = 0
    while i < len(s):
        if not is_reading_str:
            ch = s[i]
            if ch.isdigit():
                curr_length = curr_length * 10 + int(ch)
            elif ch == "(":
                is_reading_str = True

            i += 1

            """
            - otherwise (is_reading_str = True):
                - loop: while curr_length > 0:
                    - append s[i] to curr_str
                    - increment i by 1
                    - decrement curr_length by 1
                - append ''.join(curr_str) to ans
                - set curr_str = []
                - set is_reading_str to False
            - return ans
            """
        else:  # is_reading_str == True
            while curr_length > 0:
                curr_str.append(s[i])
                i += 1
                curr_length -= 1

            ans.append("".join(curr_str))
            curr_str = []
            is_reading_str = False

    return ans


# ["Hello", "World", "!"]
# ["Hello", "World", "!"] -> 5(Hello)5(World)0()

strs: List[str] = ["5ll1", "World", ""]
print(f"encode({strs}) = {encode(strs)}")
print(decode(encode(strs)))  # ["Hello", "World", "!"]
