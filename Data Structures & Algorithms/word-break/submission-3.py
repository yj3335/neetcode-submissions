class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}

        def dfs(index):
            if index == len(s):
                return True
            if index in dp:
                return dp[index]
            
            for j in range(index, len(s)):
                w = s[index:j+1]
                if w in wordDict and dfs(j+1):
                    dp[index] = True
                    return True
            
            dp[index] = False
            return False
        
        return dfs(0)

