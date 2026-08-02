class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {n : 1}
        def dfs(steps):
            if steps > n:
                return 0
            
            if steps in cache:
                return cache[steps]
            
            ans = dfs(steps+1) + dfs(steps+2)
            cache[steps] = ans
            return ans
        return dfs(0)