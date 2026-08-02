class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def helper(largestSum):
            subarrays = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largestSum:
                    subarrays += 1
                    curSum = n
            return (subarrays + 1) <= k

        left, right = max(nums), sum(nums)
        res = right

        while left<=right:
            mid = left + (right-left) // 2
            if helper(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res