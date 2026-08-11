class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, total):
            if total == target and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            if (index, total) in dp:
                return dp[(index, total)]

            dp[(index, total)] = dfs(index+1, total - nums[index]) + dfs(index+1, total + nums[index])
            return dp[(index, total)]
        dp = {}
        return dfs(0, 0)
            