class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers):
            if not numbers:
                return 0
            if len(numbers) == 1:
                return numbers[0]
            
            dp = [0] * len(numbers)
            dp[0] = numbers[0]
            dp[1] = max(dp[0], numbers[1])

            for i in range(2, len(numbers)):
                dp[i] = max(numbers[i] + dp[i-2], dp[i-1])
            
            return dp[-1]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))