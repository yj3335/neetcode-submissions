class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        subArrSum = 0
        left = 0
        for right in range(len(nums)):
            subArrSum += nums[right]
            while subArrSum >= target:
                ans = min(ans, right - left + 1)
                subArrSum -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0