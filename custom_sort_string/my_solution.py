class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        have a list of character called ans
        have a dictionary to save all the count of each character in s to a dictionary called char_freq (key: character: int, value: frequency: int)
        iterate through order from left to right. Each time, we get a character ch:
        - if ch exists in s for char_freq[ch] times, append ch for char_freq[ch] times to ans. Then, delete ch from char_freq.
        - Otherwise, continue.

        for each remaining character ch within char_freq, append ch for char_freq[ch] to the end of ans

        return ''.join(ans)
        """
        ans = []
        char_freq = dict()
        for ch in s:
            char_freq[ch] = 1 if ch not in char_freq else char_freq[ch] + 1
        for ch in order:
            if ch in char_freq:
                freq = char_freq[ch]
                ans += [ch for _ in range(freq)]
                del char_freq[ch]

        for ch, freq in char_freq.items():
            ans += [ch for _ in range(freq)]

        return ''.join(ans)
