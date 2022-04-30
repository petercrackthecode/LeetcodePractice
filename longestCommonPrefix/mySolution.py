class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for x in range(1, len(strs)):
            # If the current prefix size is 0, there's no common prefix available
            if len(prefix) == 0:
                break
            currStr = strs[x]
            for y in range(min(len(currStr), len(prefix))):
                if prefix[y] != currStr[y]:
                    prefix = prefix[:y]
                    break
                    
            if len(prefix) > len(currStr):
                prefix = currStr
        
        return prefix