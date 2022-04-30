class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix strs[0]
        for s in strs:
            while prefix and not s.startsWith(prefix):
                prefix = prefix[:-1]
        return prefix