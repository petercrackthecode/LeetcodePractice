# https://leetcode.com/problems/guess-the-word
from typing import List

"""
The solution to this problem depends on two observations:
1. If word has score x > 0, only those words that share exactly x characters with word can be the solution
e.g. suppose guess("xyz")=1
- "abc" cannot be the solution because it shares 0 letters with "xyz". "xyz" has a score of 1 so "abc" must have at least 1 letter wrong, so cannot be the solution.
- "zxy" cannot be the solution because it shares 0 letters in the right place with "xyz", so it must have at least one letter wrong.
- "ayz" cannot be the solution because it shares 2 letters with "xyz". If "ayz" were the solution then "xyz" would have a score of 2.
- "abz" can be the solution because it shares 1 letter with "xyz"
We can use this idea to quickly filter the word list:
```python
class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        while wordlist:
            word = wordlist.pop()
            matches = master.guess(word)
            # only those words that share exactly x characters with word can be the solution
            wordlist = [
                other for other in wordlist if matches == sum(w == o for w, o in zip(word, other))
            ]
```

But this on its own is not sufficient. We need to shrink the list faster for the big test cases, which requires the second observation:
2. We eliminate more words by choosing words that are more similar to the rest of the wordlist.
If `guess("xyz") > 0`, then we can eliminate words that are dissimilar to "xyz" (see above). But we can eliminate words that are similar to "xyz" if `guess("xyz") == 0`.
"""


class Master:
    def guess(self, word: str) -> int:
        return 0
