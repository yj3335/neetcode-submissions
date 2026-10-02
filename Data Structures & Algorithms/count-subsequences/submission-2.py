class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(M+1):
            # ways to make empty string using nothing (even if i dont take any character from s i can still make an empty string)
            dp[i][N] = 1
        
        # calculating how many t[j:] can be made from s[i:]
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]
