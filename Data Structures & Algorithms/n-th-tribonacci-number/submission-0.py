class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0 : 0, 1 : 1, 2: 1}
        def dfs(index):
            if index < 0:
                return 0
            if index in cache:
                return cache[index]
            
            ans = dfs(index-2) + dfs(index-1) + dfs(index-3)
            cache[index] = ans
            return ans
        return dfs(n)
