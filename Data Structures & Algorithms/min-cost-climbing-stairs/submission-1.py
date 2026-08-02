class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(index):
            if index >= len(cost):
                return 0
            
            if index in cache:
                return cache[index]

            ans = cost[index]
            ans += min(dfs(index+1), dfs(index+2))
            cache[index] = ans
            return ans
        return min(dfs(0), dfs(1))