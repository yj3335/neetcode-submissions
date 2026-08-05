class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for n in nums:
            if n < 0:
                curMax, curMin = curMin, curMax
            tempMax = n * curMax
            tempMin = n * curMin

            curMin = min(n, tempMin)
            curMax = max(n, tempMax)
            res = max(res, curMax)
        return res