class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort
        setNums = sorted(set(nums))
        ans = 0
        count = 1
        for num in setNums:
            if num+1 in setNums : 
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        return ans