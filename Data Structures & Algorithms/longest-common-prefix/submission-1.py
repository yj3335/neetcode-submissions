class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key = lambda str : len(str))
        smallest_str = sorted_strs[0]
        ans = ""
        
        for i in range(len(smallest_str)):
            found = True
            for ele in strs:
                if smallest_str[i] != ele[i]:
                    return ans
            ans += smallest_str[i]

        return ans
                
