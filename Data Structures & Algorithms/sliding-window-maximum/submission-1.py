class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        ans.append(max(nums[:k]))
        left = 1
        for right in range(k, len(nums)):
            ans.append(max(nums[left:right+1]))
            left += 1
        return ans