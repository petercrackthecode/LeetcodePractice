# https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        split string s to words delimited by the whitespaces. After our split, remove all empty string and save the words to a list called s_words
        have two pointers, left and right. left = 0 and right = len(s_words) - 1
        loop while left < right:
            swap s_words[left] and s_words[right]
            increment left by 1
            decrement right by 1
        return ' '.join(s_words)
        """
        s_words = [word for word in s.split(' ') if word != '']
        [left, right] = [0, len(s_words) - 1]
        while left < right:
            s_words[left], s_words[right] = s_words[right], s_words[left]
            left += 1
            right -= 1
        return ' '.join(s_words)
