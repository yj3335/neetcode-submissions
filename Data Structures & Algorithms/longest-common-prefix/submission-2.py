class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for ele in strs:
                if len(ele) == i or strs[0][i] != ele[i]:
                    return ans
            ans += strs[0][i]

        return ans
                
