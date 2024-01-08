# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        - have a set to save the unique characters of window (our window is guaranteed to only have unique characters): unique_ch = set()
        - slide the window while left <= right < len(s):
            - if the current character at right already exists in unique_ch, repeat these steps while left <= right and s[right] exists in unique_ch:
                - remove s[left] from unique_ch
                - increment left by 1.
            - Otherwise, add the character at right to unique_s, and ans = max(ans, len(unique_s))
        """
        ans = 0
        unique_ch = set()
        left = -1
        right = 0

        while left <= right < len(s):
            ch = s[right]
            if ch in unique_ch:
                left = 0 if left == -1 else left
                while left <= right and ch in unique_ch:
                    unique_ch.discard(s[left])
                    left += 1

            # ch is now not in unique_ch
            unique_ch.add(ch)
            ans = max(ans, len(unique_ch))
            right += 1

        return ans
