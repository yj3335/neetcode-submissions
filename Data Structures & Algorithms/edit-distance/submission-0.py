class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        # i->word1, j->word2
        def dfs(i,j):
            if i == len(word1):
                return (len(word2)-j)
            if j == len(word2):
                return (len(word1) - i)
            if (i,j) in dp:
                return dp[(i,j)]
            
            ans = dfs(i+1, j+1)
            if word1[i] != word2[j]:
                ans = 1 + min(ans, dfs(i,j+1), dfs(i+1,j))
            
            dp[(i,j)] = ans
            return ans
        return dfs(0,0)