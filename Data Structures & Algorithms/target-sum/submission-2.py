class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # 0 sum can be gotten in 1 way

        for i in range(len(nums)):
            new_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                new_dp[cur_sum - nums[i]] += count
                new_dp[cur_sum + nums[i]] += count
            dp = new_dp
        
        return dp[target]