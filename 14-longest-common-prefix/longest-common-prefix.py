class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)
        strs.sort()
        
        prefix = ""
        for i in range(len(shortest_string)):
            if strs[-1][i] == strs[0][i]:
                prefix += strs[0][i]
            else:
                break
                
        return prefix