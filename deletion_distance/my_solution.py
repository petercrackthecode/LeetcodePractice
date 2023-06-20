# https://www.pramp.com/challenge/61ojWAjLJbhob2nP2q1O
from typing import List, Set


def get_strings_after_delete_k_characters(s: List[str], k: int, string_after_deletion: Set[str]):
    """
    string_length = len(s)
    1. Starting from position i within [0..string_length - k]
      a. delete k characters from our string starting at position i:
        s = "abcd"
             0123
             i = 1, k = 2
        if i == string_length - 1:
          remaining_string = s[:-1]
        else:
          remaining_string = s[:i] + s[i+k:]
      b. get the remaining string. call it new_string.
      c. add new_string to our set str1_after_deletion:
          string_after_deletion.add(new_string)
      c. new_string_length = len(new_string) 
         for j is within [0..new_string_length]:
          get_strings_after_delete_k_characters(s, j, string_after_deletion)
    """


def deletion_distance(str1, str2):
    pass


"""
Recommend your peer to identify the base cases first. That is, cases where one of the strings is the empty string. In this case, the deletion distance is simply the length of the other string. After that, encourage them to try cases that are somewhat similar, such as one string containing 1 or 2 characters.

If your peer needs additional assistance, help them by hinting toward a recursive relation between the deletionDistance(str1, str2), and the deletionDistance for some prefixes of str1 and str2. After they find the relation, you may suggest using Dynamic Programming.

str1 = "dog"
str2 = "frog"

1. Have a map called str1_character_frequencies, which the key is a character that exists in str1, and the value is the frequencies of that character in str1.
   Have a map called str2_character_frequencies, which the key is a character that exists in str2, and the value is the frequencies of that character in str2.
2. Take out all the characters from str1 that don't belong to str1 using str2_character_frequencies.
   Take out all the characters from str2 that don't belong to str1 using str1_character_frequencies.
  
str1 = "dogg" -> "ogg"
str2 = "frog" -> "og"

=> Make sure the frequencies of two strings after the deletion match each other (the minimum character frequencies between 2 dictionaries.)
str1 = "dgo" -> clean_string -> "go"
str2 = "frog" -> clean_string -> "og"


1. Generate all the permutations of str1 after deleting [0..len(str1)] characters from it at different positions.
  a. Decide on the number of characters we're gonna delete from str1.
  b. For k characters to be deleted from a string, k is the length of the substring that'll be taken from our current string.
     Starting from positions [0..len(str1) - k] called i, delete the substring with length k starting from position i from the array: new_string = current_string taken substr (where substr is the string starting from i && len(substring) == k).
     Then, pass new_string to the helper function get_string_after_deletion(s: [str]) to receive a new set of strings after characters being deleted from different positions.
 c. Finally, we have a set of strings after deleting m characters (m is within [0..len(str1)]) from string str1. Called it str1_after_deletion.
2. Do the same above step for str2, we get the str2_after_deletion set.

longest_common_string_length = float('-inf')
Iterate through every element of str1_after_deletion: for each string_member, see if that string_member exists in str2_after_deletion:
+ No: move on to the next iteration.
+ Yes: longest_common_string_length = max(longest_common_string_length, len(string_member))


get_string_after_deletion(s: [str]) -> set[str]:

"""
