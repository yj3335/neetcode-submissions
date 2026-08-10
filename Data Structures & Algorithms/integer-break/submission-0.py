class Solution:
    def integerBreak(self, n: int) -> int:
        #top down memoization
        dp = { 1 : 1 }

        def dfs(num):
            if num in dp:
                return dp[num]
            
            res = 0 if num == n else num 
            for i in range(1, num):
                val = dfs(i) * dfs(num-i)
                res = max(res, val)

            dp[num] = res
            return res
        
        return dfs(n)