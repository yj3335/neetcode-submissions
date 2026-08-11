class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]

            dp[(index, total)] = dfs(index+1, total - nums[index]) + dfs(index+1, total + nums[index])
            return dp[(index, total)]
            
        return dfs(0, 0)
            