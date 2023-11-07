# https://leetcode.com/problems/word-break/
class Solution:
    def __init__(self):
        self.ans = False
        self.wordDict = set()

    def word_break_helper(self, s: str) -> None:
        """
        start, end
        i       
        catsan dog
        cats andog
        ["cats","dog","sand","and","cat"]

        "cats"
        "cat"

        as we found our current word, exist in wordDict

        basecase: when a string exists in wordDict and there's no remaining characters: self.ans = True
        """
        char_so_far = []

        for end in range(len(s)):
            char_so_far.append(s[end])
            word = ''.join(char_so_far)
            if word in self.wordDict:
                if end == len(s) - 1:
                    self.ans = True
                    break
                self.word_break_helper(s[end+1:])

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        start, end
        i       
        catsan dog
        cats andog
        ["cats","dog","sand","and","cat"]

        "cats"
        "cat"

        as we found our current word, exist in wordDict

        basecase: when a string exists in wordDict and there's no remaining characters: self.ans = True
        """
        self.wordDict = set(wordDict)
        char_so_far = []

        for end in range(len(s)):
            char_so_far.append(s[end])
            word = ''.join(char_so_far)
            if word in self.wordDict:
                if end == len(s) - 1:
                    self.ans = True
                    break
                self.word_break_helper(s[end+1:])

        return self.ans
