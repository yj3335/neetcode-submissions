class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        dp = {}

        def dfs(index, cur_target):
            if cur_target == 0: return True
            if cur_target < 0 or index >= len(nums): return False

            if (index, cur_target) in dp:
                return dp[(index, cur_target)]

            res = (dfs(index+1, cur_target - nums[index]) or 
                    dfs(index+1, cur_target))
            dp[(index, cur_target)] = res
            return res
        
        return dfs(0, target)